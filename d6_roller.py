# -*- coding: utf-8 -*-
"""
Created on Thu May  5 22:09:23 2022

@author: Nevermore
"""

import dice as d

def ability_rolls():
    """Rolls 4d6 and adds the three highest values.
    Useful for rolling values for your character's ability scores."""
    d6 = d.roll(4,6,True)
    d6.sort()
    del d6[0]
    adds = sum(d6)
    print(adds)
    return adds

def main():
    print("Randomize")
    
if __name__ == '__main__':
    main()
    ability_rolls()