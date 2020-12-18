### Introduction

- When trained on mid-sized datasets such as ImageNet, such models yield modest accuracies of a few percentage points below ResNets of comparable size.
- Transformers lack some of the inductive biases inherent to CNNs, such as translation equivariance and locality, and therefore do not generalize well when trained on insufficient amounts
of data.
- However, the picture changes if the models are trained on larger datasets (14M-300M images).

### Model


**Vision Transformers**

- The standard Transformer receives as input a 1D sequence of token embeddings.
- To handle 2D images, we reshape the image x ∈ R^(H×W×C) into a sequence of flattened 2D patches xp ∈ R^(N×(P2·C)), 
    where (H, W) is the resolution of the original image, 
    C is the number of channels,
    (P, P) is the resolution of each image patch, and 
    N = HW/P2 is the resulting number of patches, which also serves as the effective input sequence length for the Transformer.
- The Transformer uses constant latent vector size D through all of its layers, so we flatten the patches and map to D dimensions 
  with a trainable linear projection (Eq. 1). We refer to the output of this projection as the patch embeddings.
- Position embeddings are added to the patch embeddings to retain positional information.
- We use standard learnable 1D position embeddings, since we have not observed significant performance gains from using more advanced 2D-aware position embeddings.
-  Layernorm (LN) is applied before every block, and residual connections after every block.

**Hybrid Architectures**

- In this hybrid model, the patch embedding projection E (Eq. 1) is applied to patches extracted from a CNN feature map.

**Fine-tuning and Higher Resolution**

- The Vision Transformer can handle arbitrary sequence lengths (up to memory constraints), 
  however, the pre-trained position embeddings may no longer be meaningful.
- We therefore perform 2D interpolation of the pre-trained position embeddings, according to their location in the original image.
- Note that this resolution adjustment and patch extraction are the only points at which an inductive bias about the 2D structure of the images is manually injected into the Vision Transformer.

**Appendix**

- We fine-tune all ViT models using SGD with a momentum of 0.9.

### Results

<insert-image>
