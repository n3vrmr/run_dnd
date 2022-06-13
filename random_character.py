# -*- coding: utf-8 -*-
"""
Created on Thu May  5 22:41:47 2022

@author: Nevermore
"""
# This file is no longer in use
import d6_roller
import time as t

def random_scores():
    """Randomizes your character's ability scores.
    Hope you're feeling lucky!
    """
    ability_scores = {}
    score = True
    while score:
        ability_scores["Strength"] = d6_roller.ability_rolls()
        ability_scores["Dexterity"] = d6_roller.ability_rolls()
        ability_scores["Constitution"] = d6_roller.ability_rolls()
        ability_scores["Intelligence"] = d6_roller.ability_rolls()
        ability_scores["Wisdom"] = d6_roller.ability_rolls()
        ability_scores["Charisma"] = d6_roller.ability_rolls()
        score = False
        
    ability_mods = {}
    modifier = True
    while modifier:
        ability_mods["Strength"] = (ability_scores.get("Strength") - 10)//2
        ability_mods["Dexterity"] = (ability_scores.get("Dexterity") - 10)//2
        ability_mods["Constitution"] = (ability_scores.get("Constitution") - 10)//2
        ability_mods["Intelligence"] = (ability_scores.get("Intelligence") - 10)//2
        ability_mods["Wisdom"] = (ability_scores.get("Wisdom") - 10)//2
        ability_mods["Charisma"] = (ability_scores.get("Charisma") - 10)//2
        modifier = False
    
    t.sleep(1.5)
    print("Ability scores:",ability_scores)
    print("Ability modifiers:",ability_mods)
    return ability_scores, ability_mods

def main():
    print("Interesting choice...")
    
if __name__ == '__main__':
    main()
    random_scores()
