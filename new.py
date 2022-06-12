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
        dm = DungeonMaster()
        self.dm = dm
        self.add_players()
        return
    
    def add_players(self):
        players = []
        self.players = players
        t.sleep(1.5)
        print("Add a player to your campaign")
        t.sleep(1.5)
        add = True
        while add:
            add = False
            name = input("Enter the player name: ")
            player = Player(f"{name}")
            self.players.append(player)
            cont = input("Add another player? ").lower().strip()
            if "y" in cont:
                add = True
            else:
                add = False
        for i in range(0,len(self.players)):
            print(f"{self.players[i].name} has joined the campaign as {self.players[i].character._name}, a {self.players[i].character.race} {self.players[i].character.char_class}!")
        return self.players
            
            # else:
            #     t.sleep(1.2)
            #     print("Players, create your characters: ")
            #     t.sleep(1.2)
            #     Player.create_character(self)
    
    def player_characters(self):
        pass

class DungeonMaster:
    def __init__(self):
        game_control = True
        self.game_control = game_control
        self.dm = self.set_dm()
        return
    
    def set_dm(self):
        dm = input("Who will be the Dungeon Master for this Campaign? ")
        self.dm = dm
        print(f"{self.dm} will be the DM.")
        return self.dm
    
    def weather_set(self, weather):
        self.weather = weather
        text = f"It is {self.weather} at the moment."
        print(text)
        return self.weather
    
    def ambient_set(self, environment):
        self.environment = environment
        vowels = ["a", "e", "i", "o", "u"]
        split = list(self.environment)
        if split[0] in vowels:
            text = f"You are at an {self.environment}."
        else:
            text = f"You are at a {self.environment}"
        print(text)
        closed_spaces = ["cave", "tavern"]
        if self.environment in closed_spaces:
            self.override_sunlight(False)
        return self.environment
    
    def time_set(self, time):
        self.time = time
        text = f"The time of day is {self.time}"
        print(text)
        convert = int(self.time.replace(":", ""))
        if convert >= 600 and convert <= 1800:
            self.override_sunlight(True)
        else:
            self.override_sunlight(False)
        return self.time
    
    def check_sunlight(self):
        if self.sunlight == True:
            text = "The light of day is shining."
        else:
            text = "There is no daylight to be seen."
        print(text)
        return self.sunlight
    
    def override_sunlight(self, sunlight:bool):
        self.sunlight = sunlight
        self.check_sunlight()
        return self.sunlight
    
    def visibility_set(self):
        pass
    
    def create_npc(self):
        npcs = []
        self.npcs = npcs
        print("Add an NPC to your campaign")
        t.sleep(1.5)
        add = True
        while add:
            add = False
            name = input("Enter the NPC name: ")
            self.name = name
            npc = Character(f"{name}", 0)
            self.npcs.append(npc)
            cont = input("Add another NPC? ").lower().strip()
            if "y" in cont:
                add = True
            else:
                add = False
        return self.npcs
    
    def create_initiative(self):
        pass
    
    def add_to_initiative(self):
        pass
    
    def remove_from_initiative(self):
        pass
    
    def end_initiative(self):
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
    def __init__(self, name, level:int):
        self._name = input("Character name: ")
        self.level = int(input("Character level: "))
        self.languages = []
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
        self.no_subrace = ["human", "half elf", "half orc",
                      "tiefling", "goliath"]
        if self.race not in self.no_subrace:
            self.subrace = Race.choosing_subrace()
        if self.race in self.no_subrace:
            Race.r_asi(self)
        else:
            Race.r_asi(self)
            Race.sr_asi(self)
        Race.race_attributes(self)
        if self.race not in self.no_subrace:
            Race.subrace_attributes(self)
        self.proficiency()
        self.char_class = Classes.choosing(self)
        self.char_subclass = Classes.choosing_subclass(self)
        self.hp = Classes.hitpoints(self)
        Classes.saving_throws(self)
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
    
    def r_asi(self):
        """
        Calculates the ability score increase based on the race chosen by the
        player.

        Returns
        -------
        Updated ability_scores and ability_mods dictionaries.

        """
        if self.race == "dwarf":
            self.r = Dwarf
            Dwarf.dwarf_asi(self)
        elif self.race == "elf":
            self.r = Elf
            Elf.elf_asi(self)
        elif self.race == "halfling":
            self.r = Halfling
            Halfling.halfling_asi(self)
        elif self.race == "human":
            self.r = Human
            Human.human_asi(self)
        elif self.race == "dragonborn":
            self.r = Dragonborn
            Dragonborn.dragonborn_asi(self)
        elif self.race == "gnome":
            self.r = Gnome
            Gnome.gnome_asi(self)
        elif self.race == "half elf":
            self.r = HalfElf
            HalfElf.half_elf_asi(self)
            self.increase_two_scores()
        elif self.race == "half orc":
            self.r = HalfOrc
            HalfOrc.half_orc_asi(self)
        elif self.race == "tiefling":
            self.r = Tiefling
            Tiefling.tiefling_asi(self)
        elif self.race == "aasimar":
            self.r = Aasimar
            Aasimar.aasimar_asi(self)
        elif self.race == "goliath":
            self.r = Goliath
            Goliath.goliath_asi(self)
        if self.race in self.no_subrace and self.race != "half elf":
            print("Ability scores:",self.ability_scores)
            self.ability_modifiers()
            return self.ability_scores
        else:
            return self.ability_scores
    
    def sr_asi(self):
        """
        Calculates the ability score increase based on the race chosen by the
        player.

        Returns
        -------
        Updated ability_scores and ability_mods dictionaries.

        """
        if self.subrace == "hill dwarf":
            self.sr = HillDwarf
            HillDwarf.hdwarf_asi(self)
        elif self.subrace == "mountain dwarf":
            self.sr = MountainDwarf
            MountainDwarf.mdwarf_asi(self)
        elif self.subrace == "high elf":
            self.sr = HighElf
            HighElf.helf_asi(self)
        elif self.subrace == "wood elf":
            self.sr = WoodElf
            WoodElf.welf_asi(self)
        elif self.subrace == "drow":
            self.sr = Drow
            Drow.drow_asi(self)
        elif self.subrace == "lightfoot":
            self.sr = Lightfoot
            Lightfoot.lightfoot_asi(self)
        elif self.subrace == "stout":
            self.sr = Stout
            Stout.stout_asi(self)
        elif self.subrace == "forest gnome":
            self.sr = ForestGnome
            ForestGnome.fgnome_asi(self)
        elif self.subrace == "rock gnome":
            self.sr = RockGnome
            RockGnome.rgnome_asi(self)
        elif self.subrace == "protector aasimar":
            self.sr = ProtectorAasimar
            ProtectorAasimar.paasimar_asi(self)
        elif self.subrace == "scourge aasimar":
            self.sr = ScourgeAasimar
            ScourgeAasimar.saasimar_asi(self)
        elif self.subrace == "fallen aasimar":
            self.sr = FallenAasimar
            FallenAasimar.faasimar_asi(self)
        print("Ability scores:",self.ability_scores)
        self.ability_modifiers()
        return self.ability_scores
    
    def race_attributes(self):
        """
        Sets character attributes based on the race chosen by the player.

        Returns
        -------
        None.

        """
        if self.race == "dwarf":
            Dwarf.languages(self)
            Dwarf.darkvision(self)
            Dwarf.speed(self)
            Dwarf.dwarven_combat_training(self)
            Dwarf.dwarven_resilience(self)
        elif self.race == "elf":
            Elf.languages(self)
            Elf.darkvision(self)
            Elf.keen_senses(self)
            Elf.fey_ancestry(self)
            Elf.trance(self)
        elif self.race == "halfling":
            Halfling.languages(self)
            Halfling.brave(self)
            Halfling.speed(self)
            Halfling.size(self)
            Halfling.halfling_nimbleness(self)
            Halfling.lucky(self)
        elif self.race == "human":
            Human.languages(self)
        elif self.race == "gnome":
            Gnome.languages(self)
            Gnome.speed(self)
            Gnome.size(self)
            Gnome.darkvision(self)
            Gnome.gnome_cunning(self)
        elif self.race == "half elf":
            HalfElf.darkvision(self)
            HalfElf.fey_ancestry(self)
            HalfElf.languages(self)
            HalfElf.skill_versatility(self)
        elif self.race == "half orc":
            HalfOrc.darkvision(self)
            HalfOrc.languages(self)
            HalfOrc.relentless_endurance(self)
            HalfOrc.savage_attacks(self)
            HalfOrc.menacing(self)
        elif self.race == "tiefling":
            Tiefling.darkvision(self)
            Tiefling.hellish_resistance(self)
            Tiefling.infernal_legacy(self)
            Tiefling.languages(self)
        elif self.race == "aasimar":
            Aasimar.celestial_resistance(self)
            Aasimar.darkvision(self)
            Aasimar.healing_hands(self)
            Aasimar.languages(self)
            Aasimar.light_bearer(self)
        elif self.race == "goliath":
            Goliath.languages(self)
            Goliath.natural_athlete(self)
            Goliath.stone_endurance(self)
        return
            
    def subrace_attributes(self):
        """
        Sets character attributes based on the race chosen by the player.

        Returns
        -------
        None.

        """
        if self.subrace == "hill dwarf":
            HillDwarf.dwarven_toughness(self)
        elif self.subrace == "mountain dwarf":
            MountainDwarf.dwarven_armor_training(self)
        elif self.subrace == "high elf":
            HighElf.extra_language(self)
            HighElf.elf_weapon_training(self)
            HighElf.cantrip(self)
        elif self.subrace == "wood elf":
            WoodElf.fleet_of_foot(self)
            WoodElf.elf_weapon_training(self)
            WoodElf.mask_of_the_wild(self)
            WoodElf.speed(self)
        elif self.subrace == "drow":
            Drow.superior_darkvision(self)
            Drow.sunlight_sensitivity(self)
            Drow.drow_weapon_training(self)
            Drow.drow_magic(self)
        elif self.subrace == "lightfoot":
            Lightfoot.naturally_stealthy(self)
        elif self.subrace == "stout":
            Stout.stout_resilience(self)
        elif self.subrace == "silver":
            self.sr = SilverDragonborn
            SilverDragonborn.resistance(self)
        elif self.subrace == "forest gnome":
            ForestGnome.natural_illusionist(self)
            ForestGnome.speak_small_beasts(self)
        elif self.subrace == "rock gnome":
            RockGnome.artificer_lore(self)
            RockGnome.tinker(self)
        elif self.subrace == "protector aasimar":
            ProtectorAasimar.radiant_soul(self)
        elif self.subrace == "scourge aasimar":
            ScourgeAasimar.radiant_consumption(self)
        elif self.subrace == "fallen aasimar":
            FallenAasimar.necrotic_shroud(self)
        return
            
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
        poison_resistance = True
        self.poison_resistance = poison_resistance
        poison_save_adv = True
        self.poison_save_adv = poison_save_adv
        dwarven_resilience = [self.poison_resistance,self.poison_save_adv]
        self.dwarven_resilience = dwarven_resilience
        return self.dwarven_resilience
    
    def dwarven_combat_training(self):
        battleaxe_proficiency = True
        self.battleaxe_proficiency = battleaxe_proficiency
        handaxe_proficiency = True
        self.handaxe_proficiency = handaxe_proficiency
        light_hammer_proficiency = True
        self.light_hammer_proficiency = light_hammer_proficiency
        warhammer_proficiency = True
        self.warhammer_proficiency = warhammer_proficiency
        dwarven_combat_training = [self.battleaxe_proficiency,self.handaxe_proficiency,
                                   self.light_hammer_proficiency,self.warhammer_proficiency]
        self.dwarven_combat_training = dwarven_combat_training
        return self.dwarven_combat_training
    
    def tool_proficiency(self):
        tool = input("Choose proficiency in one of the following artisan's tools: smith's tools, brewer's supplies, or mason's tools.")
        if "smith" in tool:
            smith_tools_proficiency = True
            self.smith_tools_proficiency = smith_tools_proficiency
            return self.smith_tools_proficiency
        elif "brewer" in tool:
            brewer_tools_proficiency = True
            self.brewer_tools_proficiency = brewer_tools_proficiency
            return self.brewer_tools_proficiency
        elif "mason" in tool:
            mason_tools_proficiency = True
            self.mason_tools_proficiency = mason_tools_proficiency
            return self.mason_tools_proficiency
        
    def languages(self):
        languages = ["Common","Dwarvish"]
        self.languages = languages
        return self.languages
    
    def dwarf_asi(self):
        if self.race == "dwarf":
            self.ability_scores["Constitution"] = self.ability_scores.get("Constitution") + 2
        return self.ability_scores
    
class HillDwarf(Dwarf):
    def dwarven_toughness(self):
        dwarven_toughness = True
        self.dwarven_toughness = dwarven_toughness
        return self.dwarven_toughness
    
    def hdwarf_asi(self):
        if self.subrace == "hill dwarf":
            self.ability_scores["Wisdom"] = self.ability_scores.get("Wisdom") + 1
        return self.ability_scores
            
class MountainDwarf(Dwarf):
    def dwarven_armor_training(self):
        light_armor_proficiency = True
        self.light_armor_proficiency = light_armor_proficiency
        medium_armor_proficiency = True
        self.medium_armor_proficiency = medium_armor_proficiency
        dwarven_armor_training = [self.light_armor_proficiency,
                                  self.medium_armor_proficiency]
        self.dwarven_armor_training = dwarven_armor_training
        return self.dwarven_armor_training
    
    def mdwarf_asi(self):
        if self.subrace == "mountain dwarf":
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
        self.skill_proficiencies["perception"] = True
        return self.skill_proficiencies
    
    def fey_ancestry(self):        
        charm_save_adv = True
        self.charm_save_adv = charm_save_adv
        return self.charm_save_adv
    
    def trance(self):
        trance = True
        self.trance = trance
        return self.trance
    
    def languages(self):
        languages = ["Common","Elvish"]
        self.languages = languages
        return self.languages
    
    def elf_asi(self):
        if self.race == "elf":
            self.ability_scores["Dexterity"] = self.ability_scores.get("Dexterity") + 2
        return self.ability_scores
            
class HighElf(Elf):    
    def elf_weapon_training(self):
        longsword_proficiency = True
        self.longsword_proficiency =longsword_proficiency
        shortsword_proficiency = True
        self.shortsword_proficiency = shortsword_proficiency
        shortbow_proficiency = True
        self.shortbow_proficiency = shortbow_proficiency
        longbow_proficiency = True
        self.longbow_proficiency = longbow_proficiency
        elf_weapon_training = [self.longsword_proficiency, self.shortsword_proficiency,
                               self.shortbow_proficiency, self.longbow_proficiency]
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
        if self.subrace == "high elf":
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
        if self.subrace == "wood elf":
            self.ability_scores["Wisdom"] = self.ability_scores.get("Wisdom") + 1
        return self.ability_scores
    
class Drow(Elf):
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
        if self.subrace == "drow":
            self.ability_scores["Charisma"] = self.ability_scores.get("Charisma") + 1
        return self.ability_scores

class Halfling:
    def __init__(self):
        self.languages = []
        return
    
    def speed(self):
        speed = 25
        self.speed = speed
        return self.speed
    
    def size(self):
        size = "Small"
        self.size = size
        return self.size
    
    def brave(self):
        frighten_save_adv = True
        self.frighten_save_adv = frighten_save_adv
        return self.frighten_save_adv
    
    def lucky(self):
        pass
    
    def halfling_nimbleness(self):
        pass
    
    def languages(self):
        languages = ["Common","Halfling"]
        self.languages = languages
        return self.languages
        
    def halfling_asi(self):
        if self.race == "halfling":
            self.ability_scores["Dexterity"] = self.ability_scores.get("Dexterity") + 2
        return self.ability_scores
    
class Lightfoot(Halfling):
    def naturally_stealthy(self):
        pass
    
    def lightfoot_asi(self):
        if self.subrace == "lightfoot":
            self.ability_scores["Charisma"] = self.ability_scores.get("Charisma") + 1
        return self.ability_scores
    
class Stout(Halfling):
    def stout_resilience(self):
        poison_resistance = True
        self.poison_resistance = poison_resistance
        poison_save_adv = True
        self.poison_save_adv = poison_save_adv
        stout_resilience = [self.poison_resistance, self.poison_save_adv]
        self.stout_resilience = stout_resilience
        return self.stout_resilience
    
    def stout_asi(self):
        if self.subrace == "stout":
            self.ability_scores["Constitution"] = self.ability_scores.get("Constitution") + 1
        return self.ability_scores
    
class Human:
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
    
    def languages(self):
        languages = ["Common"]
        self.languages = languages
        extra_language = input("Choose another language: ")
        self.languages.append(extra_language)
        return self.languages
        
    def human_asi(self):
        if self.race == "human":
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
    
    def speed(self):
        speed = 30
        self.speed = speed
        return self.speed
    
    def size(self):
        size = "Medium"
        self.size = size
        return self.size
    
    def languages(self):
        languages = ["Common","Draconic"]
        self.languages = languages
        return self.languages
    
    def dragonborn_asi(self):
        if self.race == "dragonborn":
            self.ability_scores["Strength"] = self.ability_scores.get("Strength") + 2
            self.ability_scores["Charisma"] = self.ability_scores.get("Charisma") + 1
        return self.ability_scores
    
class SilverDragonborn(Dragonborn):
    def breath_weapon(self):
        bw_save_type = "Constitution save"
        self.bw_save_type = bw_save_type
        bw_save_dc = 8 + self.ability_mods.get("Constitution") + self.proficiency_bonus
        self.bw_save_dc = bw_save_dc
        bw_area = [15, "cone"]
        self.bw_area = bw_area
        if self.level < 6:
            bw_damage = d.roll(2, 6)
        elif self.level >= 6 or self.level < 11:
            bw_damage = d.roll(3, 6)
        elif self.level >= 11 or self.level < 16:
            bw_damage = d.roll(4, 6)
        elif self.level >= 16:
            bw_damage = d.roll(5, 6)
        self.bw_damage = bw_damage
        return [self.bw_save_type, self.bw_save_dc, self.bw_area, self.bw_damage]
    
    def resistance(self):
        cold_resistance = True
        self.cold_resistance = cold_resistance
        return self.cold_resistance

class Gnome:
    def __init__(self):
        self.languages = []
        return
    
    def speed(self):
        speed = 25
        self.speed = speed
        return self.speed
    
    def size(self):
        size = "Small"
        self.size = size
        return self.size
    
    def darkvision(self):
        darkvision = [True,60]
        self.darkvision = darkvision
        return self.darkvision
    
    def gnome_cunning(self):
        magic_int_save_adv = True
        self.magic_int_save_adv = magic_int_save_adv
        magic_wis_save_adv = True
        self.magic_wis_save_adv = magic_wis_save_adv
        magic_cha_save_adv = True
        self.magic_cha_save_adv = magic_cha_save_adv
        return [self.magic_int_save_adv, self.magic_wis_save_adv, self.magic_cha_save_adv]
    
    def languages(self):
        languages = ["Common","Dwarvish"]
        self.languages = languages
        return self.languages

    def gnome_asi(self):
        if self.race == "gnome":
            self.ability_scores["Intelligence"] = self.ability_scores.get("Intelligence") + 2
        return self.ability_scores
    
class ForestGnome(Gnome):
    def natural_illusionist(self):
        pass
    
    def speak_small_beasts(self):
        pass
    
    def fgnome_asi(self):
        if self.subrace == "forest gnome":
            self.ability_scores["Dexterity"] = self.ability_scores.get("Dexterity") + 1
        return self.ability_scores
    
class RockGnome(Gnome):
    def artificer_lore(self):
        pass
    
    def tinker(self):
        pass
    
    def rgnome_asi(self):
        if self.subrace == "rock gnome":
            self.ability_scores["Constitution"] = self.ability_scores.get("Constitution") + 1
        return self.ability_scores
    
class HalfElf:
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
    
    def languages(self):
        languages = ["Common", "Elvish"]
        self.languages = languages
        extra_language = input("Choose another language: ")
        self.languages.append(extra_language)
    
    def fey_ancestry(self):        
        charm_save_adv = True
        self.charm_save_adv = charm_save_adv
        return self.charm_save_adv
    
    def skill_versatility(self):
        print("Choose two skill proficiencies")
        t.sleep(1.2)
        Character.gain_skill_proficiency(self)
    
    def half_elf_asi(self):
        if self.race == "half elf":
            self.ability_scores["Charisma"] = self.ability_scores.get("Charisma") + 2
        return self.ability_scores
    
class HalfOrc:
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
    
    def languages(self):
        languages = ["Common", "Orc"]
        self.languages = languages
        return self.languages
    
    def relentless_endurance(self):
        pass
    
    def savage_attacks(self):
        pass
    
    def menacing(self):
        self.skill_proficiencies["intimidation"] = True
        return self.skill_proficiencies
    
    def half_orc_asi(self):
        if self.race == "half orc":
            self.ability_scores["Strength"] = self.ability_scores.get("Strength") + 2
            self.ability_scores["Constitution"] = self.ability_scores.get("Constitution") + 1
        return self.ability_scores
    
class Tiefling:
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
    
    def languages(self):
        languages = ["Common", "Infernal"]
        self.languages = languages
        return self.languages
    
    def hellish_resistance(self):
        fire_resistance = True
        self.fire_resistance = fire_resistance
        return self.fire_resistance
    
    def infernal_legacy(self):
        pass
    
    def tiefling_asi(self):
        if self.race == "tiefling":
            self.ability_scores["Intelligence"] = self.ability_scores.get("Intelligence") + 1
            self.ability_scores["Charisma"] = self.ability_scores.get("Charisma") + 2
        return self.ability_scores
    
class Aasimar:
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
    
    def languages(self):
        languages = ["Common", "Celestial"]
        self.languages = languages
        return self.languages
    
    def celestial_resistance(self):
        radiant_resistance = True
        self.radiant_resistance = radiant_resistance
        necrotic_resistance = True
        self.necrotic_resistance = necrotic_resistance
        return [self.radiant_resistance, self.necrotic_resistance]
    
    def healing_hands(self):
        pass
    
    def light_bearer(self):
        pass
    
    def aasimar_asi(self):
        if self.race == "aasimar":
            self.ability_scores["Charisma"] = self.ability_scores.get("Charisma") + 2
        return self.ability_scores
    
class ProtectorAasimar(Aasimar):
    def radiant_soul(self):
        pass
    
    def paasimar_asi(self):
        if self.subrace == "protector aasimar":
            self.ability_scores["Wisdom"] = self.ability_scores.get("Wisdom") + 1
        return self.ability_scores
    
class ScourgeAasimar(Aasimar):
    def radiant_consumption(self):
        pass
    
    def saasimar_asi(self):
        if self.subrace == "scourge aasimar":
            self.ability_scores["Constitution"] = self.ability_scores.get("Constitution") + 1
        return self.ability_scores
    
class FallenAasimar(Aasimar):
    def necrotic_shroud(self):
        pass
    
    def faasimar_asi(self):
        if self.subrace == "fallen aasimar":
            self.ability_scores["Strength"] = self.ability_scores.get("Strength") + 1
        return self.ability_scores

class Goliath:
    def __init__(self):
        self.languages = []
        return
    
    def languages(self):
        languages = ["Common", "Giant"]
        self.languages = languages
        return self.languages
    
    def natural_athlete(self):
        self.skill_proficiencies["athletics"] = True
        return self.skill_proficiencies
    
    def stone_endurance(self):
        pass
    
    def goliath_asi(self):
        if self.race == "goliath":
            self.ability_scores["Strength"] = self.ability_scores.get("Strength") + 2
            self.ability_scores["Constitution"] = self.ability_scores.get("Constitution") + 1
        return self.ability_scores
    
class Classes:
    def __init__(self):
        self.choosing()
        self.choosing_subclass()
        return
    
    def choosing(self):
        if self.level >= 1:
            char_class = input("Choose your class: ").lower().strip()
        self.char_class = char_class
        return self.char_class
    
    def choosing_subclass(self):
        level_1 = ["cleric", "sorcerer", "warlock"]
        level_2 = ["druid", "wizard"]
        level_3 = ["barbarian", "bard", "fighter", "monk", "paladin", "rogue"]
        if self.char_class in level_1 and self.level >= 1:
            char_subclass = input("Choose your subclass: ")
        elif self.char_class in level_2 and self.level >= 2:
            char_subclass = input("Choose your subclass: ")
        elif self.char_class in level_3 and self.level >= 3:
            char_subclass = input("Choose your subclass: ")
        else:
            char_subclass = False
        self.char_subclass = char_subclass
        return self.char_subclass
    
    def hitpoints(self):
        d6 = ["sorcerer", "wizard"]
        d8 = ["bard", "cleric", "druid", "monk", "rogue", "warlock"]
        d10 = ["fighter", "paladin"]
        d12 = ["barbarian"]
        if self.char_class in d6:
            if self.level == 1:
                hp_first = 6 + self._ability_mods.get("Constitution")
                hp = hp_first
            elif self.level > 1:
                hp_first = 6 + self._ability_mods.get("Constitution")
                hp = hp_first + (d.roll((self.level - 1), 6)) + (self.level - 1) * (self._ability_mods.get("Constitution"))
        elif self.char_class in d8:
            if self.level == 1:
                hp_first = 8 + self._ability_mods.get("Constitution")
                hp = hp_first
            elif self.level > 1:
                hp_first = 8 + self._ability_mods.get("Constitution")
                hp = hp_first + (d.roll((self.level - 1), 8)) + (self.level - 1) * (self._ability_mods.get("Constitution"))
        elif self.char_class in d10:
            if self.char_class == 1:
                hp_first = 10 + self._ability_mods.get("Constitution")
                hp = hp_first
            elif self.level > 1:
                hp_first = 10 + self._ability_mods.get("Constitution")
                hp = hp_first + (d.roll((self.level - 1), 10)) + (self.level - 1) * (self._ability_mods.get("Constitution"))
        elif self.char_class in d12:
            if self.level == 1:
                hp_first = 12 + self._ability_mods.get("Constitution")
                hp = hp_first
            elif self.level > 1:
                hp_first = 12 + self._ability_mods.get("Constitution")
                hp = hp_first + (d.roll((self.level - 1), 12)) + (self.level - 1) * (self._ability_mods.get("Constitution"))
        print(f"{self._name} has {hp} hitpoints.")
        self.hp = hp
        return self.hp
    
    def saving_throws(self):
        if self.char_class == "barbarian":
            self.save_proficiencies["Strength"] = True
            self.save_proficiencies["Constitution"] = True
        elif self.char_class == "bard":
            self.save_proficiencies["Dexterity"] = True
            self.save_proficiencies["Charisma"] = True
        elif self.char_class == "cleric":
            self.save_proficiencies["Wisdom"] = True
            self.save_proficiencies["Charisma"] = True
        elif self.char_class == "druid":
            self.save_proficiencies["Intelligence"] = True
            self.save_proficiencies["Wisdom"] = True
        elif self.char_class == "fighter":
            self.save_proficiencies["Strength"] = True
            self.save_proficiencies["Constitution"] = True
        elif self.char_class == "monk":
            self.save_proficiencies["Strength"] = True
            self.save_proficiencies["Dexterity"] = True
        elif self.char_class == "paladin":
            self.save_proficiencies["Wisdom"] = True
            self.save_proficiencies["Charisma"] = True
        elif self.char_class == "rogue":
            self.save_proficiencies["Dexterity"] = True
            self.save_proficiencies["Intelligence"] = True
        elif self.char_class == "sorcerer":
            self.save_proficiencies["Constitution"] = True
            self.save_proficiencies["Charisma"] = True
        elif self.char_class == "warlock":
            self.save_proficiencies["Wisdom"] = True
            self.save_proficiencies["Charisma"] = True
        elif self.char_class == "wizard":
            self.save_proficiencies["Intelligence"] = True
            self.save_proficiencies["Wisdom"] = True
        return self.save_proficiencies
    
    def skills(self):
        if self.char_class == "barbarian":
            player_choice = input("Skill proficiencies - Choose two from Animal Handling, Athletics, Intimidation, Nature, Perception, and Survival: ").lower()
        elif self.char_class == "bard":
            player_choice = input("Skill proficiencies - Choose any three: ").lower()
        elif self.char_class == "cleric":
            player_choice = input("Skill proficiencies - Choose two from History, Insight, Medicine, Persuasion, Religion: ").lower()
        elif self.char_class == "druid":
            player_choice = input("Skill proficiencies - Choose two from Arcana, Animal Handling, Insight, Medicine, Nature, Perception, Religion, and Survival: ").lower()
        elif self.char_class == "fighter":
            player_choice = input("Skill proficiencies - Choose two from Acrobatics, Animal Handling, Athletics, History, Insight, Intimidation, Perception, and Survival: ").lower()
        elif self.char_class == "monk":
            player_choice = input("Skill proficiencies - Choose two from Acrobatics, Athletics, History, Insight, Religion, and Stealth: ").lower()
        elif self.char_class == "paladin":
            player_choice = input("Skill proficiencies - Choose two from Athletics, Insight, Intimidation, Medicine, Persuasion, and Religion: ").lower()
        elif self.char_class == "rogue":
            player_choice = input("Skill proficiencies - Choose four from Acrobatics, Athletics, Deception, Insight, Intimidation, Investigation, Perception, Performance, Persuasion, Sleight of Hand, and Stealth: ").lower()
        elif self.char_class == "sorcerer":
            player_choice = input("Skill proficiencies - Choose two from Arcana, Deception, Insight, Intimidation, Persuasion, and Religion: ").lower()
        elif self.char_class == "warlock":
            player_choice = input("Skill proficiencies - Choose two from Arcana, Deception, History, Intimidation, Investigation, Nature, and Religion: ").lower()
        elif self.char_class == "wizard":
            player_choice = input("Skill proficiencies - Choose two from Arcana, History, Insight, Investigation, Medicine, and Religion: ").lower()
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
            
class Barbarian:
    def __init__(self):
        self.light_armor_proficiency = True
        self.medium_armor_proficiency = True
        self.shield_proficiency = True
        self.simple_weapons_proficiency = True
        self.martial_weapons_proficiency = True
        return
        
    def rage(self):
        pass
        
c = Campaign()

def main():
    print("Not affiliated with Wizards of the Coast LLC")

if __name__ == '__main__':
    main()