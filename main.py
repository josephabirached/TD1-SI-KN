# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 10:19:59 2020

@author: Charbel
"""


from character import Character
import csv
import random
from army import Army

if __name__ == "__main__":
    characters = []
    with open('characters.csv') as csvfile:   
        reader=csv.reader(csvfile)
        flag = True
        for row in reader:
            if flag:
                flag = False
                continue
            characters.append(Character(row[0], row[1], int(row[2]), row[3], float(row[4])))
    
    armies = []
    for c in characters:
        armies.append(Army(c,float(random.uniform(20.0, 100.0))))
    
    somme = 0.0
    for a in armies:
        print(a)
        somme+=a.get_total_morale()
        
    print("Somme = {}".format(somme))
        
    import numpy as np
    base = np.random.uniform(20,100, 5)
    boost = np.array([a.getCheif().getMoraleValue() for a in armies])
    s = np.sum(np.multiply(base,boost))
    print("somme = {}".format(s))