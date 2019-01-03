# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 14:09:00 2018

@author: b.sudheendra.kalyan
"""

import os
import img2pdf
from os import listdir
from os.path import isfile, join 

mypath = "C:/Users/b.sudheendra.kalyan/Desktop/cathy/inception_model/test_cats/52109918/" # path to your Image directory 

for each_file in os.listdir(mypath):
    if isfile(join(mypath,each_file)):
        image_path = os.path.join(mypath,each_file)
        pdf_path =  os.path.join(mypath,each_file.rsplit('.', 1)[0]+'.pdf')
        #print(pdf_path)
        #img.write(img2pdf.convert()
        if(image_path.endswith(".jpg") or image_path.endswith(".JPG")):
            print(image_path)
            with open(pdf_path, "wb") as f:
                f.write(img2pdf.convert(image_path))
            #with open(pdf_path, "wb") as img:
            #    img.write(img2pdf.convert(pdf_path))
        

#with open("output.pdf", "wb") as f:
#    f.write(img2pdf.convert([i for i in os.listdir('.') if i.endswith(".jpg")]))