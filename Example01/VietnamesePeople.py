#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 14:22:47 2025

@author: ngxxfus
"""

from Example01.People import People

"""
   People
   Attributes:
       - Name
       - DoB : date of birth, DD/MM/YYYY
       - Height: cm
       - Weight: Kg
       - Health: 0-10
       - MotherTongue: 
       - Image
       - Culture
       - CCCD
       - Address
   Methods:
       - Set/Get for each attribute
       - Speak(lang)
"""
"""
    super: là đối tượng tham chiếu tới class cha
"""
class VietnamesePeople(People):
    def __init__(self, 
                   Name=None, DoB=None, Height=None, 
                   Weight=None, Health=None, MotherTongue=None, 
                   Image=None, Culture=None, CCCD=None, Address=None):
        # Khởi tạo class cha (People)
        super().__init__(Name, DoB, Height, Weight, Health, 
                       MotherTongue, Image)
        # Khởi tạo class con (class hiện tại)
        self.Culture = Culture
        self.CCCD=CCCD
        self.Address=Address
    
    def PrintAllInfor(self):
        super().PrintAllInfor()
        print("\nVietnamesePeople.PrintAllInfor:")
        print(f"People.Culture={self.Culture}")
        print(f"People.CCCD={self.CCCD}")
        print(f"People.Address={self.Address}")
    

    