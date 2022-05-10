# -*- coding: utf-8 -*-
"""
Created on Wed May  4 18:45:16 2022

@author: Nevermore
"""

import dice as d
import time as t
import d6_roller

# Maybe better to define some class variables?

class Character:
    level = int(input("Character level: "))
    
    def __init__(self, name, level:int,
                 ability_scores={}, ability_mods={},
                 proficiency_bonus=0):
        name = input("Character name: ")
        self.name = name
        return
    
    @classmethod    
    def abilities(cls):
        print("Enter your ability scores:")
        t.sleep(1.2)
        cls.ability_scores = {}
        score = True
        while score:
            score = False
            cls.ability_scores["Strength"] = int(input("Strength: "))
            cls.ability_scores["Dexterity"] = int(input("Dexterity: "))
            cls.ability_scores["Constitution"] = int(input("Constitution: "))
            cls.ability_scores["Intelligence"] = int(input("Intelligence: "))
            cls.ability_scores["Wisdom"] = int(input("Wisdom: "))
            cls.ability_scores["Charisma"] = int(input("Charisma: "))

        cls.ability_mods = {}
        modifier = True
        while modifier:
            modifier = False
            cls.ability_mods["Strength"] = (cls.ability_scores.get("Strength") - 10)//2
            cls.ability_mods["Dexterity"] = (cls.ability_scores.get("Dexterity") - 10)//2
            cls.ability_mods["Constitution"] = (cls.ability_scores.get("Constitution") - 10)//2
            cls.ability_mods["Intelligence"] = (cls.ability_scores.get("Intelligence") - 10)//2
            cls.ability_mods["Wisdom"] = (cls.ability_scores.get("Wisdom") - 10)//2
            cls.ability_mods["Charisma"] = (cls.ability_scores.get("Charisma") - 10)//2
        
        print("Ability scores:",cls.ability_scores)
        print("Ability modifiers:",cls.ability_mods)
        return
    
    @classmethod
    def proficiency(cls):
        if cls.level <=4:
            pb = 2
            return pb
        elif cls.level >=5 and cls.level <=8:
            pb = 3
            return pb
        elif cls.level >=9 and cls.level <=12:
            pb = 4
            return pb
        elif cls.level >=13 and cls.level <=16:
            pb = 5
            return pb
        elif cls.level >=17 and cls.level <=20:
            pb = 6
            return pb
        cls.proficiency_bonus = pb
        
# class Race(Character()):
#     def __init__(self, cls):
        
c1 = Character("name", 0)
c1.abilities()
print("Proficiency bonus:",c1.proficiency())
print(c1.name,"is ready to rock")
# print(c1.ability_mods.get("Strength"))
