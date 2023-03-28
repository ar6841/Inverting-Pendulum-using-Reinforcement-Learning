#!/usr/bin/env python
# coding: utf-8


import numpy as np
import pendulum
epsilon = 0.1                  #epsilon greedy probability
N = 100                        #length of each episode
alpha = 0.1                    #learning rate
step_size = pendulum.DELTA_T   #size of each step (gamma)

controls = np.array([-4,0,4])
