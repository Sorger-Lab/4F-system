#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import imageio
import matplotlib.pyplot as plt


# In[34]:


#b is the mask b, the image size is 1080,1080
def SLM_mask(b,offset=0,size=1080):
    #use 50*50 to present one dot
    dot=50
    holder=np.zeros((size,size))
    for i in range(len(b)):
        holder[i*dot:i*dot+dot,i*dot:i*dot+dot]=b[i]
    holderfft=np.fft.fft2(holder)
    
    #normalize b fft
    holderfft=holderfft/holderfft[0,0]
    
    
    green=np.zeros((size,size))
    blue=np.zeros((size,size))
    angle=np.zeros((size,size))
    
    plt.imshow(holderfft.real)
    plt.colorbar()
    plt.show()
    
    
    for i in range(size):
        for j in range(size):
            if holderfft.real[i,j]<1e-6 and holderfft.imag[i,j]<1e-6:
                angle[i,j]=0
            if holderfft.real[i,j]<1e-6:
                angle[i,j]=np.pi/2
            else:
                angle[i,j]=np.arctan(holderfft.imag[i,j]/holderfft.real[i,j])

        
    angle_delta=np.pi-np.arccos(2*np.abs(holderfft)**2-1)
    
    green=(angle-angle_delta/2)/2/np.pi*255
    blue=(angle-angle_delta/2)/2/np.pi*255
    
    for i in range(size):
        for j in range(size):
            if green[i,j]<0:
                green[i,j]+=255
            if blue[i,j]<0:
                blue[i,j]+=255
    
    return green, blue

def DMD_mask(a,size=1080):
    dot=50
    holder=np.zeros((size,size))
    for i in range(len(a)):
        holder[i*dot:i*dot+dot,i*dot:i*dot+dot]=a[i]

    return holder


# In[39]:


a_bar = [1,0,1,1,0,1,1,0,1,1,1,0,0,1,1]
b_bar = [1,1,1,1,0,1,1,0,0,0,0,0,1,1,1]

red=DMD_mask(a_bar)*255
green, blue=SLM_mask(b_bar)


# In[50]:


color=np.zeros((1080,1080,3)).astype(int)
color[:,:,0]=red.astype(int)
color[:,:,1]=green.astype(int)
color[:,:,2]=blue.astype(int)

plt.imshow(color)
plt.colorbar()
plt.show()


# In[49]:


np.min(color)

