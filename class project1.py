# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 12:53:05 2024

@author: LENOVO
"""
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def split_name(self):
        new_name = self.name.split(" ")
        first_name = new_name[0]
        last_name = new_name[-1]
        return first_name, last_name


 