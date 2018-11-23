# PERCEPTRON ALGORITHM

import numpy as np 

def stepFunction(t):
	if t > 0:
		return 1
	return 0

def prediction(X, W, b):
	return(stepFunction(np.matmul(W, X) + b))


def perceptronStep(X, y, W, b, learn_rate = 0.01):
    # Fill in code
    for i in range(len(X)):
        y_hat = prediction(X[i],W,b)
        if y[i]-y_hat == 1:
            W[0] += X[i][0]*learn_rate
            W[1] += X[i][1]*learn_rate
            b += learn_rate
        elif y[i]-y_hat == -1:
            W[0] -= X[i][0]*learn_rate
            W[1] -= X[i][1]*learn_rate
            b -= learn_rate
    return W, b


# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
score = []
def softmax(L):
    expL = np.exp(L)
    sumL = sum(expL)
    for i in range(len(expL)):
        score.append(expL[i]/sumL)
    return score


# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    CE = []
    for i in range(len(Y)):
        ce =  Y[i] * np.log(P[i]) + (1 - Y[i]) * np.log(1 - P[i]) 
        CE.append(ce)
    return -np.sum(CE)
