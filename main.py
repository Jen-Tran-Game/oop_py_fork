#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 14:22:18 2025

@author: ngxxfus
"""

"""
.
└── OOP_PYTHON
    ├── Example01
    │   ├── People.py                          
    │   ├── VietnamesePeople.py                <-------- your definition here!
    │   ├── VietnameseStudent_HCMUTE.py
    │   └── VietnameseStudent.py
    └── main.py                                <-------- want to run from this file?

"""

### Example01/People.py import Object named People
from Example01.VietnamesePeople import VietnamesePeople

"""
__name__: "__main__" khi được chạy trực tiếp
__name__: <tên file> khi được chạy để import vào một file khác
"""

if __name__ == "__main__":
    print("### This is `main` function ###")
    me = VietnamesePeople(Name="Nguyen Thanh Phu", DoB="03/02/2004", MotherTongue="Vie")
    me.SetName(new_name="Nguyễn Thanh Phú")
    me.CCCD = "080204xx28xx"
    me.DoB = "03/02/2xxx"
    me.MotherTongue='Vie'
    me.Culture='Miền tây Nam bộ'
    
    me.PrintAllInfor()