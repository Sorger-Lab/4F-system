import numpy as np
import math
import matplotlib.pyplot as plt
from math import sqrt

#first
# a_bar = [0,1,0,0,1,0]
# b_bar = [0,1,1,1,1,0]

#second
# a_bar = [0,1,0,0,1,1]
# b_bar = [1,1,1,0,1,0]

#third
# a_bar = [1,0,1,0,1,1,0,0,1,0,0,0]
# b_bar = [1,0,1,1,0,1,0,0,1,0,1,1]

#main example
a_bar = [1,0,1,1,0,1,1,0,1,1,1,0,0,1,1]
b_bar = [1,1,1,1,0,1,1,0,0,0,0,0,1,1,1]

a_bar = np.append(a_bar, np.zeros((len(a_bar)-1,1)))
b_bar = np.append(b_bar, np.zeros((len(b_bar)-1,1)))

if len(a_bar) != len(b_bar): 
	print("error")
else: N = len(a_bar)

image_a_bar = np.zeros((N,N))
image_b_bar = np.zeros((N,N))


for i in range(len(image_a_bar)):
	image_a_bar[i,i] = a_bar[i]
	image_b_bar[i,i] = b_bar[i]

def DFT_matrix(N):
    i, j = np.meshgrid(np.arange(N), np.arange(N))
    omega = np.exp( - 2 * math.pi * 1J / N )
    W = np.power( omega, i * j ) / sqrt(N)
    return W

def IDFT_matrix(N):
    i, j = np.meshgrid(np.arange(N), np.arange(N))
    omega = np.exp( 2 * math.pi * 1J / N )
    W = - np.power( omega, i * j ) / sqrt(N)
    return W

W = DFT_matrix(len(image_a_bar))
dft_of_image_a_bar = W.dot(image_a_bar).dot(W)

W = DFT_matrix(len(image_b_bar))
dft_of_image_b_bar = W.dot(image_b_bar).dot(W)

convolution = np.multiply(dft_of_image_a_bar,dft_of_image_b_bar)

W = IDFT_matrix(len(convolution))
dft_of_convolution = W.dot(convolution).dot(W)
dft_of_convolution = dft_of_convolution.real

for i in range(len(dft_of_convolution)):
	for j in range(len(dft_of_convolution)):
		if dft_of_convolution[i,j]<10**(-5): dft_of_convolution[i,j] = 0.

norm = 10000

for i in range(len(dft_of_convolution)):
	for j in range(len(dft_of_convolution)):
		if dft_of_convolution[i,j]<norm and dft_of_convolution[i,j]!=0.: norm = dft_of_convolution[i,j]

dft_of_convolution = dft_of_convolution/norm

print(np. diagonal(dft_of_convolution))


plt.imshow(dft_of_convolution)

plt.show()