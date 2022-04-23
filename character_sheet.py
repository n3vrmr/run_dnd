# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 02:34:01 2022

@author: Nevermore
"""
# This is the final file

import dice
import abilities_and_mods

def saving_throws():
    save = input("Make a saving throw: ").lower().strip()
    if save == "str_save":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Strength"))
    elif save == "dex_save":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Dexterity"))
    elif save == "con_save":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Constitution"))
    elif save == "int_save":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Intelligence"))
    elif save == "wis_save":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Wisdom"))
    elif save == "cha_save":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Charisma"))
        
def ability_checks():
    check = input("Make an ability check: ").lower().strip()
    if check == "str":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Strength"))
    elif check == "dex":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Dexterity"))
    elif check == "con":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Constitution"))
    elif check == "int":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Intelligence"))
    elif check == "wis":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Wisdom"))
    elif check == "cha":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Charisma"))
        
    if check == "acrobatics":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Dexterity"))
    elif check == "animal handling":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Wisdom"))
    elif check == "arcana":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Intelligence"))
    elif check == "athletics":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Strength"))
    elif check == "deception":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Charisma"))
    elif check == "history":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Intelligence"))
    elif check == "insight":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Wisdom"))
    elif check == "intimidation":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Charisma"))
    elif check == "investigation":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Intelligence"))
    elif check == "medicine":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Wisdom"))
    elif check == "nature":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Intelligence"))
    elif check == "perception":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Wisdom"))
    elif check == "performance":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Charisma"))
    elif check == "persuasion":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Charisma"))
    elif check == "religion":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Intelligence"))
    elif check == "sleight of hand":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Dexterity"))
    elif check == "stealth":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Dexterity"))
    elif check == "survival":
        print(dice.roll_d20() + abilities_and_mods.ability_score_mods.get("Wisdom"))
        
