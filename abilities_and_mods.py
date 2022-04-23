# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 00:32:22 2022

@author: Nevermore
"""

ability_scores = {}
go = True
while go:
    ability_scores["Strength"] = int(input("Strength: "))
    ability_scores["Dexterity"] = int(input("Dexterity: "))
    ability_scores["Constitution"] = int(input("Constitution: "))
    ability_scores["Intelligence"] = int(input("Intelligence: "))
    ability_scores["Wisdom"] = int(input("Wisdom: "))
    ability_scores["Charisma"] = int(input("Charisma: "))
    go = False

ability_score_mods = {}
modifier = True
while modifier:
    ability_score_mods["Strength"] = (ability_scores.get("Strength") - 10)//2
    ability_score_mods["Dexterity"] = (ability_scores.get("Dexterity") - 10)//2
    ability_score_mods["Constitution"] = (ability_scores.get("Constitution") - 10)//2
    ability_score_mods["Intelligence"] = (ability_scores.get("Intelligence") - 10)//2
    ability_score_mods["Wisdom"] = (ability_scores.get("Wisdom") - 10)//2
    ability_score_mods["Charisma"] = (ability_scores.get("Charisma") - 10)//2
    modifier = False
print(ability_scores)
print(ability_score_mods)