# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 15:46:19 2022

@author: Nevermore
"""
# This is the second file

import dice as d
import abilities as ab

char_level = int(input("Character level: "))

def char_class():
    char_class = input("Choose your class: ")
    if char_class == "Barbarian":
        if char_level == 1:
            hp_first = 12 + ab.ability_mods.get("Constitution")
            hp = hp_first
            print("HP:",hp)
            return hp
        elif char_level > 1:
            hp_first = 12 + ab.ability_mods.get("Constitution")
            hp = hp_first + (d.roll((char_level - 1),12) + (char_level - 1) * ab.ability_mods.get("Constitution"))
            print("HP:",hp)
            return hp
        
char_class()

if __name__ == '__main__':
    print("Terry Crews is a paladin")
