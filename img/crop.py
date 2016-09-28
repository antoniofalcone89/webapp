import os,sys
from PIL import Image

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

arg = sys.argv[1]
crop(arg)
