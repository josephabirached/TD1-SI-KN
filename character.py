# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:20:34 2020

@author: Charbel
"""


class Character:
    def __init__(self, name, first_name, age, profession, morale_value):
        self.name = name
        self.first_name = first_name
        self.age = age
        self.profession = profession
        self.morale_value = morale_value
        
    def getName(self):
        return self.name   
    
    def getFirstName(self):
        return self.first_name
    
    def getAge(self):
        return self.age
    
    def getProfession(self):
        return self.profession
    
    def getMoraleValue(self):
        return self.morale_value
    
    def setName(self, name):
        self.name = name 
        
    def setFirstName(self, first_name):
        self.first_name = first_name
        
    def setAge(self, age):
        self.age = age
        
    def setProfession(self, profession):
        self.profession = profession
        
    def setMoraleBoost(self, morale_boost):
        return self.morale_boost
        
    def __repr__(self):
        return "[{} {}: Age = {}, Prof = {}, Morale Boost = {}]".format(self.name,self.first_name,self.age,self.profession,self.morale_value)
        
    