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
    player_choice = input("Choose two from Animal Handling, Athletics, Intimidation, Nature, Perception, and Survival: ").lower()


proficient = True
while proficient:
    skill_proficiencies["acrobatics"] = False
    if "acrobatics" in player_choice:
        skill_proficiencies["acrobatics"] = True
    skill_proficiencies["animal handling"] = False
    if "animal handling" in player_choice:
        skill_proficiencies["animal handling"] = True
    skill_proficiencies["arcana"] = False
    if "arcana" in player_choice:
        skill_proficiencies["arcana"] = True
    skill_proficiencies["athletics"] = False
    if "athletics" in player_choice:
        skill_proficiencies["athletics"] = True
    skill_proficiencies["deception"] = False
    if "deception" in player_choice:
        skill_proficiencies["deception"] = True
    skill_proficiencies["history"] = False
    if "history" in player_choice:
        skill_proficiencies["history"] = True
    skill_proficiencies["insight"] = False
    if "insight" in player_choice:
        skill_proficiencies["insight"] = True
    skill_proficiencies["intimidation"] = False
    if "intimidation" in player_choice:
        skill_proficiencies["intimidation"] = True
    skill_proficiencies["investigation"] = False
    if "investigation" in player_choice:
        skill_proficiencies["investigation"] = True
    skill_proficiencies["medicine"] = False
    if "medicine" in player_choice:
        skill_proficiencies["medicine"] = True
    skill_proficiencies["nature"] = False
    if "nature" in player_choice:
        skill_proficiencies["nature"] = True
    skill_proficiencies["perception"] = False
    if "perception" in player_choice:
        skill_proficiencies["perception"] = True
    skill_proficiencies["performance"] = False
    if "performance" in player_choice:
        skill_proficiencies["performance"] = True
    skill_proficiencies["persuasion"] = False
    if "persuasion" in player_choice:
        skill_proficiencies["persuasion"] = True
    skill_proficiencies["religion"] = False
    if "religion" in player_choice:
        skill_proficiencies["religion"] = True
    skill_proficiencies["sleight of hand"] = False
    if "sleight of hand" in player_choice:
        skill_proficiencies["sleight of hand"] = True
    skill_proficiencies["stealth"] = False
    if "stealth" in player_choice:
        skill_proficiencies["stealth"] = True
    skill_proficiencies["survival"] = False
    if "survival" in player_choice:
        skill_proficiencies["survival"] = True
    proficient = False

print("Proficiency bonus:",proficiency_bonus())

expertise = proficiency_bonus()*2

if __name__ == '__main__':
    print("Rogues and bards are broken...")