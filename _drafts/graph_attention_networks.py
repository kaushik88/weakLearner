### Introduction

- Leveraging masked self-attentional layers to address the shortcomings of prior methods based on graph convolutions
- Stacking layers in which nodes are able to attend over their neighborhoods’ features, we enable (implicitly) specifying different weights to 
  different nodes in a neighborhood.
- One of the benefits of attention mechanisms is that they allow for dealing with variable sized inputs, focusing on the most relevant parts of the input to make
decisions. 

### Model

**Graph Attention Layer**

- The input to our layer is a set of node features, h = {~h1, ~h2, . . . , ~hN }, ~hi ∈ R(F) , 
  where N is the number of nodes, and
  F is the number of features in each node.
- The layer produces a new set of node features (of potentially different cardinality F').
- a shared linear transformation, parametrized by a weight matrix, W ∈ R F'xF is performed on every node.
- In our experiments, the attention mechanism a is a single-layer feedforward neural network, parametrized by a weight vector ~a ∈ R^2F', 
  and applying the LeakyReLU nonlinearity (with negative input slope α = 0.2).
- Similar to Vaswani et al, we also do Multi-head attention.

