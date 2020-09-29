# Decoding-Distorted-Signals-in-Optical-Fibers
Using TensorFlow to decode signals sent through simulated optical fiber channels. This Project is a joint effort by Kartik Dutt and Lakshya Ojha of Electronics and Communications of DTU'21.
This project is part of the term project for Optical Communication.

## Understanding the Data and the Objective

Let's consider a simple baseband signal as shown below. This is the data that we use for training the model. We use this input signal and convert it to an encoded form such as Binary NRZ or 4-PAM. We also add to noise to these signals to simulate optical behavior. The model is then trained to reproduce the orignal signal with the noisy encoded signal as input.

## Simulating the Optical Channel and encoding the signal.

