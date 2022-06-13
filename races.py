# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 13:05:07 2022

@author: Nevermore
"""

import time as t

class Race:
    def __init__(self):
        self.race = self.choosing()
        self.subrace = self.choosing_subrace()
        return
    
    def choosing():
        race = input("Choose your character's race: ").lower().strip()
        return race
    
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
    
    def race_attributes(self):
        """
        Sets character attributes based on the race chosen by the player.

        Returns
        -------
        None.

        """
        if self.race == "dwarf":
            Dwarf.darkvision(self)
            Dwarf.speed(self)
            Dwarf.dwarven_combat_training(self)
            Dwarf.dwarven_resilience(self)
        elif self.race == "elf":
            Elf.darkvision(self)
            Elf.keen_senses(self)
            Elf.fey_ancestry(self)
            Elf.trance(self)
        elif self.race == "halfling":
            Halfling.brave(self)
            Halfling.speed(self)
            Halfling.size(self)
            Halfling.halfling_nimbleness(self)
            Halfling.lucky(self)
        elif self.race == "human":
            pass
        elif self.race == "dragonborn":
            Dragonborn.size(self)
            Dragonborn.speed(self)
        elif self.race == "gnome":
            Gnome.speed(self)
            Gnome.size(self)
            Gnome.darkvision(self)
            Gnome.gnome_cunning(self)
        elif self.race == "half elf":
            HalfElf.darkvision(self)
            HalfElf.fey_ancestry(self)
            HalfElf.skill_versatility(self)
        elif self.race == "half orc":
            HalfOrc.darkvision(self)
            HalfOrc.relentless_endurance(self)
            HalfOrc.savage_attacks(self)
            HalfOrc.menacing(self)
        elif self.race == "tiefling":
            Tiefling.darkvision(self)
            Tiefling.hellish_resistance(self)
            Tiefling.infernal_legacy(self)
        elif self.race == "aasimar":
            Aasimar.celestial_resistance(self)
            Aasimar.darkvision(self)
            Aasimar.healing_hands(self)
            Aasimar.light_bearer(self)
        elif self.race == "goliath":
            Goliath.natural_athlete(self)
            Goliath.stone_endurance(self)
        return
    
    def languages(self):
        if self.race == "dwarf":
            languages = ["Common","Dwarvish"]
        elif self.race == "elf":
            languages = ["Common","Elvish"]
        elif self.race == "halfling":
            languages = ["Common","Halfling"]
        elif self.race == "human":
            languages = ["Common"]
            extra_language = input("Choose another language: ")
            languages.append(extra_language)
        elif self.race == "dragonborn":
            languages = ["Common","Draconic"]
        elif self.race == "gnome":
            languages = ["Common","Dwarvish"]
        elif self.race == "half elf":
            languages = ["Common", "Elvish"]
            extra_language = input("Choose another language: ")
            languages.append(extra_language)
        elif self.race == "half orc":
            languages = ["Common", "Orc"]
        elif self.race == "tiefling":
            languages = ["Common", "Infernal"]
        elif self.race == "aasimar":
            languages = ["Common", "Celestial"]
        elif self.race == "goliath":
            languages = ["Common", "Giant"]
        self.languages = languages
        return self.languages
            
class Dwarf:
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
    
    def dwarf_asi(self):
        if self.race == "dwarf":
            self.ability_scores["Constitution"] = self.ability_scores.get("Constitution") + 2
        return self.ability_scores
        
class Elf:
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
    
    def elf_asi(self):
        if self.race == "elf":
            self.ability_scores["Dexterity"] = self.ability_scores.get("Dexterity") + 2
        return self.ability_scores

class Halfling:
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
        
    def halfling_asi(self):
        if self.race == "halfling":
            self.ability_scores["Dexterity"] = self.ability_scores.get("Dexterity") + 2
        return self.ability_scores
    
class Human:
    def speed(self):
        speed = 30
        self.speed = speed
        return self.speed
    
    def size(self):
        size = "Medium"
        self.size = size
        return self.size
        
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
    def speed(self):
        speed = 30
        self.speed = speed
        return self.speed
    
    def size(self):
        size = "Medium"
        self.size = size
        return self.size
    
    def dragonborn_asi(self):
        if self.race == "dragonborn":
            self.ability_scores["Strength"] = self.ability_scores.get("Strength") + 2
            self.ability_scores["Charisma"] = self.ability_scores.get("Charisma") + 1
        return self.ability_scores

class Gnome:
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

    def gnome_asi(self):
        if self.race == "gnome":
            self.ability_scores["Intelligence"] = self.ability_scores.get("Intelligence") + 2
        return self.ability_scores
    
class HalfElf:
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
    
    def fey_ancestry(self):        
        charm_save_adv = True
        self.charm_save_adv = charm_save_adv
        return self.charm_save_adv
    
    def skill_versatility(self):
        t.sleep(1.2)
        first = input("Choose a skill proficiency: ")
        self.skill_proficiencies[f"{first}"] = True
        t.sleep(1.2)
        second = input("Choose a skill proficiency: ")
        self.skill_proficiencies[f"{second}"] = True
        return self.skill_proficiencies
    
    def half_elf_asi(self):
        if self.race == "half elf":
            self.ability_scores["Charisma"] = self.ability_scores.get("Charisma") + 2
        return self.ability_scores
    
class HalfOrc:
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
    
class Goliath:
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