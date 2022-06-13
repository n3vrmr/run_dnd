# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 13:36:19 2022

@author: Nevermore
"""

import dice as d
from races import Dwarf, Elf, Halfling, Dragonborn, Gnome, Aasimar

class Subrace:
    def choosing_subrace():
        subrace = input("Choose your character's subrace: ").lower().strip()
        return subrace
    
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