from math import *
import cgi
import cgitb; cgitb.enable()
import matplotlib
matplotlib.use( 'Agg' )
import numpy as np
from scipy.stats.kde import gaussian_kde
import os,sys
import pylab
import PIL
from PIL import Image


def resize(arg1):
    baseheight = 321
    img = Image.open(arg1)
    hpercent = (baseheight / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))
    img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
    img.save(arg1)

def make_fig():

	global filename1,filename2,filename3
	filename1 = sys.argv[1]
	filename2 = sys.argv[2]
	filename3 = sys.argv[3]
	x2, y2 = np.genfromtxt(filename1, delimiter=',', unpack=True)
	x3, y3 = np.genfromtxt(filename2, delimiter=',', unpack=True)

	x4, y4 = np.genfromtxt(filename3, delimiter=',', unpack=True)


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

	#print(xMM,yMM)
	#print(distance)

	fig = pylab.figure(figsize=(7,4))
	ax2 = fig.add_subplot(111)

	groups = 11
	index = np.arange(groups)

	width = 0.8
	#ax2.bar(distanze, , width=100)
	pylab.ylim([0,100])
	rects1 = ax2.bar(partiteIndici, distanze, width,align='center', color='blue')
	pylab.xticks(index + 1, partite, fontsize = 8)
	pylab.legend()
	pylab.tight_layout()
	#pylab.show()
	global name

	if(os.path.isfile('barplot_distanzeDIFATT.png')):
		fig.savefig('barplot_distanzeDIFATT1.png')
		name = 'barplot_distanzeDIFATT1.png'
	else:
		fig.savefig('barplot_distanzeDIFATT.png')
		name = 'barplot_distanzeDIFATT.png'
	print(name)
make_fig()
resize(name)
