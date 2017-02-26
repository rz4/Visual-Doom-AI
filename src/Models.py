#!/usr/bin/python3
'''
Models.py
Authors: Rafael Zamora
Last Updated: 2/18/17

'''

"""
Script defines the models used by the Doom Ai.
Models are built using the Keras high-level neural network library.
Keras uses TensorFlow and Theano as back-ends.

***Current models are in the prototyping phase,

"""
import keras.backend as K
from keras.models import Model
from keras.layers import *
from keras.optimizers import RMSprop, SGD

class DModel:
    """
    DModel class is used to define Deep Reinforcemnet Learning models for the
    Vizdoom environment.

    """

    def __init__(self, resolution=(120, 160), nb_frames=1, nb_actions=2, depth_radius=1.0, depth_contrast=0.8):
        '''

        '''
        #Parameters
        self.depth_radius = depth_radius
        self.depth_contrast = depth_contrast
        self.loss_fun = 'mse'
        self.optimizer = RMSprop(lr=0.0001)

        #Input Layers
        x0 = Input(shape=(nb_frames, resolution[0], resolution[1]))

        #Convolutional Layer
        m = Convolution2D(32, 8, 8, subsample = (4,4), activation='relu')(x0)
        m = Convolution2D(64, 5, 5, subsample = (4,4), activation='relu')(m)
        m = Flatten()(m)

        # Fully Connected Layer
        m = Dense(4032, activation='relu')(m)
        m = Dropout(0.5)(m)

        #Output Layer
        y0 = Dense(nb_actions)(m)

        self.online_network = Model(input=x0, output=y0)
        self.online_network.compile(optimizer=self.optimizer, loss=self.loss_fun)
        self.online_network.summary()

    def predict(self, game, q):
        '''
        '''
        a = q
        return a

    def load_weights(self, filename):
        '''
        '''
        self.online_network.load_weights('../data/model_weights/' + filename)
        self.online_network.compile(optimizer=self.optimizer, loss=self.loss_fun, metrics=['accuracy'])

    def save_weights(self, filename):
        '''
        '''
        self.online_network.save_weights('../data/model_weights/' + filename, overwrite=True)
