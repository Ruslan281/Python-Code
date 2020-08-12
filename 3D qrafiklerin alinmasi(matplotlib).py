import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

fiqur=plt.figure()
ax=plt.axes(projection="3d") # 3d Proykte cviririk

x=[1,2,3,4,5,6,7,8,9] # mustevi uzerinde x-in qiymetlerini daxil edirik
y=[2,3,4,6,7,8,9,3,1]  # mustevi uzerinde y-in qiymetlerini daxil edirik
z=[5,4,6,7,8,9,3,2,4]  # mustevi uzerinde z-in qiymetlerini daxil edirik

ax.scatter(x,y,z,color="red") # Noqtevari gorunusleri qirmizi rengle daxil edirik
ax.set_xlabel("X Koordinanti") 
ax.set_ylabel("Y Koordinanti")
ax.set_zlabel("Z_Koordinanti")
# X,Y,Z in yazilarini yaziriq
plt.show()
#programi islek veziyyete getiririk
