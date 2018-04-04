from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import *
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from scipy import interpolate
import pylab as pl
import matplotlib as mpl

fig = plt.figure()
ax = Axes3D(fig)
ca=[1.02,1.04,1.06,1.07,1.08,1.10,1.12,1.14]
V=[61.37999491675, 62.329170095875, 63.278345275, 63.5434893626, 64.227520454125, 65.17669563324999]
ca,V = np.meshgrid(ca,V)
ca=list(ca)
V=list(V)
Z = [[-153.7438036839,-153.7463993485,-153.7397761279,-153.7363319503,-153.7282616690,-153.7086889489,-153.6856172141,-153.6569002150],
     [-153.7496508953,-153.7553485455,-153.7583086268,-153.7560137061,-153.7509710503,-153.7411647437,-153.7187757386,-153.6991110974],
     [-153.7373359076,-153.7580304885,-153.7631405348,-153.7601637821,-153.7556147885,-153.7554612904,-153.7406880895,-153.7224213790],
     [-153.7306601740,-153.7593546128,-153.7612599860,-153.7621994685,-153.7566897112,-153.7537812178,-153.7445710482,-153.7292819694],
     [-153.7202378668,-153.7370461752,-153.7588332590,-153.7571902469,-153.7600853581,-153.7583062795,-153.7520615890,-153.7438754405],
     [-153.6941617430,-153.7189539881,-153.7410703175,-153.7487153484,-153.7487615580,-153.7524184177,-153.7497272664,-153.7511895821]]
Zmin=-153.7631405348
for i in range(6):
    for j in range(8):
        Z[i][j]=Z[i][j]-Zmin
#print Z
newfunc=interpolate.interp2d(V,ca,Z)

Vnew=np.linspace(61.37999491675,65.17669563324999,200)
canew=np.linspace(1.02,1.14,200)

fnew=newfunc(Vnew,canew)
canew,Vnew = np.meshgrid(canew,Vnew)
#ax.plot_surface(V, ca, Z)

surf=ax.plot_surface(Vnew, canew, fnew, rstride=1, cstride=1, cmap='rainbow')
ax.contourf(Vnew,canew,fnew,zdir='z',offset=0.11, cmap=plt.get_cmap('rainbow'))
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf,shrink=0.5, aspect=6)
ax.set_xlabel('Volume ($\AA^3$)',fontsize=18)
ax.set_ylabel('c/a Ratio',fontsize=18)
ax.set_zlabel('Energy(eV/f.u.)',fontsize=18)
fig=plt.gcf()
fig.subplots_adjust(top=0.95,bottom=0.14,left=0.2,right=0.94,hspace=0.1,wspace=0.1)
plt.savefig('3D.png',dpi=300)
plt.show()
