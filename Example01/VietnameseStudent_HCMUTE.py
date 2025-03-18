#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 14:23:36 2025

@author: ngxxfus
"""
# import cv2:  Use OpenCV to display images instead of PIL because OpenCV displays image in higher quality, while PIL does not
from Example01.VietnameseStudent import VietnameseStudent
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.transform import resize # Use to resize image

class VietnameseStudent_HCMUTE(VietnameseStudent): 
    def __init__(self, 
                 Name = None, DoB = None, Sex = None, School = None, CCCD = None, 
                 Hometown = None, Address = None, IDofStudent = None, 
                 Gmail = None, Major = None, GPA = None, Image = None):
        super().__init__ (Name, DoB, Sex, School, CCCD,
                          Hometown, Address, IDofStudent)
        self.Gmail = Gmail
        self.Major = Major
        self.GPA = GPA
        self.Image = Image

    def showBackground(self):
        super().showBackground()
        print(f"Gmail: {self.Gmail}")
        print(f"Major: {self.Major}")
        print(f"GPA: {self.GPA}")
        print(f"Image: {self.Image}")

    def showImage(self):
        try: 
            image = plt.imread(self.Image)
            if image is None: 
                raise ValueError ("Image_path not found !")
            
            height, width = image.shape[:2]

            # output_image = resize(image, (height, width))

            plt.imshow(image) # Display image on figure
            plt.axis("off")
            plt.show() # Display figure on screen
        except Exception as e: 
            # Use except Exception instead of raise Exception to prevent the program from stopping even though an error occurs
            print(f"Show image unsuccessfully: {e}")
        