#!/usr/bin/python2.7

import numpy as np
import RayTrace as RT

def GetHits(N,pil_h,Lambda,L,R):

    Pp,Pg,Pw,Pt,Pl,hitpoint,hitpoint_p,hitpoint_gr,hitpoint_nopil,hitpoint_nogr,points_top,hitangle,hitangle_p,hitangle_gr,hitangle_nopil,hitangle_nogr,angles_top,diffuse,specular = RT.Ray_Trace(N,pil_h,Lambda,L,R)

    print("absorbed by pillar",Pp)
    print("absorbed by ground",Pg)
    print("absorbed by water", Pw)
    print("left from the top",Pt)
    print("lost after runs",Pl)
    #print("min hitpoint z",min(hitpoint[2]))

    #making arrays of hitpoints and hitangles for plotting 
    Hitpoint = np.array(hitpoint)
    Hitangle = np.array(hitangle)
    Hitpoint_pil = np.array(hitpoint_p)
    Hitangle_pil = np.array(hitangle_p)
    Hitpoint_gr = np.array(hitpoint_gr)
    Hitangle_gr = np.array(hitangle_gr)
    Hitpoint_nopil = np.array(hitpoint_nopil)
    Hitangle_nopil = np.array(hitangle_nopil)
    Hitpoint_nogr = np.array(hitpoint_nogr)
    Hitangle_nogr = np.array(hitangle_nogr)
    Points_imtop = np.array(points_top)
    angles_imtop = np.array(angles_top)

    #theta angles:
    Th_h= Hitangle[:,0]
    th_pil = Hitangle_pil[:,0]
    th_gr = Hitangle_gr[:,0]
    th_h_nopil = Hitangle_nopil[:,0]
    th_h_nogr = Hitangle_nogr[:,0]
    th_imtop = angles_imtop[:,0]
    Phi = Hitangle[:,1]  

    print("Hitpoint_pil",len(Hitpoint_pil))
    print("Hitpoint_gr",len(Hitpoint_gr))
    print("Hitpoint_nogr",len(Hitpoint_nogr))
    print("Hitpoint_nopil",len(Hitpoint_nopil))

    #pillar and ground hit points:
    x_h =Hitpoint[:,0]
    y_h =Hitpoint[:,1]
    z_h =Hitpoint[:,2]

    #only pillar
    x_pil = Hitpoint_pil[:,0]
    y_pil = Hitpoint_pil[:,1]
    z_pil = Hitpoint_pil[:,2]

    #only ground
    x_gr = Hitpoint_gr[:,0]
    y_gr = Hitpoint_gr[:,1]
    z_gr = Hitpoint_gr[:,2]

    #points between real surface and imaginary top:
    xt = Points_imtop[:,0]
    yt = Points_imtop[:,1]
    zt = Points_imtop[:,2]

    #hitpoints between real surface and imaginary top (confined to pillar's surface):
    xt_hit = []
    yt_hit = []
    zt_hit = []
    hitpoints_imtop = []
    Thetahit_imtop = []

    for i in range(0,len(xt)):
        if np.sqrt(xt[i]**2+yt[i]**2) == R:
            xt_hit.append(xt[i])
            yt_hit.append(yt[i])
            zt_hit.append(zt[i])
            nosurf = [[xt[i],yt[i],zt[i]]]
            hitpoints_imtop.append(nosurf)
            Thetahit_imtop.append(th_imtop[i])

    #if there was no pillar
    x_h_nopil = Hitpoint_nopil[:,0]
    y_h_nopil = Hitpoint_nopil[:,1]
    z_h_nopil = Hitpoint_nopil[:,2]

    #confine no pillar to inside the pillar:
    x_h_nopil_Conf = []
    y_h_nopil_Conf = []
    z_h_nopil_Conf = []
    Points_nopilConf = []
    Theta_nopil = []
    #R = 5

    for i in range(0,len(x_h_nopil)): 
        if np.sqrt(x_h_nopil[i]**2+y_h_nopil[i]**2) <= R:
            #print(i)
            x_h_nopil_Conf.append(x_h_nopil[i])
            y_h_nopil_Conf.append(y_h_nopil[i])
            z_h_nopil_Conf.append(z_h_nopil[i])
            nopil = [x_h_nopil[i],y_h_nopil[i],z_h_nopil[i]]
            Points_nopilConf.append(nopil)
            Thetanopil = th_h_nopil[i]
            #print(Thetanopil)
            Theta_nopil.append(Thetanopil)
        
    #print(Points_nopilConf[1])
    #print(x_h_nopil_Conf[1],y_h_nopil_Conf[1],z_h_nopil_Conf[1])

    #if there was no ground
    x_h_nogr = Hitpoint_nogr[:,0]
    y_h_nogr = Hitpoint_nogr[:,1]
    z_h_nogr = Hitpoint_nogr[:,2]

    #confine no ground to the pillar p:
    x_h_nogr_Conf = []
    y_h_nogr_Conf = []
    z_h_nogr_Conf = []
    Points_nogrConf = []
    Theta_nogr = []
    #R = 5

    for m in range(0,len(x_h_nogr)):
        if np.sqrt(x_h_nogr[m]**2+y_h_nogr[m]**2)==R:
            x_h_nogr_Conf.append(x_h_nogr[m])
            y_h_nogr_Conf.append(y_h_nogr[m])
            z_h_nogr_Conf.append(z_h_nogr[m])
            nogr = [x_h_nogr[m],y_h_nogr[m],z_h_nogr[m]]
            Points_nogrConf.append(nogr)
            Thetanogr = th_h_nogr[m]
            Theta_nogr.append(Thetanogr)
        
    #all hitpoints: 
    x = [x_pil,x_gr,x_h_nopil_Conf,x_h_nogr_Conf,xt_hit]
    X_all=np.concatenate(x,axis=0)
    y = [y_pil,y_gr,y_h_nopil_Conf,y_h_nogr_Conf,yt_hit]
    Y_all=np.concatenate(y,axis=0)
    z = [z_pil,z_gr,z_h_nopil_Conf,z_h_nogr_Conf,zt_hit]
    Z_all=np.concatenate(z,axis=0)

    th_h_all = [Th_h,Theta_nopil,Theta_nogr,Thetahit_imtop]
    Theta_all = np.concatenate(th_h_all,axis=0)

    All_Points = []
    for x in range(0,len(X_all)):
        point = [X_all[x],Y_all[x],Z_all[x]]
        All_Points.append(point)

    #all rays hitting pillar:
    Z_pil = [z_pil,z_h_nogr_Conf,zt_hit] #real and imaginary points
    Z_pil_all = np.concatenate(Z_pil,axis=0)
    Th_pil = [th_pil,Theta_nogr,Thetahit_imtop]
    Th_pil_all = np.concatenate(Th_pil,axis=0)
    print(len(Th_pil_all))

    #all rays hitting the ground:
    X_gr = [x_gr,x_h_nopil_Conf]
    X_gr_all = np.concatenate(X_gr,axis=0)
    Y_gr = [y_gr,y_h_nopil_Conf]
    Y_gr_all = np.concatenate(Y_gr,axis=0)
    Z_gr = [z_gr,z_h_nopil_Conf]
    Z_gr_all = np.concatenate(Z_gr,axis=0)
    print(len(Z_gr_all))
    
    print("Hitpoint_pil",len(Hitpoint_pil))
    print("Hitpoint_gr",len(Hitpoint_gr))
    print("Hitpoint_nogr_Conf",len(Points_nogrConf))
    print("Hitpoint_nopil_Conf",len(Points_nopilConf))
    print("Hitpoint_imtop",len(hitpoints_imtop))

    return Hitpoint,Th_h,Z_pil_all,Th_pil_all,X_gr_all,Y_gr_all,Z_gr_all,All_Points,Hitpoint_pil,Hitpoint_gr,Points_nopilConf, Points_nogrConf,hitpoints_imtop 

#save output txt
#np.savetxt("/Users/pmira002/Desktop/Projects/Ray_Trace/Pil_height_data/Distr_HitPoints/pil_height_100/R5/S0Ref0.2/All_points.txt", All_Points)
#np.savetxt("/Users/pmira002/Desktop/Projects/Ray_Trace/Pil_height_data/Distr_HitPoints/pil_height_100/R5/S0Ref0.2/Hitpoints_pil.txt", Hitangle_pil)
#np.savetxt("/Users/pmira002/Desktop/Projects/Ray_Trace/Pil_height_data/Distr_HitPoints/pil_height_100/R5/S0Ref0.2/Hitpoints_gr.txt", Hitpoint_gr)
#np.savetxt("/Users/pmira002/Desktop/Projects/Ray_Trace/Pil_height_data/Distr_HitPoints/pil_height_100/R5/S0Ref0.2/Points_nopil_Conf.txt", Points_nopilConf)
#np.savetxt("/Users/pmira002/Desktop/Projects/Ray_Trace/Pil_height_data/Distr_HitPoints/pil_height_100/R5/S0Ref0.2/Points_nogr_Conf.txt", Points_nogrConf)
