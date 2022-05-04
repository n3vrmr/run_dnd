#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 16:26:11 2022
@author: Nevermore
"""

import dice as d

# print(d.roll(2,20))
# game_situation = min(d.roll(2,20,True))

def adv_dis():
    query = input("Query: ")
    if "dis" in query:
        rolls = d.roll(2,20,True)
        game_situation = min(rolls)
        print("Rolling with disadvantage:",game_situation)
        if 1 in rolls:
            print("\033[1;31;47mUh-oh, natural one! Critical fail!\033[0m")
    elif "adv" in query:
        rolls = d.roll(2,20,True)
        game_situation = max(rolls)
        print("Rolling with advantage:",game_situation)
        if 20 in rolls:
            print("\033[1;32;40mNatural twenty! Critical success!\033[0m")
    return game_situation

def main():
    print("Mote of Possibility")
    
if __name__ == '__main__':
    main()