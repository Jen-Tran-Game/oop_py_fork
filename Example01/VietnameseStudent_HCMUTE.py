#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 14:23:36 2025

@author: ngxxfus
"""
import cv2  #Use OpenCV to display images instead of PIL because OpenCV displays image in higher quality, while PIL does not
from Example01.VietnameseStudent import VietnameseStudent
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
            image = cv2.imread(self.Image)
            if image is None: 
                raise ValueError ("Image_path not found !")
            
            height, width = image.shape[:2]

            new_width, new_height = width // 5, height // 5
            resized_image = cv2.resize(image, (new_width, new_height))

            cv2.imshow(f"Image of {self.Name}", resized_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except Exception as e: 
            # Use except Exception instead of raise Exception to prevent the program from stopping even though an error occurs
            print(f"Show image unsuccessfully: {e}")
        