# -*- coding: utf-8 -*-
"""
Created on Wed May  4 18:45:16 2022

@author: Nevermore
"""

import dice as d

class Character:
    def __init__(self, Name, Level,
                 ability_scores, ability_mods,
                 proficiency_bonus, death_saves):
        self.Name = input("Character name: ")
        self.Level = input("Character level: ")
        self.ability_scores = {}
        score = True
        while score:
            score = False
            ability_scores["Strength"] = int(input("Strength: "))
            ability_scores["Dexterity"] = int(input("Dexterity: "))
            ability_scores["Constitution"] = int(input("Constitution: "))
            ability_scores["Intelligence"] = int(input("Intelligence: "))
            ability_scores["Wisdom"] = int(input("Wisdom: "))
            ability_scores["Charisma"] = int(input("Charisma: "))
        self.ability_mods = {}
        modifier = True
        while modifier:
            modifier = False
            ability_mods["Strength"] = (ability_scores.get("Strength") - 10)//2
            ability_mods["Dexterity"] = (ability_scores.get("Dexterity") - 10)//2
            ability_mods["Constitution"] = (ability_scores.get("Constitution") - 10)//2
            ability_mods["Intelligence"] = (ability_scores.get("Intelligence") - 10)//2
            ability_mods["Wisdom"] = (ability_scores.get("Wisdom") - 10)//2
            ability_mods["Charisma"] = (ability_scores.get("Charisma") - 10)//2
        if self.Level <=4:
            pb = 2
            return pb
        elif self.Level >=5 and self.Level <=8:
            pb = 3
            return pb
        elif self.Level >=9 and self.Level <=12:
            pb = 4
            return pb
        elif self.Level >=13 and self.Level <=16:
            pb = 5
            return pb
        elif self.Level >=17 and self.Level <=20:
            pb = 6
            return 6
        self.proficiency_bonus = pb       