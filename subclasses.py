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