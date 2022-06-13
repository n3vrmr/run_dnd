# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 02:55:10 2022

@author: Nevermore
"""
# This file is no longer in use

import classes

def proficiency_bonus():
    """ Defines your proficiency bonus according to your character level.
    
    """
    if classes.char_level <=4:
        return 2
    elif classes.char_level >=5 and classes.char_level <=8:
        return 3
    elif classes.char_level >=9 and classes.char_level <=12:
        return 4
    elif classes.char_level >=13 and classes.char_level <=16:
        return 5
    elif classes.char_level >=17 and classes.char_level <=20:
        return 6


save_proficiencies = {"Strength":False,"Dexterity":False,"Constitution":False,
                      "Intelligence":False,"Wisdom":False,"Charisma":False}

if classes.char_c == "Barbarian":
    save_proficiencies["Strength"] = True
    save_proficiencies["Constitution"] = True
elif classes.char_c == "Bard":
    save_proficiencies["Dexterity"] = True
    save_proficiencies["Charisma"] = True
elif classes.char_c == "Cleric":
    save_proficiencies["Wisdom"] = True
    save_proficiencies["Charisma"] = True
elif classes.char_c == "Druid":
    save_proficiencies["Intelligence"] = True
    save_proficiencies["Wisdom"] = True
elif classes.char_c == "Fighter":
    save_proficiencies["Strength"] = True
    save_proficiencies["Constitution"] = True
elif classes.char_c == "Monk":
    save_proficiencies["Strength"] = True
    save_proficiencies["Dexterity"] = True
elif classes.char_c == "Paladin":
    save_proficiencies["Wisdom"] = True
    save_proficiencies["Charisma"] = True
elif classes.char_c == "Ranger":
    save_proficiencies["Strength"] = True
    save_proficiencies["Dexterity"] = True
elif classes.char_c == "Rogue":
    save_proficiencies["Dexterity"] = True
    save_proficiencies["Intelligence"] = True
elif classes.char_c == "Sorcerer":
    save_proficiencies["Constitution"] = True
    save_proficiencies["Charisma"] = True
elif classes.char_c == "Warlock":
    save_proficiencies["Wisdom"] = True
    save_proficiencies["Charisma"] = True
elif classes.char_c == "Wizard":
    save_proficiencies["Intelligence"] = True
    save_proficiencies["Wisdom"] = True
        
skill_proficiencies = {}
if classes.char_c == "Barbarian":
    player_choice = input("Skill proficiencies - Choose two from Animal Handling, Athletics, Intimidation, Nature, Perception, and Survival: ").lower()
elif classes.char_c == "Bard":
    player_choice = input("Skill proficiencies - Choose any three: ").lower()
elif classes.char_c == "Cleric":
    player_choice = input("Skill proficiencies - Choose two from History, Insight, Medicine, Persuasion, Religion: ").lower()
elif classes.char_c == "Druid":
    player_choice = input("Skill proficiencies - Choose two from Arcana, Animal Handling, Insight, Medicine, Nature, Perception, Religion, and Survival: ").lower()
elif classes.char_c == "Fighter":
    player_choice = input("Skill proficiencies - Choose two from Acrobatics, Animal Handling, Athletics, History, Insight, Intimidation, Perception, and Survival: ").lower()
elif classes.char_c == "Monk":
    player_choice = input("Skill proficiencies - Choose two from Acrobatics, Athletics, History, Insight, Religion, and Stealth: ").lower()
elif classes.char_c == "Paladin":
    player_choice = input("Skill proficiencies - Choose two from Athletics, Insight, Intimidation, Medicine, Persuasion, and Religion: ").lower()
elif classes.char_c == "Ranger":
    player_choice = input("Skill proficiencies - Choose three from Animal Handling, Athletics, Insight, Investigation, Nature, Perception, Stealth, and Survival: ").lower()
elif classes.char_c == "Rogue":
    player_choice = input("Skill proficiencies - Choose four Acrobatics, Athletics, Deception, Insight, Intimidation, Investigation, Perception, Performance, Persuasion, Sleight of Hand, and Stealth: ").lower()
elif classes.char_c == "Sorcerer":
    player_choice = input("Skill proficiencies - Choose two from Arcana, Deception, Insight, Intimidation, Persuasion, and Religion: ").lower()
elif classes.char_c == "Warlock":
    player_choice = input("Skill proficiencies - Choose two from Arcana, Deception, History, Intimidation, Investigation, Nature, and Religion: ").lower()
elif classes.char_c == "Wizard":
    player_choice = input("Skill proficiencies - Choose two from Arcana, History, Insight, Investigation, Medicine, and Religion: ").lower()

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

def main():
    print("Rogues and bards are broken...")
    
if __name__ == '__main__':
    main()
