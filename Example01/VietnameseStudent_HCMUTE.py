#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 14:23:36 2025

@author: ngxxfus
"""
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

        