# -*- coding: utf-8 -*-
import sys
import glob
import os, traceback, time
# from operator import lt
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# get image path
def get_folder(fpath, wm_file, save_path):
    try:
        img_suffix_list = ['png', 'PNG','jpg', 'JPG', 'bmp']
        for i in os.listdir(fpath):
            if i.split('.')[-1] in img_suffix_list:
                img_path = fpath + '/' + i
                img_water_mark(img_file=img_path, wm_file=wm_file, save_path=save_path)
            time.sleep(0.3)
    except Exception as e:
        print(traceback.print_exc())

# add water mark
def img_water_mark(img_file, wm_file, save_path):
    try:
        img = Image.open(img_file)
        watermark = Image.open(wm_file)
        img_size = img.size
        wm_size = watermark.size
        # print(wm_size)

        # if img_size[0] & lt & wm_size[0]:
        watermark.resize(tuple(map(lambda x: int(x * 0.5), watermark.size)))
        print('image size：', img_size)
        # default, the watermark position is set to the lower right corner
        wm_position = (img_size[0] - wm_size[0], img_size[1] - wm_size[1])
        # new layer
        layer = Image.new('RGBA', img.size)
        # Add watermark picture to layer
        layer.paste(watermark, wm_position) 
        mark_img = Image.composite(layer, img, layer)
        new_file_name = img_file.split('/')[-1]
        mark_img.save(save_path + new_file_name)
    except Exception as e:
        print(traceback.print_exc())

def watermarks(post_name):
    if post_name == 'all':
        post_name = '*'
    dir_name = './sourceimg/' + post_name + '/*'
    for files in glob.glob(dir_name):
        im = Image.open(files)
        if len(im.getbands()) < 3:
            im = im.convert('RGB')
            print(files)
        font = ImageFont.truetype('STSONG.TTF', max(30, int(im.size[1] / 20)))
        draw = ImageDraw.Draw(im)
        draw.text((im.size[0] / 2, im.size[1] / 2), u'@kuibarj.top', fill=(0, 0, 0), font=font)
        im.save(files)


if __name__ == '__main__':
    print("\n[*] Compositing please wait...")
    if len(sys.argv) == 2:
        get_folder(fpath=r"./sourceimg/image/", wm_file=r"./resources/blogo.png", save_path=r"./sourceimg/image/")
        watermarks(sys.argv[1])
        print('[+] add logo success!')
    else:
        print('[usage] <input>')
        print('\netc: python3 watermark.py all')

