#visualize the hit points(x_h,y_h,z_h) in 3D:

#!/usr/bin/python2.7

# import libraries

import numpy as np
from get_Hitpoints import GetHits
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


#input values

N = 30000
pil_h = -50
Lambda = 10**8
R = 7.5
L = 14.14

realhits,theta,Z_pil_all,Th_pil_all,X_gr_all,Y_gr_all,Z_gr_all,All_Points,Hitpoint_pil,Hitpoint_gr,Points_nopilConf,Points_nogrConf,Points_noSurf_Conf = GetHits(N,pil_h,Lambda,L,R)


#visualize the hit points(x_h,y_h,z_h) in 3D:

fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection='3d')

#Points = np.array(realhits)
#print(np.shape(realhits))

#Xq = []
#Yq = []
#Zq = []

#for q in range(0,len(realhits)):
    #xq = Points[q,0]
    #Xq.append(xq)
    #yq = Points[q,1]
    #Yq.append(yq)
    #Zq.append(Points[q,2])


#x = np.array(Xq)
#y = np.array(Yq)
#z = np.array(Zq)

x = realhits[:,0]
y = realhits[:,1]
z = realhits[:,2]

ax1.scatter3D(x, y, z, c='r', marker='.')
ax1.scatter3D(x, -y, z, c='r', marker='.')
ax1.scatter3D(-x, y, z, c='r', marker='.')
ax1.scatter3D(-x, -y, z, c='r', marker='.')


ax1.set_ylim(-L,L)
ax1.set_xlim(-L,L)
ax1.set_zlim(min(z)-pil_h,max(z))
plt.title('original hitpoints',fontsize=18)
plt.tick_params(direction='in')

print(np.min(z))

ax1.set_xlabel('X',fontsize=16)
ax1.set_ylabel('Y',fontsize=16)
ax1.set_zlabel('Z',fontsize=16)
#ax1.set_xticks(ticks=np.arange(-20,20,10))
#ax1.set_yticks(ticks=np.arange(-20,20,10))
#ax1.set_zticks(ticks=np.arange(-2000,1,500))

plt.show()


