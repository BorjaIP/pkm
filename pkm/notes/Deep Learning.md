---
title: Deep Learning
created: Saturday 12th April 2025 12:47
aliases:
  - dl
tags:
---
 **Deep learning** is a specialized subset of [[machine learning]] that uses multi-layered neural networks to analyze and process data, mimicking the way the human brain works. It is particularly effective at **recognizing complex patterns and making decisions based on large amounts of unstructured data**.

| Tool/Framework                                          | Description                                                                     |
| ------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [Deepforge](https://github.com/deepforge-dev/deepforge) | A modern development environment for deep learning                              |
| [Havorod](https://github.com/horovod/horovod)           | Distributed training framework for TensorFlow, Keras, PyTorch, and Apache MXNet |
| [DeepSpeed](https://github.com/microsoft/DeepSpeed)     | Deep learning optimization library                                              |
# Neural Networks

[**Neural network**](https://www.geeksforgeeks.org/neural-networks-a-beginners-guide/) consists of layers of interconnected nodes, or neurons, that collaborate to process input data. In a fully connected deep neural network, data flows through multiple layers, where each neuron performs nonlinear transformations, allowing the model to learn intricate representations of the data.

In a deep neural network, the **input layer** receives data, which passes through **hidden layers** that transform the data using nonlinear functions. The final **output layer** generates the model’s prediction.

- **Input Layer:** Receives raw data (e.g., pixels, words).
- **Hidden Layers:** Extract hierarchical features (shallow → deep layers).
- **Output Layer:** Produces predictions (e.g., class labels, regression values).

![[dl_layers.png]]

## Activation Functions

In a neural network, **activation functions are like the decision-makers**. They determine what **information should be passed along to the next layer**. These functions add a level of complexity, enabling the network to learn from the data and make nuanced decisions. Introduce non-linearity to model complex patterns:

- **ReLU (Rectified Linear Unit):** Most common (fast, avoids vanishing gradients).
- **Sigmoid/Tanh:** For probabilities or bounded outputs.
- **SoftMax:** For multi-class classification.
## Loss Function

The loss function is the **difference between actual and predicted values**. It allows neural networks to track the model's overall performance. Depending on specific problems, we chose a certain type of function, for example:

- Mean Squared Error ([[Machine Learning#Mean Squared Error (MSE)|MSE]]).
- Binary cross-entropy
- Categorical hinge
- Huber
- Sparse categorical cross-entropy
## Backpropagation

In **forwarding propagation**, we initialize our neural network with random inputs to produce an output that is random too. To make our model perform better, we adjust weights randomly using **backpropagation**. To track the model's performance, we need a **loss function** that will find **global minimal** to maximize the model's accuracy. 
## Stochastic Gradient Descent

**Gradient descent** is used to **optimize loss function** by changing weights in a controlled way to achieve minimum loss. Now we have an objective, but we need direction on whether to increase or decrease the **weights** to achieve better performance. The derivative of the loss function will give us direction and we can use it to update the weights of the network.

An **optimization algorithm** used to minimize a **loss function** $J(θ)$ by iteratively adjusting model parameters $θ$

$$θ_{t+1}=θ_{t} - \alpha\cdot\nabla J(θ_{t})$$
Where:

- $θ_{t}$​ = Current model parameters (weights, biases) at step $t$.
- $α$ = **Learning rate** (step size, controls how aggressively we update $θ$).
- $\nabla J(θ_{t})$ = **Gradient** (vector of partial derivatives of $J$ w.r.t. each $θ$).

| **Type**                | **How It Works**                                              | **When to Use**                        |
| ----------------------- | ------------------------------------------------------------- | -------------------------------------- |
| **Batch GD**            | Computes gradient over the **entire dataset** per step.       | Small datasets, precise updates.       |
| **Stochastic GD (SGD)** | Uses **one random sample** per step (noisy, but faster).      | Large datasets, escapes local minima.  |
| **Mini-Batch GD**       | Compromise: Uses **small random subsets (batches)** per step. | Most common (balances speed/accuracy). |
## Techniques

Various methods can be used to create strong deep learning models. 
### Learning rate decay

The learning rate is a hyperparameter - a factor that defines the system or sets conditions for its operation prior to the learning process - that controls how much change the model experiences in response to the estimated error every time the model weights are altered. Learning rates that are too high can result in unstable training processes or the learning of a suboptimal set of weights. Learning rates that are too small can produce a lengthy training process that has the potential to get stuck.

The learning rate decay method - also called _learning rate annealing_ or _adaptive learning rate_ - is the process of adapting the learning rate to increase performance and reduce training time. The easiest and most common adaptations of the learning rate during training include techniques to reduce the learning rate over time.

Common techniques in the learning rate decay method include the following:

- **Step decay.** Reduces the learning rate by a factor at specific intervals.
- **Exponential decay.** Continuously decreases the learning rate at an exponential rate.
- **1/t decay.** Reduces the learning rate inversely proportional to the iteration number.
### Transfer learning

This process involves **perfecting a previously trained model** on a new but related problem. It requires an interface to the internals of a preexisting network. First, users feed the **existing network** new data containing previously unknown classifications. Once adjustments are made to the network, new tasks can be performed with more specific categorizing abilities.

This method has the advantage of requiring much less data than others, thus reducing computation time to minutes or hours.
### Training from scratch

This method **requires** a developer to collect **a large, labeled data set and configure a network architecture** that can learn the features and model. This technique is especially useful for new applications, as well as applications with many output categories. However, it's a less common approach, as it requires inordinate amounts of data and computational resources, causing training to take days or weeks.
### Dropout

This method attempts to [solve the problem of overfitting in networks](https://www.techtarget.com/searchenterpriseai/feature/How-to-avoid-overfitting-in-machine-learning-models) with large amounts of parameters by randomly dropping units and their connections from the neural network during training.

It has been proven that the dropout method can improve the performance of neural networks on [supervised learning](https://www.techtarget.com/searchenterpriseai/definition/supervised-learning) tasks in areas such as [speech recognition](https://www.techtarget.com/searchcustomerexperience/definition/speech-recognition), document classification and computational biology.
# Neural Network Architectures

## Standard

### Perceptron

- The simplest type of neural network unit.
- Performs binary classification using a linear decision boundary.
### Multilayer Perceptron (MLP)

- A feedforward neural network with one or more hidden layers.
- Can model non-linear functions using activation functions like ReLU, sigmoid, or tanh.
### Residual Networks (ResNet)

ResNets provide an alternate pathway for data to flow to make the training process much faster and easier. The core idea behind ResNet is that a deeper network can be made from a shallow network by copying weight from the shallow counterparts using identity mapping.

The data from previous layers is fast-forwarded and copied much forward in the Neural Networks. This is what we call _skip connections_ first introduced in Residual Networks to resolve vanishing gradients.
## RNNs (Recurrent Neural Networks)



### LSTM (Long Short-term Memory Networks)

## CNNs (Convolutional Neural Networks)


## DNNs (Deconvolutional Neural Networks)

![[Pasted image 20250412134421.png]]

## GANs (Generative adversarial networks)

## Transformers
