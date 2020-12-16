### Introduction

- We present PyTorch-BigGraph (PBG), an embedding system that incorporates several modifications to traditional multi-relation embedding
systems that allow it to scale to graphs with billions of nodes and trillions of edges.
- PBG uses graph partitioning to train arbitrarily large embeddings on either a single machine or in a distributed environment.

**Challenges**

- An embedding system must be fast enough to embed graphs with 10^11 − 10^12 edges in a reasonable time.
- A model with two billion nodes and even 32 embedding parameters per node (expressed as floats) would require 800GB of memory just to store its parameters.

**Contributions**

- A block decomposition of the adjacency matrix into N buckets, training on the edges from one bucket at a time.
- Efficient negative sampling for nodes that samples negative nodes both uniformly and from the data, reuses negatives within a batch to reduce memory bandwidth.
- Support for multi-entity, multi-relation graphs with perrelation configuration options such as edge weight and choice of relation operator.

### Model

- A multi-relation graph is a directed graph G = (V, R, E) where V are the nodes (aka entities), R is a set of relations, and E is a set of edges where a generic element e = (s, r, d)
(source, relation, destination) where s, d ∈ V and r ∈ R.
- We will represent each entity and relation type with a vector of parameters. We will denote this vector as θ.
- A multirelation graph embedding uses a score function f(θs, θr, θd) that produces a score for each edge that attempts to maximize the score of f(θs, θr, θd) for any (s, r, d) ∈ E and
minimizes it for (s, r, d) !∈ E.

f(θs, θr, θd) = sim (g(s)(θs, θr), g(d)(θd, θr))
- sim is usually dot product or cosine similarity
- g is either linear, translation or complex multiplication.

**Negative sampling**

- On one hand, if we sample negatives strictly according to the data distribution, there is no penalty for the model predicting high scores for edges with rare nodes. On the
- Other hand, if we sample negatives uniformly, the model can perform very well (especially in large graphs) by simply scoring edges proportional to their source and destination
node frequency in the dataset. 
- Both of these results are undesirable, so in PBG we sample a fraction α of negatives according to their prevalence in the training data and (1−α) of them uniformly at random.By default PBG uses α = .5.
- In multi-entity graphs, negatives are only sampled from the correct entity type for an edge’s relation

L = SIGMA ( SIGMA ( max(f(e) − f(e) - f(e') + λ, 0)) e∈G and e'∈S'

### Results
