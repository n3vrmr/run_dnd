# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 02:34:01 2022

@author: Nevermore
"""
# This is the final file

import dice as d
import abilities as ab

def saving_throws():
    save = input("Make a saving throw: ").lower().strip()
    if save == "str_save":
        print(d.roll(1,20) + ab.ability_mods.get("Strength"))
        return d.roll(1,20) + ab.ability_mods.get("Strength")
    elif save == "dex_save":
        print(d.roll(1,20) + ab.ability_mods.get("Dexterity"))
        return d.roll(1,20) + ab.ability_mods.get("Dexterity")
    elif save == "con_save":
        print(d.roll(1,20) + ab.ability_mods.get("Constitution"))
        return d.roll(1,20) + ab.ability_mods.get("Constitution")
    elif save == "int_save":
        print(d.roll(1,20) + ab.ability_mods.get("Intelligence"))
        return d.roll(1,20) + ab.ability_mods.get("Intelligence")
    elif save == "wis_save":
        print(d.roll(1,20) + ab.ability_mods.get("Wisdom"))
        return d.roll(1,20) + ab.ability_mods.get("Wisdom")
    elif save == "cha_save":
        print(d.roll(1,20) + ab.ability_mods.get("Charisma"))
        return d.roll(1,20) + ab.ability_mods.get("Charisma")
        
def ability_checks():
    check = input("Make an ability check: ").lower().strip()
    if check == "str":
        print(d.roll(1,20) + ab.ability_mods.get("Strength"))
        return d.roll(1,20) + ab.ability_mods.get("Strength")
    elif check == "dex":
        print(d.roll(1,20) + ab.ability_mods.get("Dexterity"))
        return d.roll(1,20) + ab.ability_mods.get("Dexterity")
    elif check == "con":
        print(d.roll(1,20) + ab.ability_mods.get("Constitution"))
        return d.roll(1,20) + ab.ability_mods.get("Constitution")
    elif check == "int":
        print(d.roll(1,20) + ab.ability_mods.get("Intelligence"))
        return d.roll(1,20) + ab.ability_mods.get("Intelligence")
    elif check == "wis":
        print(d.roll(1,20) + ab.ability_mods.get("Wisdom"))
        return d.roll(1,20) + ab.ability_mods.get("Wisdom")
    elif check == "cha":
        print(d.roll(1,20) + ab.ability_mods.get("Charisma"))
        return d.roll(1,20) + ab.ability_mods.get("Charisma")
        
    if check == "acrobatics":
        print(d.roll(1,20) + ab.ability_mods.get("Dexterity"))
        return d.roll(1,20) + ab.ability_mods.get("Dexterity")
    elif check == "animal handling":
        print(d.roll(1,20) + ab.ability_mods.get("Wisdom"))
        return d.roll(1,20) + ab.ability_mods.get("Wisdom")
    elif check == "arcana":
        print(d.roll(1,20) + ab.ability_mods.get("Intelligence"))
        return d.roll(1,20) + ab.ability_mods.get("Intelligence")
    elif check == "athletics":
        print(d.roll(1,20) + ab.ability_mods.get("Strength"))
        return d.roll(1,20) + ab.ability_mods.get("Strength")
    elif check == "deception":
        print(d.roll(1,20) + ab.ability_mods.get("Charisma"))
        return d.roll(1,20) + ab.ability_mods.get("Charisma")
    elif check == "history":
        print(d.roll(1,20) + ab.ability_mods.get("Intelligence"))
        return d.roll(1,20) + ab.ability_mods.get("Intelligence")
    elif check == "insight":
        print(d.roll(1,20) + ab.ability_mods.get("Wisdom"))
        return d.roll(1,20) + ab.ability_mods.get("Wisdom")
    elif check == "intimidation":
        print(d.roll(1,20) + ab.ability_mods.get("Charisma"))
        return d.roll(1,20) + ab.ability_mods.get("Charisma")
    elif check == "investigation":
        print(d.roll(1,20) + ab.ability_mods.get("Intelligence"))
        return d.roll(1,20) + ab.ability_mods.get("Intelligence")
    elif check == "medicine":
        print(d.roll(1,20) + ab.ability_mods.get("Wisdom"))
        return d.roll(1,20) + ab.ability_mods.get("Wisdom")
    elif check == "nature":
        print(d.roll(1,20) + ab.ability_mods.get("Intelligence"))
        return d.roll(1,20) + ab.ability_mods.get("Intelligence")
    elif check == "perception":
        print(d.roll(1,20) + ab.ability_mods.get("Wisdom"))
        return d.roll(1,20) + ab.ability_mods.get("Wisdom")
    elif check == "performance":
        print(d.roll(1,20) + ab.ability_mods.get("Charisma"))
        return d.roll(1,20) + ab.ability_mods.get("Charisma")
    elif check == "persuasion":
        print(d.roll(1,20) + ab.ability_mods.get("Charisma"))
        return d.roll(1,20) + ab.ability_mods.get("Charisma")
    elif check == "religion":
        print(d.roll(1,20) + ab.ability_mods.get("Intelligence"))
        return d.roll(1,20) + ab.ability_mods.get("Intelligence")
    elif check == "sleight of hand":
        print(d.roll(1,20) + ab.ability_mods.get("Dexterity"))
        return d.roll(1,20) + ab.ability_mods.get("Dexterity")
    elif check == "stealth":
        print(d.roll(1,20) + ab.ability_mods.get("Dexterity"))
        return d.roll(1,20) + ab.ability_mods.get("Dexterity")
    elif check == "survival":
        print(d.roll(1,20) + ab.ability_mods.get("Wisdom"))
        return d.roll(1,20) + ab.ability_mods.get("Wisdom")
