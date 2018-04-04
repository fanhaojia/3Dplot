from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import *
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from scipy import interpolate
#import matplotlib as mpl
#from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import curve_fit
import pylab as pl
import matplotlib as mpl

fig = plt.figure()
ax = Axes3D(fig)
V=[61.37999491675, 62.329170095875, 63.278345275, 63.5434893626, 64.227520454125, 65.17669563324999]
ca=[1.02,1.03333333,1.04666667,1.06,1.07333333,1.08666667,1.1,1.11333333,1.12666667,1.14]
ca,V = np.meshgrid(ca,V)
ca=list(ca)
V=list(V)
Z = [[0.01669509,0.01553133,0.01712337,0.0214712,0.02857482,0.03843422,0.05104942,0.06642041,0.08454719,0.10542976],
     [0.01184899,0.00654394,0.00400759,0.00423992 ,0.00724095,0.01301068,0.02154909,0.0328562,0.04693199,0.06377648],
     [0.0211528,0.01155235,0.00486736,0.00109783,0.00024376,0.00230516,0.00728201,0.01517433,0.02598211,0.03970534],
     [2.52796609e-02,1.45870689e-02,6.81583799e-03,1.96596807e-03,3.74591526e-05,1.03031126e-03,4.94452437e-03,1.17800985e-02,2.15370337e-02,3.42153298e-02],
     [0.04109418,0.02726091,0.0162875,0.00817394,0.00292022,0.00052637,0.00099236,0.00431821,0.01050391,0.01954946],
     [0.06585029,0.04891589,0.03477492,0.02342738,0.01487327,0.00911259,0.00614534,0.00597152,0.00859114,0.01400418]]
#Zmin=-153.7631405348
#for i in range(6):
#    for j in range(8):
#        Z[i][j]=Z[i][j]-Zmin
#print Z
newfunc=interpolate.interp2d(V,ca,Z)

Vnew=np.linspace(61.37999491675,65.17669563324999,150)
canew=np.linspace(1.01,1.15,150)

fnew=newfunc(Vnew,canew)
canew,Vnew = np.meshgrid(canew,Vnew)
#ax.plot_surface(V, ca, Z)
#plot2=plt.plot(63.52,1.075,0.11, 'o',color='black',markersize=9)
surf=ax.plot_surface(Vnew, canew, fnew, rstride=1, cstride=1, cmap='rainbow')

ax.contourf(Vnew,canew,fnew,zdir='z',offset=0.11,cmap=plt.get_cmap('rainbow'))

ax.xaxis.set_major_locator(LinearLocator(6))
#ax.yaxis.set_major_locator(LinearLocator(5))
ax.zaxis.set_major_locator(LinearLocator(5))
ax.xaxis.set_major_formatter(FormatStrFormatter('%.00f'))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.02f'))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
for t in ax.zaxis.get_major_ticks(): t.label.set_fontsize(30)
#plt.xlim(60.8,65.5)
plt.ylim(1.01,1.15,5)
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
#ax.set_yticks(np.linspace(1.008,1.165,5))
#ax.set_yticklabels(('1.01','1.04','1.07','1.10','1.13','1.16',''))
#plt.zticks(fontsize=12)

cb =fig.colorbar(surf,shrink=0.5,aspect=6)
font_size = 30 # Adjust as appropriate.
cb.ax.tick_params(labelsize=font_size)
ax.set_xlabel('Volume ($\AA^3$)',labelpad=30,fontsize=30)
ax.set_ylabel('c/a Ratio',labelpad=30,fontsize=30)
ax.set_zlabel('Energy(eV/f.u.)',labelpad=30,fontsize=30)
fig=plt.gcf()
fig.subplots_adjust(top=0.95,bottom=0.16,left=0.2,right=0.94,hspace=0.1,wspace=0.1)
plt.savefig('3D.png',dpi=300)
plt.show()
