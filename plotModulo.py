import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from scipy.stats.kde import gaussian_kde

#Difesa da sx verso dx
x1, y1 = np.genfromtxt('terzinoSX.csv', delimiter=',', unpack=True)
x2, y2 = np.genfromtxt('centraleSX.csv', delimiter=',', unpack=True)
x3, y3 = np.genfromtxt('centraleDX.csv', delimiter=',', unpack=True)
x4, y4 = np.genfromtxt('terzinoDX.csv', delimiter=',', unpack=True)
difesaX, difesaY = np.genfromtxt('difesa.csv', delimiter=',', unpack=True)

#Centrocampo da sx verso dx
x11, y11 = np.genfromtxt('centrSX.csv', delimiter=',', unpack=True)
x22, y22 = np.genfromtxt('centrCC.csv', delimiter=',', unpack=True)
x33, y33 = np.genfromtxt('centrDX.csv', delimiter=',', unpack=True)

#attacco da sx verso dx
x111, y111 = np.genfromtxt('alaSX.csv', delimiter=',', unpack=True)
x222, y222 = np.genfromtxt('puntaCC.csv', delimiter=',', unpack=True)
x333, y333 = np.genfromtxt('alaDX.csv', delimiter=',', unpack=True)

#difesaY = difesaY[np.logical_not(np.isnan(difesaY))]
#difesaX = difesaX[np.logical_not(np.isnan(difesaX))]

y1 = y1[np.logical_not(np.isnan(y1))]
x1 = x1[np.logical_not(np.isnan(x1))]

y2 = y2[np.logical_not(np.isnan(y2))]
x2 = x2[np.logical_not(np.isnan(x2))]

y3 = y3[np.logical_not(np.isnan(y3))]
x3 = x3[np.logical_not(np.isnan(x3))]

y4 = y4[np.logical_not(np.isnan(y4))]
x4 = x4[np.logical_not(np.isnan(x4))]


y11 = y11[np.logical_not(np.isnan(y11))]
x11 = x11[np.logical_not(np.isnan(x11))]

y22 = y22[np.logical_not(np.isnan(y22))]
x22 = x22[np.logical_not(np.isnan(x22))]

y33 = y33[np.logical_not(np.isnan(y33))]
x33 = x33[np.logical_not(np.isnan(x33))]

y111 = y111[np.logical_not(np.isnan(y111))]
x111 = x111[np.logical_not(np.isnan(x111))]

y222 = y222[np.logical_not(np.isnan(y222))]
x222 = x222[np.logical_not(np.isnan(x222))]

y333 = y333[np.logical_not(np.isnan(y333))]
x333 = x333[np.logical_not(np.isnan(x333))]

xM1 = sum(x1)/len(x1)
yM1 = sum(y1)/len(y1)

xM2 = sum(x2)/len(x2)
yM2 = sum(y2)/len(y2)

xM3 = sum(x3)/len(x3)
yM3 = sum(y3)/len(y3)

xM4 = sum(x4)/len(x4)
yM4 = sum(y4)/len(y4)

xM11 = sum(x11)/len(x11)
yM11 = sum(y11)/len(y11)

xM22 = sum(x22)/len(x22)
yM22 = sum(y22)/len(y22)

xM33 = sum(x33)/len(x33)
yM33 = sum(y33)/len(y33)

xM111 = sum(x111)/len(x111)
yM111 = sum(y111)/len(y111)

xM222 = sum(x222)/len(x222)
yM222 = sum(y222)/len(y222)

xM333 = sum(x333)/len(x333)
yM333 = sum(y333)/len(y333)

#print(yM, xM)
#k = gaussian_kde(np.vstack([x, y]))
#xi, yi = np.mgrid[x.min():x.max():x.size**0.5*1j,y.min():y.max():y.size**0.5*1j]
#zi = k(np.vstack([xi.flatten(), yi.flatten()]))

#k = gaussian_kde(np.vstack([difesaX, difesaY]))
#xi, yi = np.mgrid[difesaX.min():difesaX.max():difesaX.size**0.5*1j,difesaY.min():difesaY.max():difesaY.size**0.5*1j]
#zi = k(np.vstack([xi.flatten(), yi.flatten()]))

fig = plt.figure(figsize=(12,6.5))
#ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(111)

#alpha=0.5 will make the plots semitransparent
#ax1.pcolormesh(yi, xi, zi.reshape(xi.shape), alpha=0.5)
#ax2.contourf(yi, xi, zi.reshape(xi.shape), alpha=0.3)

ax2.plot(yM1,xM1, "ro", markersize=10)
ax2.plot(yM2,xM2, "ro", markersize=10)
ax2.plot(yM3,xM3, "ro", markersize=10)
ax2.plot(yM4,xM4, "ro", markersize=10)
ax2.plot(yM11,xM11, "ro", markersize=10)
ax2.plot(yM22,xM22, "ro", markersize=10)
ax2.plot(yM33,xM33, "ro", markersize=10)
ax2.plot(yM111,xM111, "ro", markersize=10)
ax2.plot(yM222,xM222, "ro", markersize=10)
ax2.plot(yM333,xM333, "ro", markersize=10)

plt.axis('off')
plt.plot([yM1,yM2,yM3,yM4], [xM1, xM2, xM3, xM4], 'b', linewidth=3)
plt.plot([yM11,yM22,yM33], [xM11, xM22, xM33], 'b', linewidth=3)
plt.plot([yM111,yM222,yM333], [xM111, xM222, xM333], 'b', linewidth=3)
#ax1.set_xlim(0, 740)
#ax1.set_ylim(515, 0)
ax2.set_xlim(0, 740)
ax2.set_ylim(515, 0)

#overlay your soccer field
im = plt.imread('statszone_football_pitch.png')
#ax1.imshow(im, extent=[0, 740, 0, 515], aspect='auto')
ax2.imshow(im, extent=[0, 740, 0, 515], aspect='auto')

#plt.show()
#plt.savefig('heatmaps_tackles.png')

fig.savefig('realmadrid.png')