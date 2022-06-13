# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 11:12:06 2022

@author: Nevermore
"""
# This is the first file

import random as rd
import time as t

def roll(n:int,d:int,s=False,q=False):
    """Rolls a number of 'n' dice with a 'd' number of sides and adds the results of every die.
    The argument 's' is an optional argument useful for rolling multiple dice at a time when you need to keep their results.
    To query advantage or disadvantage, set the 's' and 'q' arguments as True.
    You can use the arguments (1,100) to roll a percentile die.
    You can use the arguments (1,2) to make a coin toss.
    Rolling a 20 sided die can have special results if you get a 1 or a 20.
    """
    total = 0
    box = []
    for i in range(n):
        result = rd.randint(1,d)
        total = total + result
        if s:
            box.append(result)
    if s and q == False:
        print("Rolling...")
        t.sleep(1.8)
        return box
    elif d == 20 and s and q:
        a = input("Normal, advantage or disadvantage? ")
        if "nor" in a:
            total = rd.randint(1,d)
            print("Rolling...")
            t.sleep(1.8)
            print("Dice result:",total)
            if total == 1:
                print("\033[1;31;47mUh-oh, natural one! Critical fail!\033[0m")
            elif total == 20:
                print("\033[1;32;40mNatural twenty! Critical success!\033[0m")
            return total
        if "adv" in a:
            roll = max(box)
            print("Rolling with advantage...")
            t.sleep(1.8)
            print(roll)
            if roll == 20:
                print("\033[1;32;40mNatural twenty! Critical success!\033[0m")
            return roll
        elif "dis" in a:
            roll = min(box)
            print("Rolling with disadvantage...")
            t.sleep(1.8)
            print(roll)
            if roll == 1:
                print("\033[1;31;47mUh-oh, natural one! Critical fail!\033[0m")
            return roll
    else:
        print("Rolling...")
        t.sleep(1.8)
        print("Dice result:",total)
        if d == 20 and total == 1 and n == 1:
            print("\033[1;31;47mUh-oh, natural one! Critical fail!\033[0m")
        elif d == 20 and total == 20 and n == 1:
            print("\033[1;32;40mNatural twenty! Critical success!\033[0m")
        elif d == 2 and total == 1:
            print("Heads")
        elif d == 2 and total == 2:
            print("Tails")
        return total

def main():
    print("Take a chance, roll the dice!")
    
if __name__ == '__main__':
    main()
    help(roll)