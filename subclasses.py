# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 19:50:49 2022

@author: Nevermore
"""

import dice as d
import time as t
from classes import Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Rogue, Sorcerer, Warlock, Wizard

class Subclasses:
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
    
    def set_subclass(self):
        if "berserker" in self.char_subclass:
            self.c_subclass = PathOfTheBerserker
        # elif "tragedy" in self.char_subclass:
        #     self.c_subclass = CollegeOfTragedy
        elif "light" in self.char_subclass:
            self.c_subclass = LightDomain
        
        

class PathOfTheBerserker(Barbarian):
    def frenzy(self):
        pass
    
    def mindless_rage(self):
        pass
    
    def intimidating_presence(self):
        pass
    
    def retaliation(self):
        pass

# class CollegeOfTragedy(Bard):

class LightDomain(Cleric):
    def bonus_cantrip(self):
        cantrip = "light"
        return cantrip
    
    def warding_flare(self):
        pass
    
    def radiance_of_the_dawn(self):
        if self.level >= 2:
            dmg = d.roll(2, 10) + self.level
            dmg_type = "radiant"
            text = f"{dmg} points of {dmg_type} damage!"
            print(text)
        return dmg
    
    def improved_flare(self):
        pass
    
    def potent_spellcasting(self):
        pass
    
    def corona_of_light(self):
        pass
    
class CircleOfTheMoon(Druid):
    def combat_wild_shape(self):
        pass
    
    def circle_forms(self):
        pass
    
    def primal_strike(self):
        pass
    
    def elemental_wild_shape(self):
        pass
    
    def thousand_forms(self):
        pass
    
class Champion(Fighter):
    def improved_critical(self):
        print("Critical at 19")
        return
    
    def remarkable_athlete(self):
        pass
    
    def additional_fighting_style(self):
        pass
    
    def superior_critical(self):
        pass
    
    def survivor(self):
        if self.level >= 18:
            if self.hp_current <= self.hp_total//2:
                regain = 5 + self._ability_mods.get("Constitution")
                self.hp_current = self.hp_current + regain
        return self.hp_current
    
