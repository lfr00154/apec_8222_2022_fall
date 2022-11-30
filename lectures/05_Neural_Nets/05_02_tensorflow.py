import tensorflow as tf
import numpy as np
import tensorflow_datasets
#mnist = tensorflow_datasets.load('mnist')

def run_cnn():
   mnist = tensorflow_datasets.load('mnist')
   learning_rate = 0.0001
   epochs = 10
   batch_size = 50