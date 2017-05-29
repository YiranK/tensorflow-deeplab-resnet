import os
import numpy as np

file_path = "/media/Disk/VOCdevkit/VOC2012/ImageSets/Segmentation/train.txt"
write_path = "./train.txt"
imgdir = "/JPEGImages/"
maskdir = "/SegmentationClassAug/" 

count = 0
with open(file_path, 'rb') as fr, open(write_path,'wb') as fw:
	for line in fr:
		imgname = line.strip()
		img_path = imgdir+imgname+'.jpg'
		mask_path = maskdir+imgname+'.png'
		fw.write(img_path+" "+mask_path+"\n")
		if (count < 2):
			print imgname,img_path,mask_path
		count = count+1

