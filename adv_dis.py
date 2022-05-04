#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 16:26:11 2022

@author: Nevermore
"""

import dice as d

# print(d.roll(2,20))
# result = min(d.roll(2,20,True))

adv = False
dis = False
def adv_dis():
    query = input("Query: ")
    if "dis" in query:
        dis = True
        result = min(d.roll(2,20,True))
    elif "adv" in query:
        adv = True
        result = max(d.roll(2,20,True))
    print(result)
    return result

adv_dis()