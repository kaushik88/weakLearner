---
layout: post
mathjax: true
title: "Practical Aspects of Deep Learning"
tags:
- DL
categories:
- Applied
thumbnail_path: blog/personal/deepl.png
---

Notes from Coursera course by Andrew Ng.

**Train/Dev/Test**

- Train on train test.
- Dev for hyper param tuning
- Test set for evaluation (unbiased).
- In recent times, dev and test is kept minimal (10,000) and this might be 1% of 1million total.
- Make sure train/dev/test come from the same distribution.
- Ok to not have a test set (replace it as a dev test).

**Bias and Variance**

high bias - underfitting (high train and dev error) and high variance - overfitting (low train error but higher dev error).

**Regularization**

- Solve high variance.
- L2 and L1 regularization (Logistic regression use-case)
- Dropout - each node, set a probability of dropping a node in the network.
- Inverted dropout - divide by keep prob. makes the expected value the same. This way no dropout at test time.
- While first testing out model, turn off dropout and plot J wrt num iterations.

**Input Normalization**

- Normalize input to 0 mean and 1 variance. Use same mean and variance in train and test set.
- Unnormalized - elliptical cost function whereas normalized is speherical.

**Vanishing/Exploding Gradients**

- For deep networks, if w_i > 1 for each of the layers, then it get too large and vice-versa.
- Initializing the weights randomly.
- Set variance of w_i to 1/n (n is the number of weights in layer)
- Xavier Initialization - sqrt(1/n) and it works well with tanh
- Variance of 2/n works well with ReLu.

**Optimization Algorithms**

- Exponentially weighted averages (light-weight) as compared to rolling 50-day averages.
- Bias correction (divite by Beta^t)
- Momentum
	- Calculate exponentially weighted average of gradients and use that to update weights.
	- W = W - alpha * (v_dw) where v_dw = beta * v_dw + (1-beta) * dW where dW is gradient.
- RMSProp
	- The main intuition is that we want the learning to slow in vertical direction and speed up in the horizontal direction.
	- W = W - alpha * dW / (sqrt(s_dW)) where v_dw = beta * s_dw + (1-beta) * dW^2
- Adam Optimizer
	- At a very high level, this combines Momentum and RMSProp.
	- Adaptive Moment Estimator.
- Learning Rate Decay
	- decrease alpha as num epochs increase.


**Batch Normalization**
- Allows larger range of hyperparams to work and also supports deeper network.
- Usually applied to z (before activation function).
- Calculate mean and variance but learn 2 params (beta and gamma) to reduce it to whatever mean and variance we want (rather than 0 mean and 1 variance).
- Use exponentially weighted averages to calculate mu and sigma and use the final result for test time.