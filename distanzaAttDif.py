import matplotlib.pyplot as plt
import matplotlib
from math import *
import numpy as np

x2, y2 = np.genfromtxt('centraleSX.csv', delimiter=',', unpack=True)
x3, y3 = np.genfromtxt('centraleDX.csv', delimiter=',', unpack=True)

x4, y4 = np.genfromtxt('puntaCC.csv', delimiter=',', unpack=True)


y2 = y2[np.logical_not(np.isnan(y2))]
x2 = x2[np.logical_not(np.isnan(x2))]

y3 = y3[np.logical_not(np.isnan(y3))]
x3 = x3[np.logical_not(np.isnan(x3))]

y4 = y4[np.logical_not(np.isnan(y4))]
x4 = x4[np.logical_not(np.isnan(x4))]


#print(len(x2), len(x3))

puntoMedioDifX = []
puntoMedioDifY = []

for i in range(len(x2)):
	j = (x2[i] + x3[i])/2
	puntoMedioDifX.append(j)
	k = (y2[i] + y3[i])/2
	puntoMedioDifY.append(k)

#### punto medio tra i due centrali ####
#xM2 = sum(x2)/len(x2)
#yM2 = sum(y2)/len(y2)

#xM3 = sum(x3)/len(x3)
#yM3 = sum(y3)/len(y3)

#xMM = (xM2 + xM3)/2
#yMM = (yM2 + yM3)/2

#### posizione media punta centr ####
#xMP = sum(x4)/len(x4)
#yMP = sum(y4)/len(y4)

### distanza tra dif centrale e punta ###

distanze = []
for l in range(len(x4)):
	#distance =sqrt(pow((x4[l]*(125./740) - xMM*(125./740)), 2) + pow((y4[l]*(86./515) - yMM*(86./515)), 2))
	distance =sqrt(pow((x4[l]*(125./740) - puntoMedioDifX[l]*(125./740)), 2) + pow((y4[l]*(86./515) - puntoMedioDifY[l]*(86./515)), 2))
	distance = round(distance,2)
	distanze.append(distance)
	#print(distance)
	
partite = []
partiteIndici = [1,2,3,4,5,6,7,8,9,10,11]
for z in range(len(distanze)):
	n = "match " + str(z + 1)
	partite.append(n)

distanze2=[21, 35, 30, 40, 25, 43, 33, 28, 40, 30, 38]
#print(xMM,yMM)
#print(distance)

fig = plt.figure(figsize=(12,6.5))
ax2 = fig.add_subplot(111)

groups = 11
index = np.arange(groups)

width = 0.8   
#ax2.bar(distanze, , width=100)
plt.ylim([0,100])
rects1 = ax2.bar(partiteIndici, distanze, width,align='center', color='blue', label='4-3-3 Modello')
#rects2 = ax2.bar(partiteIndici, distanze2, width,align='center', color='red', label='Squadra X')
plt.xticks(index + 1, partite)
plt.legend()
plt.tight_layout()
plt.show()

#ax2.plot(yMM,xMM, "ro")
#ax2.plot(yMP, xMP, "ro")


#ax2.set_xlim(0, 740)
#ax2.set_ylim(515, 0)

#overlay your soccer field
#im = plt.imread('statszone_football_pitch.png')
#ax1.imshow(im, extent=[0, 740, 0, 515], aspect='auto')
#ax2.imshow(im, extent=[0, 740, 0, 515], aspect='auto')

#plt.show()
fig.savefig('barplot_distanzeDIFATT.png')

#fig.savefig('difCentrali.png')