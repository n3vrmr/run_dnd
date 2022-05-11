# -*- coding: utf-8 -*-
"""
Created on Wed May  4 18:45:16 2022

@author: Nevermore
"""

import dice as d
import time as t
import d6_roller

class Character:
    def __init__(self, name, level:int,
                 ability_scores={}, ability_mods={},
                 proficiency_bonus=0):
        name = input("Character name: ")
        self.name = name
        level = int(input("Character level: "))
        self.level = level
        return
       
    def abilities(self):
        print("Enter your ability scores:")
        t.sleep(1.2)
        self.ability_scores = {}
        score = True
        while score:
            score = False
            self.ability_scores["Strength"] = int(input("Strength: "))
            self.ability_scores["Dexterity"] = int(input("Dexterity: "))
            self.ability_scores["Constitution"] = int(input("Constitution: "))
            self.ability_scores["Intelligence"] = int(input("Intelligence: "))
            self.ability_scores["Wisdom"] = int(input("Wisdom: "))
            self.ability_scores["Charisma"] = int(input("Charisma: "))

        self.ability_mods = {}
        modifier = True
        while modifier:
            modifier = False
            self.ability_mods["Strength"] = (self.ability_scores.get("Strength") - 10)//2
            self.ability_mods["Dexterity"] = (self.ability_scores.get("Dexterity") - 10)//2
            self.ability_mods["Constitution"] = (self.ability_scores.get("Constitution") - 10)//2
            self.ability_mods["Intelligence"] = (self.ability_scores.get("Intelligence") - 10)//2
            self.ability_mods["Wisdom"] = (self.ability_scores.get("Wisdom") - 10)//2
            self.ability_mods["Charisma"] = (self.ability_scores.get("Charisma") - 10)//2
        
        print("Ability scores:",self.ability_scores)
        print("Ability modifiers:",self.ability_mods)
        return
    
    def proficiency(self):
        if self.level <=4:
            pb = 2
            return pb
        elif self.level >=5 and self.level <=8:
            pb = 3
            return pb
        elif self.level >=9 and self.level <=12:
            pb = 4
            return pb
        elif self.level >=13 and self.level <=16:
            pb = 5
            return pb
        elif self.level >=17 and self.level <=20:
            pb = 6
            return pb
        self.proficiency_bonus = pb
        
# class Race(Character()):
#     def __init__(self, cls):
        
c1 = Character("name", 0)
c1.abilities()
c2 = Character("name", 0)
c2.abilities()

if c2.ability_scores.get("Intelligence") < 10:
    print(f"{c2.name} is not very smart...")
print("Proficiency bonus:",c1.proficiency())
print(c1.name,"is ready to rock")
# print(c1.ability_mods.get("Strength"))
