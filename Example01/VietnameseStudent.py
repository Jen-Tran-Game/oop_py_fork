#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 14:23:22 2025

@author: ngxxfus
"""
import cv2
class VietnameseStudent: 
    def __init__(self, 
                 Name = None, DoB = None, Sex = None, School = None, CCCD = None,
                 Hometown = None, Address = None, IDofStudent = None): 
        self.Name = Name
        self.DoB = DoB
        self.Sex = Sex
        self.School = School
        self.CCCD = CCCD
        self.Hometown = Hometown
        self.Address = Address
        self.IDofStudent = IDofStudent
    
    def showBackground(self): 
        print (f"Name: {self.Name}")
        print (f"DoB: {self.DoB}")
        print (f"Sex: {self.Sex}")
        print (f"School: {self.School}")
        print (f"CCCD: {self.CCCD}")
        print (f"Hometown: {self.Hometown}")
        print (f"Address: {self.Address}")
        print (f"IDofStudent: {self.IDofStudent}")


    

