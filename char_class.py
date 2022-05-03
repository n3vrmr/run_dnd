# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 15:46:19 2022

@author: Nevermore, Luiza
"""
# This is the third file

import dice as d
import abilities as ab

char_level = int(input("Character level: "))

def char_class():
    global char_c
    char_c = input("Choose your class: ")
    if char_c == "Barbarian":
        if char_level == 1:
            hp_first = 12 + ab.ability_mods.get("Constitution")
            hp = hp_first
        elif char_level > 1:
            hp_first = 12 + ab.ability_mods.get("Constitution")
            hp = hp_first + (d.roll((char_level - 1),12) + (char_level - 1) * ab.ability_mods.get("Constitution"))
    elif char_c == "Bard":
         if char_level == 1:
            hp_first = 8 + ab.ability_mods.get("Constitution")
            hp = hp_first
         elif char_level > 1:
            hp_first = 8 + ab.ability_mods.get("Constitution")
            hp = hp_first + (d.roll((char_level - 1),8) + (char_level - 1) * ab.ability_mods.get("Constitution"))
    elif char_c == "Cleric":
         if char_level == 1:
            hp_first = 8 + ab.ability_mods.get("Constitution")
            hp = hp_first
         elif char_level > 1:
            hp_first = 8 + ab.ability_mods.get("Constitution")
            hp = hp_first + (d.roll((char_level - 1),8) + (char_level - 1) * ab.ability_mods.get("Constitution"))
    elif char_c == "Druid":
         if char_level == 1:
            hp_first = 8 + ab.ability_mods.get("Constitution")
            hp = hp_first
         elif char_level > 1:
            hp_first = 8 + ab.ability_mods.get("Constitution")
            hp = hp_first + (d.roll((char_level - 1),8) + (char_level - 1) * ab.ability_mods.get("Constitution"))
    elif char_c == "Fighter":
         if char_level == 1:
            hp_first = 10 + ab.ability_mods.get("Constitution")
            hp = hp_first
         elif char_level > 1:
            hp_first = 10 + ab.ability_mods.get("Constitution")
            hp = hp_first + (d.roll((char_level - 1),10) + (char_level - 1) * ab.ability_mods.get("Constitution"))
    elif char_c == "Monk":
         if char_level == 1:
            hp_first = 8 + ab.ability_mods.get("Constitution")
            hp = hp_first
         elif char_level > 1:
            hp_first = 8 + ab.ability_mods.get("Constitution")
            hp = hp_first + (d.roll((char_level - 1),8) + (char_level - 1) * ab.ability_mods.get("Constitution"))
    elif char_c == "Paladin":
         if char_level == 1:
            hp_first = 10 + ab.ability_mods.get("Constitution")
            hp = hp_first
         elif char_level > 1:
            hp_first = 10 + ab.ability_mods.get("Constitution")
            hp = hp_first + (d.roll((char_level - 1),10) + (char_level - 1) * ab.ability_mods.get("Constitution"))
    elif char_c == "Ranger":
         if char_level == 1:
            hp_first = 10 + ab.ability_mods.get("Constitution")
            hp = hp_first
         elif char_level > 1:
            hp_first = 10 + ab.ability_mods.get("Constitution")
            hp = hp_first + (d.roll((char_level - 1),10) + (char_level - 1) * ab.ability_mods.get("Constitution"))
    elif char_c == "Rogue":
         if char_level == 1:
            hp_first = 8 + ab.ability_mods.get("Constitution")
            hp = hp_first
         elif char_level > 1:
            hp_first = 8 + ab.ability_mods.get("Constitution")
            hp = hp_first + (d.roll((char_level - 1),8) + (char_level - 1) * ab.ability_mods.get("Constitution"))
    elif char_c == "Sorcerer":
         if char_level == 1:
            hp_first = 6 + ab.ability_mods.get("Constitution")
            hp = hp_first
         elif char_level > 1:
            hp_first = 6 + ab.ability_mods.get("Constitution")
            hp = hp_first + (d.roll((char_level - 1),6) + (char_level - 1) * ab.ability_mods.get("Constitution"))
    elif char_c == "Warlock":
          if char_level == 1:
            hp_first = 8 + ab.ability_mods.get("Constitution")
            hp = hp_first
          elif char_level > 1:
            hp_first = 8 + ab.ability_mods.get("Constitution")
            hp = hp_first + (d.roll((char_level - 1),8) + (char_level - 1) * ab.ability_mods.get("Constitution"))
    elif char_c == "Wizard":
         if char_level == 1:
            hp_first = 6 + ab.ability_mods.get("Constitution")
            hp = hp_first
         elif char_level > 1:
            hp_first = 6 + ab.ability_mods.get("Constitution")
            hp = hp_first + (d.roll((char_level - 1),6) + (char_level - 1) * ab.ability_mods.get("Constitution"))
            
    print("HP:",hp)
    return hp
    return char_c

char_class()

if __name__ == '__main__':
    print("Terry Crews is a paladin")