import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
 
sets = ['train', 'test', 'val']
 
classes = ["AoXian","HeiBan","GanTiao","LieKou","HaoZao","NiaoZhuo","LanZao","ShuZao"]
 
 
def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    # print(str(x).split(".")[0])
    # print(str(y).split(".")[0])
    #
    # print(str(w).split(".")[0])
    # print(str(h).split(".")[0])

    if not str(x).split(".")[0] == "0":
        print(x, y, w, h)
    elif  not str(y).split(".")[0] == "0":
        print(x, y, w, h)
    elif not str(w).split(".")[0] == "0":
        print(x, y, w, h)
    elif not str(h).split(".")[0] == "0":
        print(x, y, w, h)
    return (x, y, w, h)
 
 
def convert_annotation(image_id):
    in_file = open('data/Annotations/%s.xml' % (image_id))
    out_file = open('data/labels/%s.txt' % (image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
 
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
 
 
wd = getcwd()
print(wd)
dirlist = os.listdir("data/images")
for image_set in sets:
    if not os.path.exists('data/labels/'):
        os.makedirs('data/labels/')
    image_ids = open('data/ImageSets/%s.txt' % (image_set)).read().strip().split()
    list_file = open('data/%s.txt' % (image_set), 'w')
    for image_id in image_ids:
        for dirs in dirlist:
            s = dirs.split("."[0])
            if image_id == s[0]:

                list_file.write('data/images/%s.%s\n' % (image_id, s[1]))
                convert_annotation(image_id)
            else:
                continue
    list_file.close()


