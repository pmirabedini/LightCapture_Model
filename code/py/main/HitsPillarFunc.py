#!/usr/bin/python2.7

import numpy as np
import InitialFuncs as IF

def HitsPillarQ(x,y,z,pil_height,phi,Theta,L,R):
    m = np.tan(Theta)
    Theta = ((Theta+np.pi) % (2*np.pi)) - np.pi   #same as theta ??
    Theta_A = np.arctan2((R-y),-x)
    Theta_B = np.arctan2(-y,(R-x))
    global d
    global sc
    global X_nopil,Y_nopil, Z_nopil

    X_nopil, Y_nopil, Z_nopil= 0, 0, 0 
    X_nogr, Y_nogr, Z_nogr= 0, 0, 0

    Hit_ground = [0,0,0]
    Hit_pil = [0,0,0]
    
    if Theta_B >0:
        Theta_A = Theta_A -2*np.pi
        Theta_B = Theta_B -2*np.pi
    Theta_C = np.arctan2(-y,(L-x))
    Theta_D = np.arctan2((L-y),(L-x))
    Theta_E = np.arctan2((L-y),-x)
        
    if Theta_A >0:
        Theta_A = Theta_A-2*np.pi
        
    #print (Theta*180/np.pi,Theta_A*180/np.pi,Theta_B*180/np.pi,Theta_C*180/np.pi,Theta_D*180/np.pi,Theta_E*180/np.pi)
            
    if Theta_A < Theta < Theta_B:
        Ct = np.cos(Theta)
        St = np.sin(Theta)
        Ct2 = Ct*Ct
        St2 = St*St
        X = -(y*Ct*St) + (x*St2) + np.sqrt(Ct2*((R-y)*(R+y)*Ct2 + (R-x)*(R+x)*St2 + x*y*np.sin(2*Theta)))
        Y = np.sqrt(R**2-X**2)
        wall = 5
        #print('wall=5')
        Theta_n = np.arctan2(Y,X)
        d = np.sqrt((X-x)**2 + (Y-y)**2)  
        Z = d/np.tan(phi)
        Hit_pil = [X,Y,Z]
        print(Hit_pil)

        #what if there was no pillar:
        X_nopil = x - (pil_height-z)*(x-X)/(Z-z) #this is the same as when having a ground 
        Y_nopil = y - (pil_height-z)*(y-Y)/(Z-z)
        Z_nopil = pil_height
        #print(X_nopil,Y_nopil,Z_nopil)
                    
    elif Theta_B < Theta < Theta_C:
        #print('Wall 1')
        Xa = x-y/m
        X = Xa
        Y = 0
        wall = 1
        Theta_n = np.pi/2
                
    elif Theta_C < Theta < Theta_D:
        #print('Wall 2')
        Yb = y+m*(L-x)
        X = L
        Y = Yb
        wall = 2
        Theta_n = np.pi

    elif Theta_D < Theta < Theta_E:  
        #print('Wall 3')
        Xc = x+(L-y)/m
        X = Xc
        Y = L
        wall = 3
        Theta_n = -np.pi/2
            
    else:
        #print('Wall 4')
        Yd = y-x*m
        X = 0
        Y = Yd
        wall = 4
        Theta_n = 0.0
        
    d = np.sqrt((X-x)**2 + (Y-y)**2)  
    Z = d/np.tan(phi)
    #print(Z)
    v = np.sqrt((X-x)**2+(Y-y)**2+(Z-z)**2)   #we need Z here before we define v
    #Z = np.cos(phi)*v
    #print(Z)
    phi_new = phi
    Theta_new = 2*Theta_n - np.pi - Theta
    sc = 1
    
    #ground
    if Z <= pil_height:
        #print(X,Y,Z)

        #what if there was no ground:
        X_nogr = X
        Y_nogr = Y
        Z_nogr = Z

	#what if there is a ground
        wall = 6
        #print('wall=6')
        X = x - ((pil_height-z)*(x-X))/(Z-z)
        Y = y - ((pil_height-z)*(y-Y))/(Z-z)
        Z = pil_height
        Hit_ground = [X, Y, Z]
        Theta_new = Theta
        phi_new = np.pi - phi
        
    if Z > 10:
        wall = 7
        X = x - z*(x-X)/(z-Z)
        Y = y - z*(y-Y)/(z-Z)
        Z = 0
        Theta_new = Theta
        phi_new = np.pi - phi
        
    HitPoint = [X,Y,Z]
    Hitpoint_nopil = [X_nopil,Y_nopil,Z_nopil]
    Hitpoint_nogr = [X_nogr,Y_nogr,Z_nogr]
    
    #for a ray that hits the pillar consider some specularity:
    s = 0 
        
    if 5<=wall<7:
        if np.random.random() < s: 
            sc = 0
            #print('specular reflection')
        else: 
            #diffuse reflection
            sc = 1
            #print('diffuse reflection')
            
            #choose random angles for reflection
            Theta2,phi2 = IF.get_random_direction_angles()
            
            #new normal direction
            if wall == 5:
                #print('diffuse wall 5')
                Z = [HitPoint[0],HitPoint[1],0.0] 
                X = [0,0,1]
                #print(normal(Z))
            else:
                Z = [0,0,1]
                X = [1,0,0]
                    
            Hitpoint_n = IF.normal(HitPoint)    
            Theta_new,phi_new = IF.rel_dir_cartesian(Z,X,Theta2,phi2)  
            #print(phi_new*180/np.pi)

    return([wall,d,v,HitPoint[0],HitPoint[1],HitPoint[2],Theta_new,phi_new,sc,Hit_pil[0],Hit_pil[1],Hit_pil[2],Hit_ground[0],Hit_ground[1],Hit_ground[2],Hitpoint_nopil[0], Hitpoint_nopil[1],Hitpoint_nopil[2],Hitpoint_nogr[0],Hitpoint_nogr[1],Hitpoint_nogr[2]]) 
   
