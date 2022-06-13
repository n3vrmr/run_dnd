# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 14:18:36 2022

@author: Nevermore
"""

import d6_roller
import time as t
from races import Race
from subraces import Subrace
from classes import Classes

class Player:
    def __init__(self, name):
        self.name = name
        game_control = False
        self.game_control = game_control
        character = self.create_character()
        self.character = character
        return
    
    def create_character(self):
        character = Character("name", 0)
        self.character = character
        return self.character
        
class Character:
    """Create a character in the Dungeons & Dragons 5th Edition format.
    """
    def __init__(self, name, level:int):
        self._name = input("Character name: ")
        self.level = int(input("Character level: "))
        self.save_proficiencies = {"Strength":False, "Dexterity":False,
                                   "Constitution":False, "Intelligence":False,
                                   "Wisdom":False, "Charisma":False}
        self.skill_proficiencies = {"acrobatics":False, "animal handling":False,
                                    "arcana":False, "athletics":False,
                                    "deception":False, "history":False,
                                    "insight":False, "intimidation":False,
                                    "investigation":False, "medicine":False,
                                    "nature":False, "perception":False,
                                    "performance":False, "persuasion":False,
                                    "religion":False, "sleight of hand":False,
                                    "stealth":False, "survival":False}
        self.size = "Medium"
        self.speed = 30
        self.random = input("Generate random? Reply Y for yes or N for no. ").strip().lower()
        if "y" in self.random:
            self.random = True
        elif "n" in self.random:
            self.random = False
        self.abilities()
        self.race = Race.choosing()
        self.languages = Race.languages(self)
        self.no_subrace = ["human", "half elf", "half orc",
                      "tiefling", "goliath"]
        if self.race not in self.no_subrace:
            self.subrace = Subrace.choosing_subrace()
        if self.race in self.no_subrace:
            Race.r_asi(self)
        else:
            Race.r_asi(self)
            Subrace.sr_asi(self)
        Race.race_attributes(self)
        if self.race not in self.no_subrace:
            Subrace.subrace_attributes(self)
        self.proficiency()
        self.char_class = Classes.choosing(self)
        self.char_subclass = Classes.choosing_subclass(self)
        self.hp = Classes.hitpoints(self)
        Classes.set_class(self)
        Classes.saves(self)
        Classes.skills(self)
        return
       
    def abilities(self):
        """
        Allows the player to set their character's ability scores manually,
        or randomly rolls for each ability score individually. After
        determining each score, prints the dictionary.
               
        Returns
        -------
        ability_scores: A dictionary with the name of each ability score as a 
        key, and integers as their correpsonding values.
        
        """
        if self.random == True:
            self.ability_scores = {}
            score = True
            while score:
                score = False
                self.ability_scores["Strength"] = d6_roller.ability_rolls()
                self.ability_scores["Dexterity"] = d6_roller.ability_rolls()
                self.ability_scores["Constitution"] = d6_roller.ability_rolls()
                self.ability_scores["Intelligence"] = d6_roller.ability_rolls()
                self.ability_scores["Wisdom"] = d6_roller.ability_rolls()
                self.ability_scores["Charisma"] = d6_roller.ability_rolls()
            t.sleep(1.5)
        
        else:
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
        return self.ability_scores
    
    def ability_modifiers(self):
        """
        Calculates each ability score modifier based on the values of the
        corresponding ability scores. The way this is is done is as described
        in the Dungeons & Dragons 5th Edition Player's Handbook:
            (ability score - 10), divided by two and rounded down.
        After determining each of the modifiers, it prints the dictionary.

        Returns
        -------
        ability_mods: A dictionary with the name of each ability score modifier
        as a key, and integers as their correpsonding values.

        """
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
            print("Ability modifiers:",self._ability_mods)
        return self._ability_mods
    
    def increase_one_score(self):
        """
        Method for increasing one of your ability scores by 2 points,
        based on player choice.
        
        Returns
        -------
        Updated ability_scores and ability_mods dictionaries.
        """
        choice = input("Choose an ability score to increase by 2: ").strip().lower()
        if "str" in choice:
            self.ability_scores["Strength"] = self.ability_scores.get("Strength") + 2
        elif "dex" in choice:
            self.ability_scores["Dexterity"] = self.ability_scores.get("Dexterity") + 2
        elif "con" in choice:
            self.ability_scores["Constitution"] = self.ability_scores.get("Constitution") + 2
        elif "int" in choice:
            self.ability_scores["Intelligence"] = self.ability_scores.get("Intelligence") + 2
        elif "wis" in choice:
            self.ability_scores["Wisdom"] = self.ability_scores.get("Wisdom") + 2
        elif "cha" in choice:
            self.ability_scores["Charisma"] = self.ability_scores.get("Charisma") + 2
        print("Ability scores:",self.ability_scores)
        self.ability_modifiers()
        return self.ability_scores
    
    def increase_two_scores(self):
        """
        Method for increasing two of your ability scores by 1 point,
        based on player choice.
        
        Returns
        -------
        Updated ability_scores and ability_mods dictionaries.
        """
        choice = input("Choose two ability scores to increase by 1: ").strip().lower()
        if "str" in choice:
            self.ability_scores["Strength"] = self.ability_scores.get("Strength") + 1
        if "dex" in choice:
            self.ability_scores["Dexterity"] = self.ability_scores.get("Dexterity") + 1
        if "con" in choice:
            self.ability_scores["Constitution"] = self.ability_scores.get("Constitution") + 1
        if "int" in choice:
            self.ability_scores["Intelligence"] = self.ability_scores.get("Intelligence") + 1
        if "wis" in choice:
            self.ability_scores["Wisdom"] = self.ability_scores.get("Wisdom") + 1
        if "cha" in choice:
            self.ability_scores["Charisma"] = self.ability_scores.get("Charisma") + 1
        print("Ability scores:",self.ability_scores)
        self.ability_modifiers()
        return self.ability_scores
        
    def proficiency(self):
        """
        Defines your character's proficiency bonus based on their level.
        
        Returns
        -------
        self.ability_scores: a dictionary with your character's abilities as
        the keys, and the scores as the associated values.
        
        """
        if self.level <=4:
            pb = 2
        elif self.level >=5 and self.level <=8:
            pb = 3
        elif self.level >=9 and self.level <=12:
            pb = 4
        elif self.level >=13 and self.level <=16:
            pb = 5
        elif self.level >=17 and self.level <=20:
            pb = 6
        self.proficiency_bonus = pb
        return self.proficiency_bonus
    
    def gain_skill_proficiency(self):
        player_choice = input("Choose skill proficiencies: ")
        if "acrobatics" in player_choice:
            self.skill_proficiencies["acrobatics"] = True
        if "animal handling" in player_choice:
            self.skill_proficiencies["animal handling"] = True
        if "arcana" in player_choice:
            self.skill_proficiencies["arcana"] = True
        if "athletics" in player_choice:
            self.skill_proficiencies["athletics"] = True
        if "deception" in player_choice:
            self.skill_proficiencies["deception"] = True
        if "history" in player_choice:
            self.skill_proficiencies["history"] = True
        if "insight" in player_choice:
            self.skill_proficiencies["insight"] = True
        if "intimidation" in player_choice:
            self.skill_proficiencies["intimidation"] = True
        if "investigation" in player_choice:
            self.skill_proficiencies["investigation"] = True
        if "medicine" in player_choice:
            self.skill_proficiencies["medicine"] = True
        if "nature" in player_choice:
            self.skill_proficiencies["nature"] = True
        if "perception" in player_choice:
            self.skill_proficiencies["perception"] = True
        if "performance" in player_choice:
            self.skill_proficiencies["performance"] = True
        if "persuasion" in player_choice:
            self.skill_proficiencies["persuasion"] = True
        if "religion" in player_choice:
            self.skill_proficiencies["religion"] = True
        if "sleight of hand" in player_choice:
            self.skill_proficiencies["sleight of hand"] = True
        if "stealth" in player_choice:
            self.skill_proficiencies["stealth"] = True
        if "survival" in player_choice:
            self.skill_proficiencies["survival"] = True
        return self.skill_proficiencies