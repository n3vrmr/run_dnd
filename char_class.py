# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 15:46:19 2022

@author: Nevermore
"""
# This file is kicking my ass

import dice as d
import abilities as ab

char_level = int(input("Character level: "))

def char_class():
    char_class = input("Choose your class: ")
    if char_class == "Barbarian":
        if char_level == 1:
            hp_first = 12 + ab.ability_mods.get("Constitution")
        print("HP:",hp_first) # UnboundLocalError: local variable 'hp_first' referenced before assignment
        return hp_first
        if char_level > 1:
            hp = hp_first + (char_level - 1) * (d.roll(1,12)+ab.ability_mods.get("Constitution"))
        print("HP:",hp)
        return hp
        
char_class()

if __name__ == '__main__':
    print("Terry Crews is a paladin")