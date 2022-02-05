# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 11:26:15 2021

@author: vishw
"""
import os  
import time
import pygetwindow as gw
eyeErgonomics= gw.getWindowsWithTitle('Eye ergonomics')[0]
i=0
while(1):
    print(i)
    i+=1
    os.system('cls')  
    print("Follow 20-20-20 Rule")
    print("\n\n")
    print("            The Rule states that we should see an object which is 20 feet\naway from us for 20 seconds for every 20 Minutes while using Computer\nor Mobile Phone.")
    print("\n"*10)
    print('            Currently We are using an interval of 13.33 Minutes')
    eyeErgonomics.minimize()
    eyeErgonomics.maximize()
    time.sleep(20)
    '''eyeErgonomics.maximize()
    time.sleep(1)
    eyeErgonomics.maximize()
    time.sleep(1)
    eyeErgonomics.maximize()
    time.sleep(5)'''
    eyeErgonomics.minimize()
    time.sleep(800)
