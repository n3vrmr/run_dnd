# -*- coding: utf-8 -*-
"""
Created on Thu May  5 22:09:23 2022

@author: Nevermore
"""

import dice as d

def ability_rolls(r=True):
    """Rolls 4d6 and adds the three highest values.
    Useful for rolling values for your character's ability scores.
    If you want to roll one value at a time, no argument is needed.
    If you want to roll all six values to later decide which ability scores will receive them,
    use the optional argument 'False'.
    """
    if r:
        d6 = d.roll(4,6,True)
        d6.sort()
        del d6[0]
        adds = sum(d6)
        print(adds)
        return adds
    else:
        raw_scores = []
        for i in range(6):
            d6 = d.roll(4,6,True)
            d6.sort()
            del d6[0]
            adds = sum(d6)
            raw_scores.append(adds)
        print(raw_scores)
        return raw_scores

def main():
    print("Randomize")
    
if __name__ == '__main__':
    main()
    ability_rolls()
    ability_rolls(False)