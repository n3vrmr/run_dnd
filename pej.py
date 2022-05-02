# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 02:55:10 2022

@author: Nevermore
"""
# This is the fourth file

import char_class as ch_c

def proficiency_bonus():
    """ Defines your proficiency bonus according to your character level.
    
    """
    if ch_c.char_level <=4:
        return 2
    elif ch_c.char_level >=5 and ch_c.char_level <=8:
        return 3
    elif ch_c.char_level >=9 and ch_c.char_level <=12:
        return 4
    elif ch_c.char_level >=13 and ch_c.char_level <=16:
        return 5
    elif ch_c.char_level >=17 and ch_c.char_level <=20:
        return 6


save_proficiencies = {}
if ch_c.char_c == "Barbarian":
    proficient = True
    while proficient:
        save_proficiencies["Strength"] = True
        save_proficiencies["Dexterity"] = False
        save_proficiencies["Constitution"] = True
        save_proficiencies["Intelligence"] = False
        save_proficiencies["Wisdom"] = False
        save_proficiencies["Charisma"] = False
        proficient = False
        
skill_proficiencies = {}
if ch_c.char_c == "Barbarian":
    proficient = True
    while proficient:
        player_choice = input("Choose two from Animal Handling, Athletics, Intimidation, Nature, Perception, and Survival: ").lower()
        skill_proficiencies["acrobatics"] = False
        skill_proficiencies["animal handling"] = False
        if "animal handling" in player_choice:
            skill_proficiencies["animal handling"] = True
        skill_proficiencies["arcana"] = False
        skill_proficiencies["athletics"] = False
        if "athletics" in player_choice:
            skill_proficiencies["athletics"] = True
        skill_proficiencies["deception"] = False
        skill_proficiencies["history"] = False
        skill_proficiencies["insight"] = False
        skill_proficiencies["intimidation"] = False
        if "intimidation" in player_choice:
            skill_proficiencies["intimidation"] = True
        skill_proficiencies["investigation"] = False
        skill_proficiencies["medicine"] = False
        skill_proficiencies["nature"] = False
        if "nature" in player_choice:
            skill_proficiencies["nature"] = True
        skill_proficiencies["perception"] = False
        if "perception" in player_choice:
            skill_proficiencies["perception"] = True
        skill_proficiencies["performance"] = False
        skill_proficiencies["persuasion"] = False
        skill_proficiencies["religion"] = False
        skill_proficiencies["sleight of hand"] = False
        skill_proficiencies["stealth"] = False
        skill_proficiencies["survival"] = False
        if "survival" in player_choice:
            skill_proficiencies["survival"] = True
        proficient = False

print("Proficiency bonus:",proficiency_bonus())

expertise = proficiency_bonus()*2

if __name__ == '__main__':
    print("Rogues and bards are broken...")