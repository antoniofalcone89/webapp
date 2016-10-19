import cgi
import cgitb; cgitb.enable()
import matplotlib
matplotlib.use( 'Agg' )
import numpy as np
from scipy.stats.kde import gaussian_kde
import os,sys
import pylab
from PIL import Image
import uuid

def crop(arg1):
    # size is width/height
    img = Image.open(arg1)
    left = 88
    top = 41
    width = 545
    height = 321
    box = (left, top, left+width, top+height)
    #area = img.crop(box)

    #area.save('cropped_0_388_image1', 'jpeg')
    output_img = img.crop(box)
    output_img.save(arg1, 'png')

def make_fig():
    global folder
    folder  = "433files/"
    global imgFolder
    imgFolder = "imgGen/"
    global filename
    global filename1,filename2,filename3,filename4,filename5,filename6,filename7,filename8,filename9,filename10
    filename1 = folder + sys.argv[1]
    filename2 = folder + sys.argv[2]
    filename3 = folder + sys.argv[3]
    filename4 = folder + sys.argv[4]
    filename5 = folder + sys.argv[5]
    filename6 = folder + sys.argv[6]
    filename7 = folder + sys.argv[7]
    filename8 = folder + sys.argv[8]
    filename9 = folder + sys.argv[9]
    filename10 = folder + sys.argv[10]

    #Squadra
    x1, y1 = np.genfromtxt(filename1, delimiter=',', unpack=True)
    x2, y2 = np.genfromtxt(filename2, delimiter=',', unpack=True)
    x3, y3 = np.genfromtxt(filename3, delimiter=',', unpack=True)
    x4, y4 = np.genfromtxt(filename4, delimiter=',', unpack=True)
    x11, y11 = np.genfromtxt(filename5, delimiter=',', unpack=True)
    x22, y22 = np.genfromtxt(filename6, delimiter=',', unpack=True)
    x33, y33 = np.genfromtxt(filename7, delimiter=',', unpack=True)
    x111, y111 = np.genfromtxt(filename8, delimiter=',', unpack=True)
    x222, y222 = np.genfromtxt(filename9, delimiter=',', unpack=True)
    x333, y333 = np.genfromtxt(filename10, delimiter=',', unpack=True)

    #Difesa da sx verso dx
    # x1, y1 = np.genfromtxt('terzinoSX.csv', delimiter=',', unpack=True)
    # x2, y2 = np.genfromtxt('centraleSX.csv', delimiter=',', unpack=True)
    # x3, y3 = np.genfromtxt('centraleDX.csv', delimiter=',', unpack=True)
    # x4, y4 = np.genfromtxt('terzinoDX.csv', delimiter=',', unpack=True)

    #Centrocampo da sx verso dx
    # x11, y11 = np.genfromtxt('centrSX.csv', delimiter=',', unpack=True)
    # x22, y22 = np.genfromtxt('centrCC.csv', delimiter=',', unpack=True)
    # x33, y33 = np.genfromtxt('centrDX.csv', delimiter=',', unpack=True)

    #attacco da sx verso dx
    # x111, y111 = np.genfromtxt('alaSX.csv', delimiter=',', unpack=True)
    # x222, y222 = np.genfromtxt('puntaCC.csv', delimiter=',', unpack=True)
    # x333, y333 = np.genfromtxt('alaDX.csv', delimiter=',', unpack=True)




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


    fig = pylab.figure(figsize=(7,4), frameon=False)
    #ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(111)

    #alpha=0.5 will make the plots semitransparent
    #ax1.pcolormesh(yi, xi, zi.reshape(xi.shape), alpha=0.5)
    #ax2.contourf(yi, xi, zi.reshape(xi.shape), alpha=0.3)

    #PUNTI ROSSI CHE INDICANO LA POSIZIONE DEI GIOCATORI
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

    pylab.axis('off')

    #LINEE DI COLLEGAMENTO TRA I GIOCATORI DEI REPARTI

    pylab.plot([yM1,yM2,yM3,yM4], [xM1, xM2, xM3, xM4], 'b', linewidth=3)
    pylab.plot([yM11,yM22,yM33], [xM11, xM22, xM33], 'b', linewidth=3)
    pylab.plot([yM111,yM222,yM333], [xM111, xM222, xM333], 'b', linewidth=3)
    #ax1.set_xlim(0, 740)
    #ax1.set_ylim(515, 0)

    ax2.set_xlim(0, 740)
    ax2.set_ylim(515, 0)

    #overlay your soccer field
    im = pylab.imread('statszone_football_pitch.png')
    #ax1.imshow(im, extent=[0, 740, 0, 515], aspect='auto')
    ax2.imshow(im, extent=[0, 740, 0, 515], aspect='auto')
    global unique_filename
    unique_filename = str(uuid.uuid4())

    #plt.show()
    #plt.savefig('heatmaps_tackles.png')
    # if(os.path.isfile('disposizione.png')):
    #     filename = 'disposizione1.png'
    # else:
    #     filename = 'disposizione.png'

    fig.savefig(imgFolder+unique_filename+".png")
    print(unique_filename+".png")
make_fig()
crop(imgFolder+unique_filename+".png")
