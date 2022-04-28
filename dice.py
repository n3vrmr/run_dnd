# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 11:12:06 2022

@author: Nevermore
"""
# This is the first file

import random as rd

def roll(n:int,d:int):
    """Rolls a number of 'n' dice with a 'd' number of sides and adds the results of every die.
    You can use the arguments (1,100) to roll a percentile die.
    You can use the arguments (1,2) to make a coin toss.
    Rolling a 20 sided die can have special results if you get a 1 or a 20.
    """
    total = 0
    for i in range(n):
        result = rd.randint(1,d)
        total = total + result
    if d == 20 and total == 1:
        print("\033[1;31;47mUh-oh, natural one! Critical fail!\033[0m")
    elif d == 20 and total == 20:
        print("\033[1;32;40mNatural twenty! Critical success!\033[0m")
    elif d == 2 and total == 1:
        print("Heads")
    elif d == 2 and total == 2:
        print("Tails")
    print(total)
    return total

def main():
    if __name__ == '__main__':
        print("Take a chance, roll the dice!")
        
main()