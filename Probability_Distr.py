#!/usr/bin/python2.7

import numpy as np
import get_Hitpoints as Hit
import matplotlib.pyplot as plt
from get_Hitpoints import GetHits

N = 100000
pil_h = -50
Lambda = 10**8
R = 7.5
L = 14.14


Z_pil_all,Th_pil_all,X_gr_all,Y_gr_all,Z_gr_all,All_Points,Hitpoints_pil,Hitpoints_gr,Points_nopilConf, Points_nogrConf, hitpoints_imtop = GetHits(N,pil_h,Lambda,L,R)

#Gaussian: 

def G(X,Y,i,j,wx,wy):
    A= 1/(2*np.pi*(wx*wy))
    B= (X-i)/wx
    F= (Y-j)/wy
    J = B**2+F**2
    C= A*np.exp(-J/2)
    return C

#test Gaussian:
xo = np.linspace(-np.pi,np.pi,100)
yo = np.linspace(-1,0,100)
xg, yg = np.meshgrid(xo,yo) 
z = G(xg,yg,0.0,0.0,0.2,0.2)
#print(z)
plt.pcolormesh(z)
plt.show()

#probability distribution:

def P3d (x,y,xo,yo,wx,wy):
   
    X,Y = xo, yo
    S=np.zeros(np.shape(X))
    N=len(x)  
    n=0
    
    while n<N:
        i=x[n]
        j=y[n]
        S += G(X,Y,i,j,wx,wy)
        n+=1
    return S/N


xd = Th_pil_all
yd = Z_pil_all
#xd = Th_h_all


xd = np.concatenate((Th_pil_all,0.5*np.pi-Th_pil_all))
xd = np.concatenate((xd-np.pi*0.5,xd,xd+np.pi*0.5,xd+np.pi,xd+np.pi*1.5,xd+np.pi*2))
print(len(xd))
yd = np.concatenate((Z_pil_all,Z_pil_all))
yd = np.concatenate((yd,yd,yd,yd,yd,yd))
#yd = np.concatenate(Z_pil_all,Z_pil_all,Z_pil_all,Z_pil_all)

#xd = x_gr
#yd = y_gr
yo_min = min(yd)

nmap=100
nmap2 = 150

xo = np.linspace(0,2*np.pi,nmap)
yo = np.linspace(-100,0,nmap)
xo2 = np.linspace(0,2*np.pi,nmap2)
yo2 = np.linspace(-100,0,nmap2)
#xo = np.linspace(0,20,nmap2)
#yo = np.linspace(0,L,nmap)
xg, yg = np.meshgrid(xo,yo)
xg2, yg2 = np.meshgrid(xo2,yo2)

print('xd',np.shape(xd))
print('yd',np.shape(yd))
print('xg',np.shape(xg))

p1 = P3d(xd,yd,xg,yg,np.pi*2/50.0,abs(pil_h)/50.0)
p2 = P3d(xd,yd,xg,yg,np.pi*2/100.0,abs(pil_h)/100.0)
p3 = P3d(xd,yd,xg2,yg2,np.pi*2/50.0,abs(pil_h)/50.0)
p4 = P3d(xd,yd,xg2,yg2,np.pi*2/100.0,abs(pil_h)/100.0)

#p = P3d(xd,yd,xg,yg,1,1)
#p = P3d(xd,yd,xg,yg,abs(pil_h)/100.0,abs(pil_h)/100.0)
#print('p',np.shape(p))


#fig2 = plt.figure()
#ax2 = fig2.add_subplot(1, 1, 1)

l = len(p1)

keep=0
for j in yd:
    if j>yo_min:
        keep+=1

print('keep',keep)

string="R= "+str(R)
#ax2.plot(yo,p.mean(1))
#ax2.plot(yo,p1.mean(1),'r',yo,p2.mean(1),'g',yo2,p3.mean(1),'b',yo2,p4.mean(1),'k')
#ax2.set_ylabel('mean probability distribution',fontsize=16)
#ax2.set_xlabel('Z ($\mu$m)',fontsize=16)
#ax2.tick_params(direction='in')
#plt.tick_params(labelsize=14)

#fig2.savefig('/Users/pmira002/Desktop/Projects/Ray_Trace/Pil_height_data/Distr_HitPoints/pil_height_50/R5/S0Ref0/_Figures/meanP3D-pillar-wx.02pi-wy.5.jpg',dpi=200,bbox_inches='tight')

fig3=plt.figure()
ax3 = fig3.add_subplot(1, 1, 1)
ax3.pcolormesh(p1)
#plt.yticks(np.arange(yo_min, 0, 10)) 
plt.show()
#fig3.savefig('/Users/pmira002/Desktop/Projects/Ray_Trace/Pil_height_data/Distr_HitPoints/pil_height_50/R5/S0Ref0/_Figures/colormap-pillar-wx.02pi-wy.5.jpg', dpi=200)
#np.savetxt("/Users/pmira002/Desktop/Projects/Ray_Trace/Pil_height_data/Distr_HitPoints/pil_height_50/R5/S0Ref0/P3D-pillar-wx.02piwy.5.txt", Points_nogrConf)
np.savetxt("/Users/pmira002/Desktop/Projects/Ray_Trace/Pil_height_data/Pil_height_data/Duncan_sys/P3D-h50-S0Ref0.txt", p1)


