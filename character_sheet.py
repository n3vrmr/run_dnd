# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 02:34:01 2022

@author: Nevermore
"""
# This is the final file

import dice as d
import abilities as ab

def saving_throws():
    """Rolls a saving throw with a d20 plus your ability modifier.
    """
    save = input("Make a saving throw: ").lower().strip()
    if save == "str_save":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Strength"))
    elif save == "dex_save":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Dexterity"))
    elif save == "con_save":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Constitution"))
    elif save == "int_save":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Intelligence"))
    elif save == "wis_save":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Wisdom"))
    elif save == "cha_save":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Charisma"))
        
def ability_checks():
    """Rolls an ability check with a d20 plus your ability modifier.
    """
    check = input("Make an ability check: ").lower().strip()
    if check == "str":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Strength"))
    elif check == "dex":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Dexterity"))
    elif check == "con":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Constitution"))
    elif check == "int":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Intelligence"))
    elif check == "wis":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Wisdom"))
    elif check == "cha":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Charisma"))

def skill_checks():
    """Rolls a skill check with a d20 plus the relevant ability modifier.
    """
    check = input("Make a skill check: ").lower().strip()
    if check == "acrobatics":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Dexterity"))
    elif check == "animal handling":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Wisdom"))
    elif check == "arcana":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Intelligence"))
    elif check == "athletics":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Strength"))
    elif check == "deception":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Charisma"))
    elif check == "history":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Intelligence"))
    elif check == "insight":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Wisdom"))
    elif check == "intimidation":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Charisma"))
    elif check == "investigation":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Intelligence"))
    elif check == "medicine":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Wisdom"))
    elif check == "nature":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Intelligence"))
    elif check == "perception":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Wisdom"))
    elif check == "performance":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Charisma"))
    elif check == "persuasion":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Charisma"))
    elif check == "religion":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Intelligence"))
    elif check == "sleight of hand":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Dexterity"))
    elif check == "stealth":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Dexterity"))
    elif check == "survival":
        print("Total:",d.roll(1,20) + ab.ability_mods.get("Wisdom"))

if __name__ == '__main__':
    print("Let's play some D&D!")