import os,sys
import PIL
from PIL import Image

def resize(arg1):
    baseheight = 321
    img = Image.open(arg1)
    hpercent = (baseheight / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))
    img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
    img.save(arg1)

arg = sys.argv[1]
resize(arg)
