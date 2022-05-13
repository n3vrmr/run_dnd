# -*- coding: utf-8 -*-
"""
Created on Wed May  4 18:45:16 2022

@author: Nevermore
"""

import dice as d
import time as t
import d6_roller

class Character:
    """Create a character in the Dungeons & Dragons 5th Edition format.
    """
    def __init__(self, name, level:int, random=False,
                 ability_scores={}, _ability_mods={},
                 proficiency_bonus=0):
        """Sets the initial state for a new character.
        """
        name = input("Character name: ")
        self._name = name
        level = int(input("Character level: "))
        self.level = level
        random = input("Generate random? Reply Y for yes or N for no. ").strip().lower()
        self.random = random
        if "y" in self.random:
            self.random = True
        elif "n" in self.random:
            self.random = False
        return
       
    def abilities(self):
        """Allows the player to set their character's ability scores manually,
        then defines the respective ability modifiers according to those values.
        The way the ability modifiers are calculated is as described in the Player's Handbook:
        (ability score - 10), divided by 2 and rounded down.
        """
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

        self._ability_mods = {}
        modifier = True
        while modifier:
            modifier = False
            self._ability_mods["Strength"] = (self.ability_scores.get("Strength") - 10)//2
            self._ability_mods["Dexterity"] = (self.ability_scores.get("Dexterity") - 10)//2
            self._ability_mods["Constitution"] = (self.ability_scores.get("Constitution") - 10)//2
            self._ability_mods["Intelligence"] = (self.ability_scores.get("Intelligence") - 10)//2
            self._ability_mods["Wisdom"] = (self.ability_scores.get("Wisdom") - 10)//2
            self._ability_mods["Charisma"] = (self.ability_scores.get("Charisma") - 10)//2
        
        print("Ability scores:",self.ability_scores)
        print("Ability modifiers:",self._ability_mods)
        return
    
    def random_scores(self):
        """Randomizes your character's ability scores.
        Hope you're feeling lucky!
        """
        self.ability_scores = {}
        score = True
        while score:
            self.ability_scores["Strength"] = d6_roller.ability_rolls()
            self.ability_scores["Dexterity"] = d6_roller.ability_rolls()
            self.ability_scores["Constitution"] = d6_roller.ability_rolls()
            self.ability_scores["Intelligence"] = d6_roller.ability_rolls()
            self.ability_scores["Wisdom"] = d6_roller.ability_rolls()
            self.ability_scores["Charisma"] = d6_roller.ability_rolls()
            score = False
            
        self._ability_mods = {}
        modifier = True
        while modifier:
            self._ability_mods["Strength"] = (self.ability_scores.get("Strength") - 10)//2
            self._ability_mods["Dexterity"] = (self.ability_scores.get("Dexterity") - 10)//2
            self._ability_mods["Constitution"] = (self.ability_scores.get("Constitution") - 10)//2
            self._ability_mods["Intelligence"] = (self.ability_scores.get("Intelligence") - 10)//2
            self._ability_mods["Wisdom"] = (self.ability_scores.get("Wisdom") - 10)//2
            self._ability_mods["Charisma"] = (self.ability_scores.get("Charisma") - 10)//2
            modifier = False
        
        t.sleep(1.5)
        print("Ability scores:",self.ability_scores)
        print("Ability modifiers:",self._ability_mods)
        return
    
    def proficiency(self):
        """Defines your character's proficiency bonus based on their level.
        """
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
if c1.random == True:
    c1.random_scores()
else:
    c1.abilities()
    
c2 = Character("name", 0)
if c2.random == True:
    c2.random_scores()
else:
    c2.abilities()

if c2.ability_scores.get("Intelligence") < 10:
    print(f"{c2._name} is not very smart...")
    
print("Proficiency bonus:",c1.proficiency())
print(c1._name,"is ready to rock")
# print(c1._ability_mods.get("Strength"))
