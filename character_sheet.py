# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 02:34:01 2022

@author: Nevermore
"""
# This file is no longer in use

import dice as d
import abilities as ab
import pej

def saving_throws():
    """Rolls a saving throw with a d20 plus your ability modifier. 
    If you are proficient, your proficiency bonus is also added.
    """
    save = input("Make a saving throw: ").lower().strip()
    if save == "str_save":
        if pej.save_proficiencies.get("Strength") == True:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Strength") + pej.proficiency_bonus())
        else:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Strength"))
    elif save == "dex_save":
        if pej.save_proficiencies.get("Dexterity") == True:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Dexterity") + pej.proficiency_bonus())
        else:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Dexterity"))
    elif save == "con_save":
        if pej.save_proficiencies.get("Constitution") == True:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Constitution") + pej.proficiency_bonus())
        else:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Constitution"))
    elif save == "int_save":
        if pej.save_proficiencies.get("Intelligence") == True:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Intelligence") + pej.proficiency_bonus())
        else:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Intelligence"))
    elif save == "wis_save":
        if pej.save_proficiencies.get("Wisdom") == True:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Wisdom") + pej.proficiency_bonus())
        else:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Wisdom"))
    elif save == "cha_save":
        if pej.save_proficiencies.get("Charisma") == True:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Charisma") + pej.proficiency_bonus())
        else:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Charisma"))
        
def ability_checks():
    """Rolls an ability check with a d20 plus your ability modifier.
    If you are proficient, your proficiency bonus is also added.
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
    If you are proficient, your proficiency bonus is also added.
    """
    check = input("Make a skill check: ").lower().strip()
    if check == "acrobatics":
        if pej.skill_proficiencies.get("acrobatics") == True:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Dexterity") + pej.proficiency_bonus())
        else:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Dexterity"))
    elif check == "animal handling":
        if pej.skill_proficiencies.get("animal handling") == True:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Wisdom") + pej.proficiency_bonus())
        else:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Wisdom"))
    elif check == "arcana":
        if pej.skill_proficiencies.get("arcana") == True:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Intelligence") + pej.proficiency_bonus())
        else:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Intelligence"))
    elif check == "athletics":
        if pej.skill_proficiencies.get("athletics") == True:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Strength") + pej.proficiency_bonus())
        else:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Strength"))
    elif check == "deception":
        if pej.skill_proficiencies.get("deception") == True:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Charisma") + pej.proficiency_bonus())
        else:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Charisma"))
    elif check == "history":
        if pej.skill_proficiencies.get("history") == True:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Intelligence") + pej.proficiency_bonus())
        else:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Intelligence"))
    elif check == "insight":
        if pej.skill_proficiencies.get("insight") == True:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Wisdom") + pej.proficiency_bonus())
        else:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Wisdom"))
    elif check == "intimidation":
        if pej.skill_proficiencies.get("intimidation") == True:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Charisma") + pej.proficiency_bonus())
        else:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Charisma"))
    elif check == "investigation":
        if pej.skill_proficiencies.get("investigation") == True:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Intelligence") + pej.proficiency_bonus())
        else:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Intelligence"))
    elif check == "medicine":
        if pej.skill_proficiencies.get("medicine") == True:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Wisdom") + pej.proficiency_bonus())
        else:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Wisdom"))
    elif check == "nature":
        if pej.skill_proficiencies.get("nature") == True:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Intelligence") + pej.proficiency_bonus())
        else:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Intelligence"))
    elif check == "perception":
        if pej.skill_proficiencies.get("perception") == True:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Wisdom") + pej.proficiency_bonus())
        else:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Wisdom"))
    elif check == "performance":
        if pej.skill_proficiencies.get("performance") == True:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Charisma") + pej.proficiency_bonus())
        else:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Charisma"))
    elif check == "persuasion":
        if pej.skill_proficiencies.get("persuasion") == True:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Charisma") + pej.proficiency_bonus())
        else:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Charisma"))
    elif check == "religion":
        if pej.skill_proficiencies.get("religion") == True:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Intelligence") + pej.proficiency_bonus())
        else:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Intelligence"))
    elif check == "sleight of hand":
        if pej.skill_proficiencies.get("sleight of hand") == True:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Dexterity") + pej.proficiency_bonus())
        else:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Dexterity"))
    elif check == "stealth":
        if pej.skill_proficiencies.get("stealth") == True:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Dexterity") + pej.proficiency_bonus())
        else:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Dexterity"))
    elif check == "survival":
        if pej.skill_proficiencies.get("survival") == True:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Wisdom") + pej.proficiency_bonus())
        else:
            print("Total:",d.roll(1,20) + ab.ability_mods.get("Wisdom"))

def main():
    print("Let's play some D&D!")

if __name__ == '__main__':
    main()
    saving_throws()
    ability_checks()
    skill_checks()
