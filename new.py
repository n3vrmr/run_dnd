# -*- coding: utf-8 -*-
"""
Created on Wed May  4 18:45:16 2022

@author: Nevermore
"""

import dice as d
import time as t
import d6_roller

class Campaign:
    def __init__(self):
        self.add_players()
        self.set_dm()
        return
    
    def add_players(self):
        players = []
        self.players = players
        print("Add a player to your campaign:")
        t.sleep(1.5)
        add = True
        while add:
            name = input("Enter the player name: ")
            self.name = name
            add = False
            player = Player(f"{self.name}")
            self.players.append(player)
            cont = input("Add another player? ").lower().strip()
            if "y" in cont:
                add = True
            else:
                add = False
        for i in range(0,len(self.players)):
            print(f"{self.players[i].name} has joined the campaign!")
        return self.players
    
    def set_dm(self):
        select_player = input("Who will be the Dungeon Master for this Campaign? ")
        for self.player in self.players:
            if select_player == self.player:
                self.player = DungeonMaster
                print(f"{select_player} will be the DM.")
            # else:
            #     t.sleep(1.2)
            #     print("Players, create your characters: ")
            #     t.sleep(1.2)
            #     Player.create_character(self)
        return self.players
    
    def player_characters(self):
        pass

class DungeonMaster:
    def __init__(self):
        game_control = True
        self.game_control = game_control
        return
    
    def weather_set(self, condition):
        pass
    
    def ambient_set(self):
        pass
    
    def time_set(self):
        pass
    
    def override_sunlight(self):
        pass
    
    def visibility_set(self):
        pass
    
    def create_npc(self):
        pass
    
    def create_initiative(self):
        pass
    
    def add_to_initiative(self):
        pass
    
    def remove_from_initiative(self):
        pass

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
    def __init__(self, name, level:int, random=False,
                 ability_scores={}, _ability_mods={},
                 proficiency_bonus=0):
        """Sets the initial state for a new character.
        """
        name = input("Character name: ")
        self._name = name
        level = int(input("Character level: "))
        self.level = level
        languages = []
        self.languages = languages
        size = "Medium"
        self.size = size
        speed = 30
        self.speed = speed
        random = input("Generate random? Reply Y for yes or N for no. ").strip().lower()
        self.random = random
        if "y" in self.random:
            self.random = True
        elif "n" in self.random:
            self.random = False
        r = Race.choosing()
        self.race = r
        if "human" not in self.race:
            sr = Race.choosing_subrace()
            self.subrace = sr
        advantage = False
        self.advantage = advantage
        disadvantage = False
        self.disadvantage = disadvantage
        self.abilities()
        if "human" in self.race:
            self.r_asi()
        else:
            self.r_asi()
            self.sr_asi()
        self.race_attributes()
        if "human" not in self.race:
            self.subrace_attributes()
        return
       
    def abilities(self):
        """Allows the player to set their character's ability scores manually,
        then defines the respective ability modifiers according to those values.
        The way the ability modifiers are calculated is as described in the Player's Handbook:
        (ability score - 10), divided by 2 and rounded down.
        In case you chose to generate a random character, the ability scores will be decided for you instead.
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
        TYPE
            DESCRIPTION.
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
        TYPE
            DESCRIPTION.
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
        self.proficiency_bonus = pb
        return pb
        
    def adv_dis(self):
        """
        Make a roll with either advantage or disadvantage.
        If you have both advantage and disadvantage, they cancel out.
        Advantage and disadvantage do not stack.
        Returns
        -------
        game_situation : the highest roll for advantage and the lowest
        roll for disadvantage.
        """
        if self.advantage == True:
            rolls = d.roll(2,20,True)
            game_situation = max(rolls)
            print("Rolling with advantage:",game_situation)
            if 20 in rolls:
                print("\033[1;32;40mNatural twenty! Critical success!\033[0m")
        elif self.disadvantage == True:
            rolls = d.roll(2,20,True)
            game_situation = min(rolls)
            print("Rolling with disadvantage:",game_situation)
            if 1 in rolls:
                print("\033[1;31;47mUh-oh, natural one! Critical fail!\033[0m")
        elif self.advantage == True and self.disadvantage == True:
            self.advantage == False
            self.disadvantage == False
        return game_situation
        
    def r_asi(self):
        if "dwarf" in self.race:
            r = Dwarf
            self.r = r
            Dwarf.dwarf_asi(self)
        elif "elf" in self.race:
            r = Elf
            self.r = r
            Elf.elf_asi(self)
        elif "halfling" in self.race:
            r = Halfling
            self.r = r
            Halfling.halfling_asi(self)
        elif "human" in self.race:
            r = Human
            self.r = r
            Human.human_asi(self)
        elif "dragonborn" in self.race:
            r = Dragonborn
            self.r = r
            Dragonborn.dragonborn_asi(self)
        elif "gnome" in self.race:
            r = Gnome
            self.r = r
            Gnome.gnome_asi(self)
        elif "half elf" in self.race:
            r = HalfElf
            self.r = r
            HalfElf.half_elf_asi(self)
            self.increase_two_scores()
        elif "halforc" in self.race or "half-orc" in self.race:
            self.ability_scores["Strength"] = self.ability_scores.get("Strength") + 2
            self.ability_scores["Constitution"] = self.ability_scores.get("Constitution") + 1
        elif "tiefling" in self.race:
            self.ability_scores["Intelligence"] = self.ability_scores.get("Intelligence") + 1
            self.ability_scores["Charisma"] = self.ability_scores.get("Charisma") + 2
        elif "aasimar" in self.race:
            self.ability_scores["Charisma"] = self.ability_scores.get("Charisma") + 2
        elif "goliath" in self.race:
            self.ability_scores["Strength"] = self.ability_scores.get("Strength") + 2
            self.ability_scores["Constitution"] = self.ability_scores.get("Constitution") + 1
        if "human" in self.race:
            print("Ability scores:",self.ability_scores)
            self.ability_modifiers()
            return self.ability_scores
        else:
            return self.ability_scores
    
    def sr_asi(self):
        if "hill dwarf" in self.subrace:
            sr = HillDwarf
            self.sr = sr
            HillDwarf.hdwarf_asi(self)
        elif "mountain dwarf" in self.subrace:
            sr = MountainDwarf
            self.sr = sr
            MountainDwarf.mdwarf_asi(self)
        elif "high elf" in self.subrace:
            sr = HighElf
            self.sr = sr
            HighElf.helf_asi(self)
        elif "wood elf" in self.subrace:
            sr = WoodElf
            self.sr = sr
            WoodElf.welf_asi(self)
        elif "drow" in self.subrace:
            sr = Drow
            self.sr = sr
            Drow.drow_asi(self)
        print("Ability scores:",self.ability_scores)
        self.ability_modifiers()
        return self.ability_scores
    
    def race_attributes(self):
        if "dwarf" in self.race:
            Dwarf.languages(self)
            Dwarf.darkvision(self)
            Dwarf.speed(self)
            Dwarf.dwarven_combat_training(self)
            Dwarf.dwarven_resilience(self)
        elif "elf" in self.race:
            Elf.languages(self)
            Elf.darkvision(self)
            Elf.keen_senses(self)
            Elf.fey_ancestry(self)
            Elf.trance(self)
    
    def subrace_attributes(self):
        if "hill dwarf" in self.subrace:
            HillDwarf.dwarven_toughness(self)
        elif "mountain dwarf" in self.subrace:
            MountainDwarf.dwarven_armor_training(self)
        elif "high elf" in self.subrace:
            HighElf.extra_language(self)
            HighElf.elf_weapon_training(self)
            HighElf.cantrip(self)
        elif "wood elf" in self.subrace:
            WoodElf.fleet_of_foot(self)
            WoodElf.elf_weapon_training(self)
            WoodElf.mask_of_the_wild(self)
            WoodElf.speed(self)
        elif "drow" in self.subrace:
            Drow.superior_darkvision(self)
            Drow.sunlight_sensitivity(self)
            Drow.drow_weapon_training(self)
            Drow.drow_magic(self)
    
    def unarmed_attack(self):
        to_hit = d.roll(1, 20) + self._ability_mods.get("Strength")
        if to_hit >= 0:
            hit = True
        else:
            hit = False
        if hit:
            print(f"{self._name} rolled {to_hit} to hit")
            damage = d.roll(1, 4) + self._ability_mods.get("Strength")
        print(f"{damage} points of bludgeoning damage")
        return damage
    
class Race:
    def __init__(self, r_asi=True):
        self.race = self.choosing()
        self.subrace = self.choosing_subrace()
        return self.race
    
    def choosing():
        race = input("Choose your character's race: ").lower().strip()
        return race
        
    def choosing_subrace():
        subrace = input("Choose your character's subrace: ").lower().strip()
        return subrace
            
class Dwarf:
    def __init__(self):
        self.languages = []
        return
    
    def speed(self):
        speed = 25
        self.speed = speed
        return self.speed
    
    def size(self):
        size = "Medium"
        self.size = size
        return self.size
    
    def darkvision(self):
        darkvision = [True,60]
        self.darkvision = darkvision
        return self.darkvision
    
    def dwarven_resilience(self):
        dwarven_resilience = True
        self.dwarven_resilience = dwarven_resilience
        return self.dwarven_resilience
    
    def dwarven_combat_training(self):
        dwarven_combat_training = True
        self.dwarven_combat_training = dwarven_combat_training
        return self.dwarven_combat_training
        
    def languages(self):
        languages = ["Common","Dwarvish"]
        self.languages = languages
        return self.languages
    
    def dwarf_asi(self):
        if "dwarf" in self.race:
            self.ability_scores["Constitution"] = self.ability_scores.get("Constitution") + 2
        return self.ability_scores
    
class HillDwarf(Dwarf):
    def dwarven_toughness(self):
        dwarven_toughness = True
        self.dwarven_toughness = dwarven_toughness
        return self.dwarven_toughness
    
    def hdwarf_asi(self):
        if "hill dwarf" in self.subrace:
            self.ability_scores["Wisdom"] = self.ability_scores.get("Wisdom") + 1
        return self.ability_scores
            
class MountainDwarf(Dwarf):
    def dwarven_armor_training(self):
        dwarven_armor_training = True
        self.dwarven_armor_training = dwarven_armor_training
        return self.dwarven_armor_training
    
    def mdwarf_asi(self):
        if "mountain dwarf" in self.subrace:
            self.ability_scores["Strength"] = self.ability_scores.get("Strength") + 2
        return self.ability_scores
        
class Elf:
    def __init__(self):
        self.languages = []
        return
    
    def speed(self):
        speed = 30
        self.speed = speed
        return self.speed
    
    def size(self):
        size = "Medium"
        self.size = size
        return self.size
    
    def darkvision(self):
        darkvision = [True,60]
        self.darkvision = darkvision
        return self.darkvision
    
    def keen_senses(self):
        keen_senses = True
        self.keen_senses = keen_senses
        return self.keen_senses
    
    def fey_ancestry(self):
        fey_ancestry = True
        self.fey_ancestry = fey_ancestry
        return self.fey_ancestry
    
    def trance(self):
        trance = True
        self.trance = trance
        return self.trance
    
    def languages(self):
        languages = ["Common","Elvish"]
        self.languages = languages
        return self.languages
    
    def elf_asi(self):
        if "elf" in self.race:
            self.ability_scores["Dexterity"] = self.ability_scores.get("Dexterity") + 2
        return self.ability_scores
            
class HighElf(Elf):    
    def elf_weapon_training(self):
        elf_weapon_training = True
        self.elf_weapon_training = elf_weapon_training
        return self.elf_weapon_training
    
    def cantrip(self):
        cantrip = True
        self.cantrip = cantrip
        return self.cantrip
    
    def extra_language(self):
        extra_language = input("Choose another language: ")
        self.languages.append(extra_language)
        text = f"{self._name} can speak the following languages: {self.languages}"
        print(text)
        return self.languages
    
    def helf_asi(self):
        if "high elf" in self.subrace:
            self.ability_scores["Intelligence"] = self.ability_scores.get("Intelligence") + 1
        return self.ability_scores
    
class WoodElf(Elf):
    def __init__(self):
        self.elf_weapon_training = True
        self.fleet_of_foot()
        self.mask_of_the_wild = True
        return
    
    def elf_weapon_training(self):
        elf_weapon_training = True
        self.elf_weapon_training = elf_weapon_training
        return self.elf_weapon_training
    
    def fleet_of_foot(self):
        speed = 35
        self.speed = speed
        return self.speed
    
    def mask_of_the_wild(self):
        mask_of_the_wild = True
        self.mask_of_the_wild = mask_of_the_wild
        return self.mask_of_the_wild
    
    def welf_asi(self):
        if "wood elf" in self.subrace:
            self.ability_scores["Wisdom"] = self.ability_scores.get("Wisdom") + 1
        return self.ability_scores
    
class Drow(Elf):
    def __init__(self):
        self.darkvision = self.superior_darkvision()
        self.sunlight_sensitivity = True
        self.drow_magic = True
        self.drow_weapon_training = True
        return
    
    def superior_darkvision(self):
        darkvision = [True,120]
        self.darkvision = darkvision
        return self.darkvision
    
    def sunlight_sensitivity(self):
        sunlight_sensitivity = True
        self.sunlight_sensitivity = sunlight_sensitivity
        return self.sunlight_sensitivity
    
    def drow_magic(self):
        drow_magic = True
        self.drow_magic = drow_magic
        return self.drow_magic
    
    def drow_weapon_training(self):
        drow_weapon_training = True
        self.drow_weapon_training = drow_weapon_training
        return self.drow_weapon_training
    
    def drow_asi(self):
        if "drow" in self.subrace:
            self.ability_scores["Charisma"] = self.ability_scores.get("Charisma") + 1
        return self.ability_scores

class Halfling:
    def __init__(self):
        self.languages = []
        return
    
    def halfling_asi(self):
        if "halfling" in self.race:
            self.ability_scores["Dexterity"] = self.ability_scores.get("Dexterity") + 2
        return self.ability_scores
    
class Human:
    def __init__(self):
        self.languages = []
        return
        
    def human_asi(self):
        if "human" in self.race:
            self.ability_scores["Strength"] = self.ability_scores.get("Strength") + 1
            self.ability_scores["Dexterity"] = self.ability_scores.get("Dexterity") + 1
            self.ability_scores["Constitution"] = self.ability_scores.get("Constitution") + 1
            self.ability_scores["Intelligence"] = self.ability_scores.get("Intelligence") + 1
            self.ability_scores["Wisdom"] = self.ability_scores.get("Wisdom") + 1
            self.ability_scores["Charisma"] = self.ability_scores.get("Charisma") + 1
        return self.ability_scores
        
class Dragonborn:
    def __init__(self):
        self.languages = []
        return
    
    def dragonborn_asi(self):
        if "dragonborn" in self.race:
            self.ability_scores["Strength"] = self.ability_scores.get("Strength") + 2
            self.ability_scores["Charisma"] = self.ability_scores.get("Charisma") + 1
        return self.ability_scores

class Gnome:
    def __init__(self):
        self.languages = []
        return

    def gnome_asi(self):
        if "gnome" in self.race:
            self.ability_scores["Intelligence"] = self.ability_scores.get("Intelligence") + 2
        return self.ability_scores
    
class HalfElf:
    def __init__(self):
        self.languages = []
        return
    
    def half_elf_asi(self):
        if "half elf" in self.race:
            self.ability_scores["Charisma"] = self.ability_scores.get("Charisma") + 2
        return self.ability_scores
        
c=Campaign()

def main():
    print("Not affiliated with Wizards of the Coast LLC")

if __name__ == '__main__':
    main()