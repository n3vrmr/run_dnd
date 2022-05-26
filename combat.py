# -*- coding: utf-8 -*-
"""
Created on Wed May 25 21:39:05 2022

@author: Nevermore
"""

import dice as d
from new import Character,Race,Dwarf
from weapons import Battleaxe
from monster import beholder

class Combat:
    def __init__(self, initiative = {}):
        self.initiative = initiative
        
    def initiative(instance):
        print("")