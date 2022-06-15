# -*- coding: utf-8 -*-
"""
Created on Wed May 25 21:39:05 2022

@author: Nevermore
"""

import dice as d

class Combat:
    def __init__(self, initiative = {}):
        self.initiative = initiative
        
    def initiative(instance):
        print("")
    
    def attacking(self, weapon):
        self.weapon = weapon
        
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