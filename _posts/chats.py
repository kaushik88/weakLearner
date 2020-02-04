from datetime import datetime
import ciso8601

VISITOR_ROLE = 'visitor'
AGENT_ROLE = 'agent'

from typing import List
from abc import abstractmethod

import random

import dateutil.parser
from datetime import datetime
import json
import os
import pdb, time
import spacy

def parse_timestamp(obj):
    try:
        return ciso8601.parse_datetime(obj)
    except:
        if isinstance(obj, datetime):
            return obj
        elif isinstance(obj, float):
            return datetime.utcfromtimestamp(obj)
        elif isinstance(obj, int):
            return datetime.utcfromtimestamp(obj/1000)
        elif isinstance(obj, str):
            return dateutil.parser.parse(obj)
        elif isinstance(obj, bytes):
            return dateutil.parser.parse(str(obj))
        else:
            raise Exception('Unknown type for date: {}'.format(type(obj)))

class Message(object):
    def __init__(self, text, timestamp, speaker_role, speaker_id, **kwargs):
        if not isinstance(timestamp, float):
            print('Message timestamp is not a float! {} {}'.format(
                timestamp, type(timestamp)))
            timestamp = datetime.utcnow()

        self.text = text
        self._timestamp = timestamp
        self.speaker_role = speaker_role
        self.speaker_id = speaker_id
        self._features = None

        if 'sid' in kwargs: self.sid = kwargs['sid']
        else: self.sid = None

        if 'annotations' in kwargs: self.annotations = kwargs['annotations']
        else: self.annotations = None

    @property
    def timestamp(self):
        if isinstance(self._timestamp, datetime):
            return self._timestamp.timestamp()
        else:
            return self._timestamp

    @property
    def author_is_agent(self):
        return self.speaker_role == 'agent'

    def to_dict(self, with_features=False):
        serialized = {
            'text': self.text,
            'timestamp': self.timestamp,
            'speaker_role': self.speaker_role,
            'speaker_id': self.speaker_id,
            'annotations': self.annotations,
            'sid': self.sid
        }

        if with_features and self._features:
            serialized['features'] = self._features.to_dict()

        return serialized

    @classmethod
    def from_dict(cls, d):
        # TODO: make to_dict and from_dict consistent with each other.
        try:
            return cls(
                text=d['text'],
                timestamp=d['pubDate'],
                speaker_role='agent' if d['authorIsAgent'] else 'visitor',
                speaker_id=d.get('author'))
        except Exception as e:
            print(
                'Unable to parse message from dictionary with error {}'.format(
                    str(e)))
            raise e

    def __repr__(self):
        return '[{}] {}: {}'.format(self.timestamp, self.speaker_role,
                                    self.text)


class Chat(object):
    VISITOR = VISITOR_ROLE
    AGENT = AGENT_ROLE

    def __init__(self,
                 body,
                 country,
                 tags,
                 open_date,
                 start_url,
                 chat_name,
                 annotations,
                 agent_platform_ids=[],
                 visitor_platform_ids=[],
                 **kwargs):
        self.messages = [self._create_message(m) for m in body]
        self.tags = tags
        self.country = country
        self.agent_platform_ids = agent_platform_ids
        self.visitor_platform_ids = visitor_platform_ids

        self.open_date = parse_timestamp(open_date)
        self.start_url = start_url
        self.chat_name = chat_name
        self.annotations = annotations
        self._features = None
        self.turns = None

    def _create_message(self, obj):
        if isinstance(obj, Message):
            return obj
        elif isinstance(obj, dict):
            return Message(**obj)
        else:
            raise Exception('Unknown type for message: {}'.format(type(obj)))

    def set_turns(self, turn_list):
        self.turns = turn_list

    def set_label(self, label):
        self.visitor_dropped = label

    @classmethod
    def from_dict(cls, d):
        body = d.get('messages', [])
        country = d.get('country')
        tags = d.get('tags', [])
        start_url = d.get('start_url')
        agent_platform_ids = d.get('agent_platform_ids')
        visitor_platform_ids = d.get('visitor_platform_ids')
        annotations = d.get('label')

        assert 'chat_name' in d, 'Dict to initialize Chat must have chat_name field.'
        chat_name = d['chat_name']

        assert 'open_date' in d, 'Dict to initialize Chat must have open_date field.'
        open_date = d['open_date']

        return Chat(
            body=body,
            country=country,
            tags=tags,
            open_date=open_date,
            start_url=start_url,
            chat_name=chat_name,
            annotations=annotations,
            agent_platform_ids=agent_platform_ids,
            visitor_platform_ids=visitor_platform_ids)

    def to_dict(self, with_features=False):
        serialized = {
            'country':
            self.country,
            'open_date':
            self.open_date.isoformat(),
            'start_url':
            self.start_url,
            'chat_name':
            self.chat_name,
            'tags':
            self.tags,
            'agent_platform_ids':
            self.agent_platform_ids,
            'visitor_platform_ids':
            self.visitor_platform_ids,
            'body':
            [message.to_dict(with_features) for message in self.messages],
            'annotations':
            self.annotations,
        }

        if with_features and self._features:
            serialized['features'] = self._features.to_dict()

        return serialized

    @property
    def last_message(self):
        if not self.messages:
            return None
        else:
            return self.messages[-1]

    def __getitem__(self, key):
        if not isinstance(key, slice): return self.messages[key]
        (start, end, step) = (key.start, key.stop, key.step)

        messages = self.messages.__getitem__(key)

        return PartialChat(
            body=messages,
            country=self.country,
            tags=self.tags,
            open_date=self.open_date.isoformat(),
            start_url=self.start_url,
            chat_name=self.chat_name)

    @property
    def contexts(self):
        return list(self.iter_context())

    def iter_context(self):
        """ Iterate through the conversation and replay context.
        """
        for mi in range(len(self) + 1):
            yield self[:mi]

    def __repr__(self):
        return self.chat_name

    def __len__(self):
        return len(self.messages)

    def __bool__(self):
        return len(self) > 0

    def __contains__(self, partial_chat):
        return set(partial_chat.messages).issubset(set(self.messages))

    @property
    def agent_spoke_last(self):
        return len(
            self.messages) > 0 and self.messages[-1].speaker_role == 'agent'


# TODO: this should be fixed - Chat should inherit from PartialChat, because
# the latter is more generic.
class PartialChat(Chat):
    """ Context for a certain point in conversation.
    """

    def __init__(self, **kwargs):
        super(PartialChat, self).__init__(**kwargs)

    def __repr__(self):
        return '{}[:{}]'.format(self.chat_name, len(self.messages))


class Chats(object):
    def __init__(self, chats):
        self.chats = list(chats)
        self.cursor = 0

    @classmethod
    def load(cls, json_path):
        return cls.from_json(json_path)

    @classmethod
    def from_json(cls, json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            raw_chats = json.load(f)

        chats = []
        for raw_chat in raw_chats:
            chats += [Chat.from_dict(dict(raw_chat))]

        return cls(chats=chats)

    @classmethod
    def from_postgres(cls, postgresurl, start_datetime, end_datetime, tags,
                      company):
        from .chats_postgres import ChatsPostgresLoader
        os.environ['CRESTA_POSTGRES'] = postgresurl
        return ChatsPostgresLoader.get_chats(
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            tags=tags,
            company=company)

    @classmethod
    def from_graphql(cls,
                     endpoint,
                     start_datetime,
                     end_datetime,
                     tags,
                     company,
                     limit=None,
                     chat_name=None):
        from .chats_graphql import ChatsGraphQLLoader
        loader = ChatsGraphQLLoader(endpoint)
        return loader.get_chats(
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            tags=tags,
            company=company,
            limit=limit,
            chat_name=chat_name)

    def shuffle(self):
        chats = list(self.chats)
        random.shuffle(chats)
        return Chats(chats)

    def filter(self, func):
        chats = list(filter(func, self.chats))
        return Chats(chats)

    def __getitem__(self, key):
        return self.chats[key]

    def dump_json(self, json_path):
        with open(json_path, 'w') as f:
            json.dump(list(map(Chat.to_dict, self.chats)), f)

    def dump(self, json_path):
        return self.dump_json(json_path)

    def __iter__(self):
        return iter(self.chats)

    def __len__(self):
        return len(self.chats)
