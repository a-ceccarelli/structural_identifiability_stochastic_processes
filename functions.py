# importing all the libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import copy
import random
import pandas as pd
import math
import scipy
from scipy.stats import norm, expon
from scipy.linalg import null_space
import time

import os
cwd = os.getcwd()


def n_state_model_with_random_IC(delta_t, T, V, Lambda, P, a, Sigma, sigma, t0=0.0, state='?', seed=1223, checks=False):
    """
    delta_t = time step (s)
    T = total time (s)
    
    #all velocities (with sign)   
    V = [v_1, v_2, ..., v_n] # here indexed 0,1,...,n-1
    
    # rates time spent on state i
    Lambda = [lambda_1, lambda_2, ..., lambda_n] = (lambda_i) # here indexed 0,1,...,n-1
    
    # transition matrix: p_ij probability of switching from i to j
    P = (p_ij)            
    
    sigma #noise std
    
    x0 = initial position
    state = initial state known or '?'
    seed = select random seed
    """
    # set a random seed
    np.random.seed(seed)
    random.seed(seed)
    #print(V, Lambda, P, sigma)

    if checks:
    
        if delta_t<=0 or T<delta_t:
            print('Error defining time')
            return None
        
        n = Lambda.shape[0]
        
        if np.any(Lambda <= np.zeros(n)):
            print('Error defining lambdas')
            return None
        
        if n!=P.shape[0] or n!=P.shape[1] or n!=V.shape[0]:
            print('Error with dimensions')
            return None
        
        if np.any(np.diag(P) != np.zeros(n)):
            print('Error defining transition matrix P diag')
            return None
            
        if np.any(np.testing.assert_allclose(np.sum(P, axis=1), np.ones(n), rtol=1e-07)):
            print('Error defining transition matrix P sum')
            return None
        
        if np.any(sigma < 0):
            print('Error defining noise parameter sigma')
            return None
        
    else:
        n = Lambda.shape[0]
        
    x0 = np.random.normal(loc=0, scale=Sigma)
        
    t = [t0]
    x = [x0]
    curr_dt = 0
    curr_dx = 0

    #Building Q transpose
    Q = np.zeros((n,n))
    for i in range(n):
        for j in range(0,i):
            Q[i,j] = Lambda[i]*P[i,j]
        Q[i,i] = -Lambda[i]
        for j in range(i+1,n):
            Q[i,j] = Lambda[i]*P[i,j]
    Qt = Q.T
    
    state = random.choices(np.arange(n), weights=a, k=1)[0]
        
    state_save = []
        
    while t[-1]<T: # T is in seconds again
        curr_dt = np.random.exponential(scale=1/Lambda[state])
        curr_dx = curr_dt*V[state]
        t.append(t[-1]+curr_dt)
        x.append(x[-1]+curr_dx)
        state_save.append(state)
        state = random.choices(np.arange(n), weights=P[state, :], k=1)[0]
    
    state_save.append(state)
    
    #CREATE delta_t=0.3 approx
    t_points = np.linspace(0, T, int(T/delta_t)+1) #e.g. 0, 0.3, 0.6, ..., 60
    #print(x,t)
    x_points = np.zeros(t_points.shape)
    # generate error points
    y_points = np.random.normal(loc=0, scale=sigma,
                                size=t_points.shape)
    switches = np.zeros(t_points.shape)
    all_states_save = [[] for i in range(int(T/delta_t)+1)]
    
    j = 0
    p = np.polyfit(t[j:j+2], x[j:j+2], 1)
    for i in range(0,int(T/delta_t)+1):
        todo = True
        while todo:
            all_states_save[i].append(state_save[j])
            if t_points[i]>=t[j] and t_points[i]<=t[j+1]:
                x_points[i] += np.polyval(p, t_points[i])
                y_points[i] += x_points[i]
                todo = False
                
                if t_points[i]==t[j]:
                    if i!= 0:
                        switches[i] += 1
            else:
                j+=1
                switches[i] +=1
                p = np.polyfit(t[j:j+2], x[j:j+2], 1)
    Nswitches = switches[1:]
    states = all_states_save[1:]
     
    return x_points, y_points, t, Nswitches, states