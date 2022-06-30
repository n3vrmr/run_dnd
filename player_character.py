# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 14:18:36 2022

@author: Nevermore
"""

import dice as d
import d6_roller
import time as t
from races import Race
from subraces import Subrace
from classes import Classes
from subclasses import Subclasses
from weapons import Club, Dagger, Greatclub, Handaxe, Javelin, LightHammer
from weapons import Mace, Quarterstaff, Sickle, Spear, LightCrossbow, Dart
from weapons import Shortbow, Sling, Battleaxe, Flail, Glaive, Greataxe
from weapons import Greatsword, Halberd, Lance, Longsword, Maul, Morningstar
from weapons import Pike, Rapier, Scimitar, Shortsword, Trident, WarPick
from weapons import Warhammer, Whip, Blowgun, HandCrossbow, HeavyCrossbow, Longbow

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
        self.set_weapon_proficiencies()
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
        self.char_subclass = Subclasses.choosing_subclass(self)
        self.hp_total = Classes.hitpoints(self)
        self.hp_current = self.hp_total
        Classes.set_class(self)
        Classes.saves(self)
        Classes.skills(self)
        Subclasses.set_subclass(self)
        self.inventory = []
        self.convert_weapon_proficiency()
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
    
    def make_saving_throw(self, ability):
        if ability == "str":
            ability = "Strength"
        elif ability == "dex":
            ability = "Dexterity"
        elif ability == "con":
            ability = "Constitution"
        elif ability == "int":
            ability = "Intelligence"
        elif ability == "wis":
            ability = "Wisdom"
        elif ability == "cha":
            ability = "Charisma"
        print(f"Making {ability} save...")
        self._saving = True
        while self._saving:
            if self.save_proficiencies.get(f"{ability}") == True:
                saving_throw = d.roll(2,20,True,True) + self._ability_mods.get(f"{ability}") + self.proficiency_bonus
            else:
                saving_throw = d.roll(2,20,True,True) + self._ability_mods.get(f"{ability}")
            self._saving = False
        self.saving_throw = saving_throw
        t.sleep(1.2)
        print("Total:", self.saving_throw)
        return self.saving_throw
    
    def make_skill_check(self, skill):
        print(f"Making {skill} check...")
        str_skills = ["athletics"]
        dex_skills = ["acrobatics", "sleight of hand", "stealth"]
        int_skills = ["arcana", "history", "investigation", "nature",
                      "religion"]
        wis_skills = ["animal handling", "insight", "medicine", "perception",
                      "survival"]
        cha_skills = ["deception", "intimidation", "performance", "persuasion"]
        self._check = True
        while self._check:
            if skill in str_skills:
                if self.skill_proficiencies.get(f"{skill}") == True:
                    skill_check = d.roll(2,20,True,True) + self._ability_mods.get("Strength") + self.proficiency_bonus
                elif self.skill_proficiencies.get(f"{skill}") == "expertise":
                    skill_check = d.roll(2,20,True,True) + self._ability_mods.get("Strength") + (self.proficiency_bonus * 2)
                elif self.skill_proficiencies.get(f"{skill}") == "jack":
                    skill_check = d.roll(2,20,True,True) + self._ability_mods.get("Strength") + (self.proficiency_bonus//2)
                else:
                    skill_check = d.roll(2,20,True,True) + self._ability_mods.get("Strength")
            elif skill in dex_skills:
                if self.skill_proficiencies.get(f"{skill}") == True:
                   skill_check = d.roll(2,20,True,True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
                elif self.skill_proficiencies.get(f"{skill}") == "expertise":
                    skill_check = d.roll(2,20,True,True) + self._ability_mods.get("Dexterity") + (self.proficiency_bonus * 2)
                elif self.skill_proficiencies.get(f"{skill}") == "jack":
                    skill_check = d.roll(2,20,True,True) + self._ability_mods.get("Dexterity") + (self.proficiency_bonus//2)
                else:
                    skill_check = d.roll(2,20,True,True) + self._ability_mods.get("Dexterity")
            elif skill in int_skills:
                if self.skill_proficiencies.get(f"{skill}") == True:
                    skill_check = d.roll(2,20,True,True) + self._ability_mods.get("Intelligence") + self.proficiency_bonus
                elif self.skill_proficiencies.get(f"{skill}") == "expertise":
                    skill_check = d.roll(2,20,True,True) + self._ability_mods.get("Intelligence") + (self.proficiency_bonus * 2)
                elif self.skill_proficiencies.get(f"{skill}") == "jack":
                    skill_check = d.roll(2,20,True,True) + self._ability_mods.get("Intelligence") + (self.proficiency_bonus//2)
                else:
                    skill_check = d.roll(2,20,True,True) + self._ability_mods.get("Intelligence")
            elif skill in wis_skills:
                if self.skill_proficiencies.get(f"{skill}") == True:
                    skill_check = d.roll(2,20,True,True) + self._ability_mods.get("Wisdom") + self.proficiency_bonus
                elif self.skill_proficiencies.get(f"{skill}") == "expertise":
                    skill_check = d.roll(2,20,True,True) + self._ability_mods.get("Wisdom") + (self.proficiency_bonus * 2)
                elif self.skill_proficiencies.get(f"{skill}") == "jack":
                    skill_check = d.roll(2,20,True,True) + self._ability_mods.get("Wisdom") + (self.proficiency_bonus//2)
                else:
                    skill_check = d.roll(2,20,True,True) + self._ability_mods.get("Wisdom")
            elif skill in cha_skills:
                if self.skill_proficiencies.get(f"{skill}") == True:
                    skill_check = d.roll(2,20,True,True) + self._ability_mods.get("Charisma") + self.proficiency_bonus
                elif self.skill_proficiencies.get(f"{skill}") == "expertise":
                    skill_check = d.roll(2,20,True,True) + self._ability_mods.get("Charisma") + (self.proficiency_bonus * 2)
                elif self.skill_proficiencies.get(f"{skill}") == "jack":
                    skill_check = d.roll(2,20,True,True) + self._ability_mods.get("Charisma") + (self.proficiency_bonus//2)
                else:
                    skill_check = d.roll(2,20,True,True) + self._ability_mods.get("Charisma")
            self._check = False
        self.skill_check = skill_check
        t.sleep(1.2)
        print("Total:", self.skill_check)
        return self.skill_check
    
    def level_up(self):
        d6 = ["sorcerer", "wizard"]
        d8 = ["bard", "cleric", "druid", "monk", "rogue", "warlock"]
        d10 = ["fighter", "paladin"]
        d12 = ["barbarian"]
        self.level = self.level + 1
        if self.char_class in d6:
            new_hitpoints = self.hp_total + d.roll(1,6) + self._ability_mods.get("Constitution")
            self.hp_total = new_hitpoints
            self.hp_current = self.hp_total
        elif self.char_class in d8:
            new_hitpoints = self.hp_total + d.roll(1,8) + self._ability_mods.get("Constitution")
            self.hp_total = new_hitpoints
            self.hp_current = self.hp_total
        elif self.char_class in d10:
            new_hitpoints = self.hp_total + d.roll(1,10) + self._ability_mods.get("Constitution")
            self.hp_total = new_hitpoints
            self.hp_current = self.hp_total
        elif self.char_class in d12:
            new_hitpoints = self.hp_total + d.roll(1,12) + self._ability_mods.get("Constitution")
            self.hp_total = new_hitpoints
            self.hp_current = self.hp_total
        print("New hitpoint total:", self.hp_total)
        return self.level
    
    def set_weapon_proficiencies(self):
        self.proficiency_simple_weapons = False
        self.proficiency_club = False
        self.proficiency_dagger = False
        self.proficiency_greatclub = False
        self.proficiency_handaxe = False
        self.proficiency_javelin = False
        self.proficiency_light_hammer = False
        self.proficiency_mace = False
        self.proficiency_quarterstaff = False
        self.proficiency_sickle = False
        self.proficiency_spear = False
        self.proficiency_light_xbow = False
        self.proficiency_darts = False
        self.proficiency_shortbow = False
        self.proficiency_sling = False
        self.proficiency_martial_weapons = False
        self.proficiency_battleaxe = False
        self.proficiency_flail = False
        self.proficiency_glaive = False
        self.proficiency_greataxe = False
        self.proficiency_greatsword = False
        self.proficiency_halberd = False
        self.proficiency_lance = False
        self.proficiency_longsword = False
        self.proficiency_maul = False
        self.proficiency_morningstar = False
        self.proficiency_pike = False
        self.proficiency_rapier = False
        self.proficiency_scimitar = False
        self.proficiency_shortsword = False
        self.proficiency_trident = False
        self.proficiency_war_pick = False
        self.proficiency_warhammer = False
        self.proficiency_whip = False
        self.proficiency_blowgun = False
        self.proficiency_hand_xbow = False
        self.proficiency_heavy_xbow = False
        self.proficiency_longbow = False
        return
    
    def convert_weapon_proficiency(self):
        if self.proficiency_simple_weapons == True:
            self.proficiency_club = True
            self.proficiency_dagger = True
            self.proficiency_greatclub = True
            self.proficiency_handaxe = True
            self.proficiency_javelin = True
            self.proficiency_light_hammer = True
            self.proficiency_mace = True
            self.proficiency_quarterstaff = True
            self.proficiency_sickle = True
            self.proficiency_spear = True
            self.proficiency_light_xbow = True
            self.proficiency_darts = True
            self.proficiency_shortbow = True
            self.proficiency_sling = True
        if self.proficiency_martial_weapons == True:
            self.proficiency_battleaxe = True
            self.proficiency_flail = True
            self.proficiency_glaive = True
            self.proficiency_greataxe = True
            self.proficiency_greatsword = True
            self.proficiency_halberd = True
            self.proficiency_lance = True
            self.proficiency_longsword = True
            self.proficiency_maul = True
            self.proficiency_morningstar = True
            self.proficiency_pike = True
            self.proficiency_rapier = True
            self.proficiency_scimitar = True
            self.proficiency_shortsword = True
            self.proficiency_trident = True
            self.proficiency_war_pick = True
            self.proficiency_warhammer = True
            self.proficiency_whip = True
            self.proficiency_blowgun = True
            self.proficiency_hand_xbow = True
            self.proficiency_heavy_xbow = True
            self.proficiency_longbow = True
        return
            

    def add_item(self, item):
        if item == "Club":
            weapon = Club()
            self.inventory.append(weapon)
        elif item == "Dagger":
            weapon = Dagger()
            self.inventory.append(weapon)
        elif item == "Greatclub":
            weapon = Greatclub()
            self.inventory.append(weapon)
        elif item == "Handaxe":
            weapon = Handaxe()
            self.inventory.append(weapon)
        elif item == "Javelin":
            weapon = Javelin()
            self.inventory.append(weapon)
        elif item == "Light hammer":
            weapon = LightHammer()
            self.inventory.append(weapon)
        elif item == "Mace":
            weapon = Mace()
            self.inventory.append(weapon)
        elif item == "Quarterstaff":
            weapon = Quarterstaff()
            self.inventory.append(weapon)
        elif item == "Sickle":
            weapon = Sickle()
            self.inventory.append(weapon)
        elif item == "Spear":
            weapon = Spear()
            self.inventory.append(weapon)
        elif item == "Light crossbow":
            weapon = LightCrossbow()
            self.inventory.append(weapon)
        elif item == "Dart":
            weapon = Dart()
            self.inventory.append(weapon)
        elif item == "Shortbow":
            weapon = Shortbow()
            self.inventory.append(weapon)
        elif item == "Sling":
            weapon = Sling()
            self.inventory.append(weapon)
        elif item == "Battleaxe":
            weapon = Battleaxe()
            self.inventory.append(weapon)
        elif item == "Flail":
            weapon = Flail()
            self.inventory.append(weapon)
        elif item == "Glaive":
            weapon = Glaive()
            self.inventory.append(weapon)
        elif item == "Greataxe":
            weapon = Greataxe()
            self.inventory.append(weapon)
        elif item == "Greatsword":
            weapon = Greatsword()
            self.inventory.append(weapon)
        elif item == "Halberd":
            weapon = Halberd()
            self.inventory.append(weapon)
        elif item == "Lance":
            weapon = Lance()
            self.inventory.append(weapon)
        elif item == "Longsword":
            weapon = Longsword()
            self.inventory.append(weapon)
        elif item == "Maul":
            weapon = Maul()
            self.inventory.append(weapon)
        elif item == "Morningstar":
            weapon = Morningstar()
            self.inventory.append(weapon)
        elif item == "Pike":
            weapon = Pike()
            self.inventory.append(weapon)
        elif item == "Rapier":
            weapon = Rapier()
            self.inventory.append(weapon)
        elif item == "Scimitar":
            weapon = Scimitar()
            self.inventory.append(weapon)
        elif item == "Shortsword":
            weapon = Shortsword()
            self.inventory.append(weapon)
        elif item == "Trident":
            weapon = Trident()
            self.inventory.append(weapon)
        elif item == "War pick":
            weapon = WarPick()
            self.inventory.append(weapon)
        elif item == "Warhammer":
            weapon = Warhammer()
            self.inventory.append(weapon)
        elif item == "Whip":
            weapon = Whip()
            self.inventory.append(weapon)
        elif item == "Blowgun":
            weapon = Blowgun()
            self.inventory.append(weapon)
        elif item == "Hand crossbow":
            weapon = HandCrossbow()
            self.inventory.append(weapon)
        elif item == "Heavy crossbow":
            weapon = HeavyCrossbow()
            self.inventory.append(weapon)
        elif item == "Longbow":
            weapon = Longbow()
            self.inventory.append(weapon)
        return self.inventory
    
    def attack_roll(self, weapon):
        if weapon == "Club":
            if self.proficiency_club == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
            print("Total:",roll)
            return roll
        elif weapon == "Dagger":
            if self.proficiency_dagger == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
            print("Total:",roll)
            return roll
        elif weapon == "Greatclub":
            if self.proficiency_greatclub == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
            print("Total:",roll)
            return roll
        elif weapon == "Handaxe":
            if self.proficiency_handaxe == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
            print("Total:",roll)
            return roll
        elif weapon == "Javelin":
            if self.proficiency_javelin == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
            print("Total:",roll)
            return roll
        elif weapon == "Light hammer":
            if self.proficiency_light_hammer == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
            print("Total:",roll)
            return roll
        elif weapon == "Mace":
            if self.proficiency_mace == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
            print("Total:",roll)
            return roll
        elif weapon == "Quarterstaff":
            if self.proficiency_quarterstaff == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
            print("Total:",roll)
            return roll
        elif weapon == "Sickle":
            if self.proficiency_sickle == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
            print("Total:",roll)
            return roll
        elif weapon == "Spear":
            if self.proficiency_spear == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
            print("Total:",roll)
            return roll
        elif weapon == "Light crossbow":
            if self.proficiency_light_xbow == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
            print("Total:",roll)
            return roll
        elif weapon == "Dart":
            if self.proficiency_darts == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
            print("Total:",roll)
            return roll
        elif weapon == "Shortbow":
            if self.proficiency_shortbow == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
            print("Total:",roll)
            return roll
        elif weapon == "Sling":
            if self.proficiency_sling == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
            print("Total:",roll)
            return roll
        elif weapon == "Battleaxe":
            if self.proficiency_battleaxe == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
            print("Total:",roll)
            return roll
        elif weapon == "Flail":
            if self.proficiency_flail == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
            print("Total:",roll)
            return roll
        elif weapon == "Glaive":
            if self.proficiency_glaive == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
            print("Total:",roll)
            return roll
        elif weapon == "Greataxe":
            if self.proficiency_greataxe == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
            print("Total:",roll)
            return roll
        elif weapon == "Greatsword":
            if self.proficiency_greatsword == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
            print("Total:",roll)
            return roll
        elif weapon == "Halberd":
            if self.proficiency_halberd == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
            print("Total:",roll)
            return roll
        elif weapon == "Lance":
            if self.proficiency_lance == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
            print("Total:",roll)
            return roll
        elif weapon == "Longsword":
            if self.proficiency_longsword == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
            print("Total:",roll)
            return roll
        elif weapon == "Maul":
            if self.proficiency_maul == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
            print("Total:",roll)
            return roll
        elif weapon == "Morningstar":
            if self.proficiency_morningstar == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
            print("Total:",roll)
            return roll
        elif weapon == "Pike":
            if self.proficiency_pike == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
            print("Total:",roll)
            return roll
        elif weapon == "Rapier":
            if self.proficiency_rapier == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
            print("Total:",roll)
            return roll
        elif weapon == "Scimitar":
            if self.proficiency_scimitar == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
            print("Total:",roll)
            return roll
        elif weapon == "Shortsword":
            if self.proficiency_shortsword == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
            print("Total:",roll)
            return roll
        elif weapon == "Trident":
            if self.proficiency_trident == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
            print("Total:",roll)
            return roll
        elif weapon == "War pick":
            if self.proficiency_war_pick == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
            print("Total:",roll)
            return roll
        elif weapon == "Warhammer":
            if self.proficiency_warhammer == True or self.proficiency_martial_weapons == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
            print("Total:",roll)
            return roll
        elif weapon == "Whip":
            if self.proficiency_whip == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
            print("Total:",roll)
            return roll
        elif weapon == "Blowgun":
            if self.proficiency_blowgun == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
            print("Total:",roll)
            return roll
        elif weapon == "Hand crossbow":
            if self.proficiency_hand_xbow == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
            print("Total:",roll)
            return roll
        elif weapon == "Heavy crossbow":
            if self.proficiency_heavy_xbow == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
            print("Total:",roll)
            return roll
        elif weapon == "Longbow":
            if self.proficiency_longbow == True:
                roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
            else:
               roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
            print("Total:",roll)
            return roll
        
    def damage_roll(self, weapon):
        if weapon == "Club":
            dmg = d.roll(1, 4) + self._ability_mods.get("Strength")
            print("Total:",dmg)
            return dmg
        elif weapon == "Dagger":
            dmg = d.roll(1, 4) + self._ability_mods.get("Dexterity")
            print("Total:",dmg)
            return dmg
        elif weapon == "Greatclub":
            dmg = d.roll(1, 8) + self._ability_mods.get("Strength")
            print("Total:",dmg)
            return dmg
        elif weapon == "Handaxe":
            dmg = d.roll(1, 6) + self._ability_mods.get("Strength")
            print("Total:",dmg)
            return dmg
        elif weapon == "Javelin":
            dmg = d.roll(1, 6) + self._ability_mods.get("Strength")
            print("Total:",dmg)
            return dmg
        elif weapon == "Light hammer":
            dmg = d.roll(1, 4) + self._ability_mods.get("Strength")
            print("Total:",dmg)
            return dmg
        elif weapon == "Mace":
            dmg = d.roll(1, 6) + self._ability_mods.get("Strength")
            print("Total:",dmg)
            return dmg
        elif weapon == "Quarterstaff":
            hands = input("One or two hands? ")
            if "1" in hands or "one" in hands:
                dmg = d.roll(1, 6) + self._ability_mods.get("Dexterity")
                print("Total:",dmg)
            elif "2" in hands or "two" in hands:
                dmg = d.roll(1, 8) + self._ability_mods.get("Dexterity")
                print("Total:",dmg)
            return dmg
        elif weapon == "Sickle":
            dmg = d.roll(1, 4) + self._ability_mods.get("Dexterity")
            print("Total:",dmg)
            return dmg
        elif weapon == "Spear":
            hands = input("One or two hands? ")
            if "1" in hands or "one" in hands:
                dmg = d.roll(1, 6) + self._ability_mods.get("Strength")
                print("Total:",dmg)
            elif "2" in hands or "two" in hands:
                dmg = d.roll(1, 8) + self._ability_mods.get("Strength")
                print("Total:",dmg)
            return dmg
        elif weapon == "Light crossbow":
            dmg = d.roll(1, 8) + self._ability_mods.get("Dexterity")
            print("Total:",dmg)
            return dmg
        elif weapon == "Dart":
            dmg = d.roll(1, 4) + self._ability_mods.get("Dexterity")
            print("Total:",dmg)
            return dmg
        elif weapon == "Shortbow":
            dmg = d.roll(1, 8) + self._ability_mods.get("Dexterity")
            print("Total:",dmg)
            return dmg
        elif weapon == "Sling":
            dmg = d.roll(1, 4) + self._ability_mods.get("Dexterity")
            print("Total:",dmg)
            return dmg
        elif weapon == "Battleaxe":
            hands = input("One or two hands? ")
            if "1" in hands or "one" in hands:
                dmg = d.roll(1, 8) + self._ability_mods.get("Strength")
                print("Total:",dmg)
            elif "2" in hands or "two" in hands:
                dmg = d.roll(1, 10) + self._ability_mods.get("Strength")
                print("Total:",dmg)
            return dmg
        elif weapon == "Flail":
            dmg = d.roll(1, 8) + self._ability_mods.get("Strength")
            print("Total:",dmg)
            return dmg
        elif weapon == "Glaive":
            dmg = d.roll(1, 10) + self._ability_mods.get("Strength")
            print("Total:",dmg)
            return dmg
        elif weapon == "Greataxe":
            dmg = d.roll(1, 12) + self._ability_mods.get("Strength")
            print("Total:",dmg)
            return dmg
        elif weapon == "Greatsword":
            dmg = d.roll(2, 6) + self._ability_mods.get("Strength")
            print("Total:",dmg)
            return dmg
        elif weapon == "Halberd":
            dmg = d.roll(1, 10) + self._ability_mods.get("Strength")
            print("Total:",dmg)
            return dmg
        elif weapon == "Lance":
            dmg = d.roll(1, 12) + self._ability_mods.get("Strength")
            print("Total:",dmg)
            return dmg
        elif weapon == "Longsword":
            hands = input("One or two hands? ")
            if "1" in hands or "one" in hands:
                dmg = d.roll(1, 8) + self._ability_mods.get("Strength")
                print("Total:",dmg)
            elif "2" in hands or "two" in hands:
                dmg = d.roll(1, 10) + self._ability_mods.get("Strength")
                print("Total:",dmg)
            return dmg
        elif weapon == "Maul":
            dmg = d.roll(2, 6) + self._ability_mods.get("Strength")
            print("Total:",dmg)
            return dmg
        elif weapon == "Morningstar":
            dmg = d.roll(1, 8) + self._ability_mods.get("Strength")
            print("Total:",dmg)
            return dmg
        elif weapon == "Pike":
            dmg = d.roll(1, 10) + self._ability_mods.get("Strength")
            print("Total:",dmg)
            return dmg
        elif weapon == "Rapier":
            dmg = d.roll(1, 8) + self._ability_mods.get("Dexterity")
            print("Total:",dmg)
            return dmg
        elif weapon == "Scimitar":
            dmg = d.roll(1, 6) + self._ability_mods.get("Dexterity")
            print("Total:",dmg)
            return dmg
        elif weapon == "Shortsword":
            dmg = d.roll(1, 6) + self._ability_mods.get("Dexterity")
            print("Total:",dmg)
            return dmg
        elif weapon == "Trident":
            hands = input("One or two hands? ")
            if "1" in hands or "one" in hands:
                dmg = d.roll(1, 6) + self._ability_mods.get("Strength")
                print("Total:",dmg)
            elif "2" in hands or "two" in hands:
                dmg = d.roll(1, 8) + self._ability_mods.get("Strength")
                print("Total:",dmg)
            return dmg
        elif weapon == "War pick":
            dmg = d.roll(1, 8) + self._ability_mods.get("Strength")
            print("Total:",dmg)
            return dmg
        elif weapon == "Warhammer":
            hands = input("One or two hands? ")
            if "1" in hands or "one" in hands:
                dmg = d.roll(1, 8) + self._ability_mods.get("Strength")
                print("Total:",dmg)
            elif "2" in hands or "two" in hands:
                dmg = d.roll(1, 10) + self._ability_mods.get("Strength")
                print("Total:",dmg)
            return dmg
        elif weapon == "Whip":
            dmg = d.roll(1, 4) + self._ability_mods.get("Dexterity")
            print("Total:",dmg)
            return dmg
        elif weapon == "Blowgun":
            dmg = 1
            print("Total:",dmg)
            return dmg
        elif weapon == "Hand crossbow":
            dmg = d.roll(1, 6) + self._ability_mods.get("Dexterity")
            print("Total:",dmg)
            return dmg
        elif weapon == "Heavy crossbow":
            dmg = d.roll(1, 10) + self._ability_mods.get("Dexterity")
            print("Total:",dmg)
            return dmg
        elif weapon == "Longbow":
            dmg = d.roll(1, 8) + self._ability_mods.get("Dexterity")
            print("Total:",dmg)
            return dmg

def main():
    print("Is it thursday yet?")
    
if __name__ == '__main__':
    main()