# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 11:01:25 2020

@author: Charbel
"""


class Army:
    
    def __init__(self, cheif, base_morale):
        self.cheif = cheif
        self.base_morale = base_morale
    
    def getCheif(self):
        return self.cheif
    
    def getBaseMorale(self):
        return self.base_morale
    
    def setCheif(self, cheif):
        self.cheif = cheif
        
    def setBaseMorale(self, base_morale):
        self.base_morale = base_morale
        
    def __repr__(self):
        return "[Cheif: {}, Base: {}, total morale:{}]".format(self.cheif,self.base_morale,self.get_total_morale())
    
    def get_total_morale(self):
        return self.cheif.getMoraleValue() * self.base_morale