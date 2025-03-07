#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 14:22:30 2025

@author: ngxxfus
"""

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
   Methods:
       - Set/Get for each attribute
       - Speak(lang)
"""

"""
    Name of variables:
        - thisIsAVariable
        - this_is_a_variable
        - ThisIsAVariable
"""

from warnings import warn

"""
    __init__: là một hàm đặt biệt, được gọi khi khởi tạo class. constructor
    __super__:
    Mỗi phương thức (method) bên trong class, điều phải truyền tham số đầu tiên là "self" để báo cho Python biết đây là một hàm thuộc class đó.
"""
class People:
    def __check_none(self, var, none_msg="is None value!"):
        if var is None:
            raise ValueError(f"__check_none: {none_msg}")
    
    def __init__(self, Name=None, DoB=None, Height=None, Weight=None, Health=None, MotherTongue=None, Image=None):
        self.Name=Name
        self.DoB=DoB
        self.Height=Height
        self.Weight=Weight
        self.Health=Health
        self.MotherTongue=MotherTongue
        self.Image=Image        
    
        
    def SetName(self, new_name):
        
        self.__check_none(new_name, "`new_name` is None!!!!")
        
        if len(new_name) < 5:
            raise ValueError("Wrong size of `name`! The size of name must greater than 5 characters!!!")
        else:
            self.Name = new_name


    def PrintAllInfor(self):
        print("\nPeople.PrintAllInfor:")
        print(f"People.Name={self.Name}")
        print(f"People.DoB={self.DoB}")
        print(f"People.Height={self.Height}")
        print(f"People.Weight={self.Weight}")
        print(f"People.Health={self.Health}")
        print(f"People.Image={self.Image}")
        
    
if __name__ == "__main__":
    print("### This is `main` function in `People.py` ###")













