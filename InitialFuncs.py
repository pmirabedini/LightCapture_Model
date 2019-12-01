#!/usr/bin/python2.7
#InitialFuncs

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#generate random angles:

def get_random_direction_angles():
    Theta2 = (np.random.rand()-0.5)*2*np.pi  
    phi2 = (np.random.rand())*2*np.pi   
    return Theta2, phi2   


#generate normal vector:

def normal(v):
    n_v = v/np.sqrt(v[0]**2+ v[1]**2+v[2]**2)
    return n_v


#function that takes polar angles defined relative to the normal vector and convert them to angles in cartesian:

def rel_dir_cartesian(normalV,V2, Theta2, phi2):
 
    #The vector and angles in the original coordinate system:
    v2 = [np.sin(phi2)*np.cos(Theta2),np.sin(phi2)*np.sin(Theta2),np.cos(phi2)]

    #define the new coordinate system:
    x_nc = V2
    z_nc = normal(normalV)
    y_nc = np.cross(z_nc,x_nc)
                
    #v2 direction in the cartesian coordinates:
    v2_cart = np.multiply(v2[0],x_nc) + np.multiply(v2[1],y_nc) + np.multiply(v2[2],z_nc)
                
    #find the angles in cartesian and call them Theta3 and phi3:
    Theta3 = np.arctan2(v2_cart[1],v2_cart[0])
    phi3 =  np.arccos(v2_cart[2])
    return Theta3, phi3


