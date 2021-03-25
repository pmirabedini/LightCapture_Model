#!/usr/bin/python2.7

import numpy as np
import InitialFuncs as IF
import HitsPillarFunc as HP

def FollowRay(Lambda,Pil_height,L,R):
    x_hit = []
    y_hit = []
    z_hit = []
    RES = []
    r = 0
    z = 0
    
    #define a random ray direction and angles:
    
    while r<R:        
        x = np.random.random()*L
        y = np.random.random()*L
        r = np.sqrt(x**2+y**2)
       
    Th,phi = IF.get_random_direction_angles()
    phi = np.pi-phi
    
    
    #parameters:
    
    global N_absorbed_pillar
    global N_absorbed_Ground
    global N_absorbed_water
    global N_lost
    global N_lost_top
    global N_diffuse
    global N_specular
    N_absorbed_pillar=0
    N_absorbed_Ground = 0
    N_absorbed_water = 0
    N_lost = 0
    N_lost_top = 0
    N_diffuse = 0
    N_specular = 0
    leg = 0
    Ref = 0
    keep = 0
    leg_max = 1000
    
    
    #main loop: follow a ray for leg_max times:
    
    while leg < leg_max: 
        leg+=1

        #find HitsPillarQ
        [wall,d,v,x,y,z,Th,phi,sc,xp,yp,zp,xg,yg,zg,x_nop,y_nop,z_nop,x_nog,y_nog,z_nog] = HP.HitsPillarQ(x,y,z,Pil_height,phi,Th,L,R) 
        
        # if the ray hits somewhere below the surface
        if z<0:
            # Was it absorbed by water? 
            Cw = np.exp(-v/Lambda)
            if np.random.random() > Cw:
                #print('absorbed by water')
                #RES=[2,x,y,z]
                RES = [2,x,y,z,Th,phi,sc,xp,yp,zp,xg,yg,zg,x_nop,y_nop,z_nop,x_nog,y_nog,z_nog]
                N_absorbed_water+=1
                
            # Not absorbed by water?! then it will hit something! :D
            
            # Does it hit the ground or pillar?
            elif wall >= 5:
                # Does it get absorbed by pillar or ground?
                if np.random.random() > Ref:
                    if wall == 5:
                        #print('absorbed by pillar')
                        N_absorbed_pillar+=1
                        #RES=[1,x,y,z] 
                        RES = [1,x,y,z,Th,phi,sc,xp,yp,zp,xg,yg,zg,x_nop,y_nop,z_nop,x_nog,y_nog,z_nog]
                    else:
                        #print('absorbed by ground')
                        N_absorbed_Ground+=1
                        #RES=[0,x,y,z]
                        RES = [0,x,y,z,Th,phi,sc,xp,yp,zp,xg,yg,zg,x_nop,y_nop,z_nop,x_nog,y_nog,z_nog]
                    break
                        
                #If reflected, Was it specular?
                dice2 = np.random.random()
                if sc==1:
                    N_specular+=1
                    #print('reflected specular')
                else:
                    N_diffuse+=1
                    #print('reflected diffuse')
        
        #If the ray ended up somewhere above the surface, assume it is lost
        elif z>=0: 
            #print('Left from the top surface')
            N_lost_top+=1
            #RES=[3,x,y,z]
            RES = [3,x,y,z,Th,phi,sc,xp,yp,zp,xg,yg,zg,x_nop,y_nop,z_nop,x_nog,y_nog,z_nog]
            break 
     
    # Assume the ray is lost if it did not get absorbed by leg = leg_max
    else:
        #print('lost because not absorbed after leg')
        N_lost+=1 
        #RES=[-1,x,y,z]
        RES = [-1,x,y,z,Th,phi,sc,xp,yp,zp,xg,yg,zg,x_nop,y_nop,z_nop,x_nog,y_nog,z_nog]
            
    #print (leg)        
    return RES,Th*(180/np.pi),phi*(180/np.pi),N_absorbed_pillar,N_absorbed_Ground,N_absorbed_water,N_lost,N_lost_top,N_specular,N_diffuse,d
