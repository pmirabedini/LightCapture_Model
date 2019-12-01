#!/usr/bin/python2.7

import numpy as np
import InitialFuncs as IF
import HitsPillarFunc as HP
import FollowRayFunc as FRF

def Ray_Trace(N,Pil_height,Lambda,L,R):
    N_pil = 0
    N_wat = 0
    N_los = 0
    N_gr = 0
    N_top = 0
    N_spec = 0
    N_dif = 0
    hitpoint = [] #pillar and ground
    hitpoint_nopil = [] #if there was no pillar
    hitpoint_nogr = [] #if there was no ground
    hitpoint_gr = [] #only ground
    hitpoint_pil = [] #only pillar
    points_topim = [] #top
    hitangle = []
    hitangle_nopil = []
    hitangle_nogr = []
    hitangle_gr = []
    hitangle_pil = []
    angles_topim = []
    
    for i in range(0,N):
        OUT=FRF.FollowRay(Lambda,Pil_height,L,R)
        p = list(OUT[0])
        N_spec = N_spec + OUT[9]
        N_dif = N_dif + OUT[8]
        d = OUT[10]
        
        if 0<=p[0]<= 1:
            hitpoint.append(p[1:4])
            #print("hitpoint",hitpoint)
            hitangle.append([np.arctan2(p[1],p[2]),np.arctan2(d,p[3])])
            
            if p[0]==1:
                N_pil+=1
                hitpoint_pil.append(p[7:10])
                hitangle_pil.append([np.arctan2(p[7],p[8]),np.arctan2(d,p[9])])
                hitpoint_nopil.append(p[13:16]) 
                hitangle_nopil.append([np.arctan2(p[13],p[14]),np.arctan2(d,p[15])])
                
            elif p[0]==0:
                N_gr+= 1
                hitpoint_gr.append(p[10:13])
                hitangle_gr.append([np.arctan2(p[10],p[11]),np.arctan2(d,p[12])])
                hitpoint_nogr.append(p[16:19])
                hitangle_nogr.append([np.arctan2(p[16],p[17]),np.arctan2(d,p[18])])
        
        elif p[0] == 2:
            N_wat += 1
            
        elif p[0] == 0:
            N_gr += 1
            
        elif p[0] == 3:
            N_top += 1
            if 0<=p[3]<10:
                points_topim.append(p[1:4])
                angles_topim.append([np.arctan2(p[1],p[2]),np.arctan2(d,p[3])])
        
        else:
            N_los += 1
    i=i+1
    
    #probabilities:

    P_pil = N_pil/N
    P_gr = N_gr/N
    P_wat = N_wat/N
    P_top = N_top/N
    P_los = N_los/N
    
    #print('#diffuse reflections for N rays',N_dif)
    #print('#specular reflections for N rays', N_spec)
    
    return P_pil,P_gr,P_wat,P_top,P_los,hitpoint,hitpoint_pil,hitpoint_gr,hitpoint_nopil,hitpoint_nogr,points_topim,hitangle,hitangle_pil,hitangle_gr,hitangle_nopil,hitangle_nogr,angles_topim,N_dif,N_spec
