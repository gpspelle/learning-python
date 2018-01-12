# Sigmoid neuron

This README explain what math is behind a sigmoid neuron.

## Sigmoid neuron properties

A sigmoid neuron has weights (w) for it's inputs and a bias (b), equal as a 
perceptron. But the output function is controlled by a sigma factor.

Output = sigma * (w . x + b), where '.' is a doc product between weight and input
vectors.

And, sigma = 1 / (1 + exp(- w . x - b)).

Then, the main difference is that a sigmoid neuron is smoother, because it can
assume a inifity of values between 0 and 1. 

## Reference

[PurlpleBooth](http://neuralnetworksanddeeplearning.com/chap1.html)

