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
import scipy.stats as stats

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
    x5, y5 = np.genfromtxt(filename5, delimiter=',', unpack=True)
    x6, y6 = np.genfromtxt(filename6, delimiter=',', unpack=True)
    x7, y7 = np.genfromtxt(filename7, delimiter=',', unpack=True)
    x8, y8 = np.genfromtxt(filename8, delimiter=',', unpack=True)
    x9, y9 = np.genfromtxt(filename9, delimiter=',', unpack=True)
    x10, y10 = np.genfromtxt(filename10, delimiter=',', unpack=True)

    y1 = y1[np.logical_not(np.isnan(y1))]
    x1 = x1[np.logical_not(np.isnan(x1))]
    k1 = gaussian_kde(np.vstack([x1, y1]))
    xi1, yi1 = np.mgrid[x1.min():x1.max():x1.size**0.5*1j,y1.min():y1.max():y1.size**0.5*1j]
    zi1 = k1(np.vstack([xi1.flatten(), yi1.flatten()]))

    y2 = y2[np.logical_not(np.isnan(y2))]
    x2 = x2[np.logical_not(np.isnan(x2))]
    k2 = gaussian_kde(np.vstack([x2, y2]))
    xi2, yi2 = np.mgrid[x2.min():x2.max():x2.size**0.5*1j,y2.min():y2.max():y2.size**0.5*1j]
    zi2 = k2(np.vstack([xi2.flatten(), yi2.flatten()]))

    y3 = y3[np.logical_not(np.isnan(y3))]
    x3 = x3[np.logical_not(np.isnan(x3))]
    k3 = gaussian_kde(np.vstack([x3, y3]))
    xi3, yi3 = np.mgrid[x3.min():x3.max():x3.size**0.5*1j,y3.min():y3.max():y3.size**0.5*1j]
    zi3 = k3(np.vstack([xi3.flatten(), yi3.flatten()]))

    y4 = y4[np.logical_not(np.isnan(y4))]
    x4 = x4[np.logical_not(np.isnan(x4))]
    k4 = gaussian_kde(np.vstack([x4, y4]))
    xi4, yi4 = np.mgrid[x4.min():x4.max():x4.size**0.5*1j,y4.min():y4.max():y4.size**0.5*1j]
    zi4 = k4(np.vstack([xi4.flatten(), yi4.flatten()]))

    y5 = y5[np.logical_not(np.isnan(y5))]
    x5 = x5[np.logical_not(np.isnan(x5))]
    k5 = gaussian_kde(np.vstack([x5, y5]))
    xi5, yi5 = np.mgrid[x5.min():x5.max():x5.size**0.5*1j,y5.min():y5.max():y5.size**0.5*1j]
    zi5 = k5(np.vstack([xi5.flatten(), yi5.flatten()]))

    y6 = y6[np.logical_not(np.isnan(y6))]
    x6 = x6[np.logical_not(np.isnan(x6))]
    k6 = gaussian_kde(np.vstack([x6, y6]))
    xi6, yi6 = np.mgrid[x6.min():x6.max():x6.size**0.5*1j,y6.min():y6.max():y6.size**0.5*1j]
    zi6 = k6(np.vstack([xi6.flatten(), yi6.flatten()]))

    y7 = y7[np.logical_not(np.isnan(y7))]
    x7 = x7[np.logical_not(np.isnan(x7))]
    k7 = gaussian_kde(np.vstack([x7, y7]))
    xi7, yi7 = np.mgrid[x7.min():x7.max():x7.size**0.5*1j,y7.min():y7.max():y7.size**0.5*1j]
    zi7 = k7(np.vstack([xi7.flatten(), yi7.flatten()]))

    y8 = y8[np.logical_not(np.isnan(y8))]
    x8 = x8[np.logical_not(np.isnan(x8))]
    k8 = gaussian_kde(np.vstack([x8, y8]))
    xi8, yi8 = np.mgrid[x8.min():x8.max():x8.size**0.5*1j,y8.min():y8.max():y8.size**0.5*1j]
    zi8 = k8(np.vstack([xi8.flatten(), yi8.flatten()]))

    y9 = y9[np.logical_not(np.isnan(y9))]
    x9 = x9[np.logical_not(np.isnan(x9))]
    k9 = gaussian_kde(np.vstack([x9, y9]))
    xi9, yi9 = np.mgrid[x9.min():x9.max():x9.size**0.5*1j,y9.min():y9.max():y9.size**0.5*1j]
    zi9 = k9(np.vstack([xi9.flatten(), yi9.flatten()]))

    y10 = y10[np.logical_not(np.isnan(y10))]
    x10 = x10[np.logical_not(np.isnan(x10))]
    k10 = gaussian_kde(np.vstack([x10, y10]))
    xi10, yi10 = np.mgrid[x10.min():x10.max():x10.size**0.5*1j,y10.min():y10.max():y10.size**0.5*1j]
    zi10 = k10(np.vstack([xi10.flatten(), yi10.flatten()]))


    #COORDINATE DEI PUNTI NELLE ZONE PIU DENSE
    xy1 = np.vstack([x1,y1])
    kde1 = stats.gaussian_kde(xy1)
    density1 = kde1(xy1)

    punti1 = xy1.T[np.argmax(density1)]

    xy2 = np.vstack([x2,y2])
    kde2 = stats.gaussian_kde(xy2)
    density2 = kde1(xy2)

    punti2 = xy2.T[np.argmax(density2)]

    xy3 = np.vstack([x3,y3])
    kde3 = stats.gaussian_kde(xy3)
    density3 = kde2(xy3)

    punti3 = xy3.T[np.argmax(density3)]

    xy4 = np.vstack([x4,y4])
    kde4 = stats.gaussian_kde(xy4)
    density4 = kde4(xy4)

    punti4 = xy4.T[np.argmax(density4)]

    xy5 = np.vstack([x5,y5])
    kde5 = stats.gaussian_kde(xy5)
    density5 = kde5(xy5)

    punti5 = xy5.T[np.argmax(density5)]

    xy6 = np.vstack([x6,y6])
    kde6 = stats.gaussian_kde(xy6)
    density6 = kde6(xy6)

    punti6 = xy6.T[np.argmax(density6)]

    xy7 = np.vstack([x7,y7])
    kde7 = stats.gaussian_kde(xy7)
    density7 = kde7(xy7)

    punti7 = xy7.T[np.argmax(density7)]

    xy8 = np.vstack([x8,y8])
    kde8 = stats.gaussian_kde(xy8)
    density8 = kde8(xy8)

    punti8 = xy8.T[np.argmax(density8)]

    xy9 = np.vstack([x9,y9])
    kde9 = stats.gaussian_kde(xy9)
    density9 = kde9(xy9)

    punti9 = xy9.T[np.argmax(density9)]

    xy10 = np.vstack([x10,y10])
    kde10 = stats.gaussian_kde(xy10)
    density10 = kde10(xy10)

    punti10 = xy10.T[np.argmax(density10)]

    fig = pylab.figure(figsize=(7,4))
    #ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(111)

    #alpha=0.5 will make the plots semitransparent
    #ax1.pcolormesh(yi, xi, zi.reshape(xi.shape), alpha=0.5)
    #ax2.contourf(yi, xi, zi.reshape(xi.shape), alpha=0.5)
    #ax2.scatter(punti[0], punti[1], marker='o', c='r', s=10)


    #Coordinata del punto nella zona piu densa
    ax2.plot(punti1[1], punti1[0],"ro", markersize=10)
    ax2.plot(punti2[1], punti2[0],"ro", markersize=10)
    ax2.plot(punti3[1], punti3[0],"ro", markersize=10)
    ax2.plot(punti4[1], punti4[0],"ro", markersize=10)
    ax2.plot(punti5[1], punti5[0],"ro", markersize=10)
    ax2.plot(punti6[1], punti6[0],"ro", markersize=10)
    ax2.plot(punti7[1], punti7[0],"ro", markersize=10)
    ax2.plot(punti8[1], punti8[0],"ro", markersize=10)
    ax2.plot(punti9[1], punti9[0],"ro", markersize=10)
    ax2.plot(punti10[1], punti10[0],"ro", markersize=10)

    pylab.axis('off')

    ax2.plot([punti1[1],punti2[1],punti3[1],punti4[1]], [punti1[0], punti2[0], punti3[0], punti4[0]], 'b', linewidth=3)
    ax2.plot([punti5[1],punti6[1],punti7[1]], [punti5[0], punti6[0], punti7[0]], 'b', linewidth=3)
    ax2.plot([punti8[1],punti9[1],punti10[1]], [punti8[0], punti9[0], punti10[0]], 'b', linewidth=3)

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
