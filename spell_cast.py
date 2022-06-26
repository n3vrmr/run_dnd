# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 18:32:27 2022

@author: Nevermore
"""

import dice as d
import time as t

class Spells:
    def __init__(self, spell_name, spell_level, spell_range, cast_time,
                 verbal:bool, somatic:bool, material:str, duration, dmg_type=False):
        self.spell_name = spell_name
        self.spell_level = spell_level
        self.spell_range = spell_range
        self.cast_time = cast_time
        self.verbal = verbal
        self.somatic = somatic
        self.material = material
        self.duration = duration
        self.dmg_type = dmg_type
        return

def fireball(level:int):
    fireball = Spells("fireball", level, 150, "1 action", True, True,
                      "a tiny ball of bat guano and sulfur", "Instantaneous", 
                      "fire")
    if level == 3:
        dmg = d.roll(8, 6)
    elif level >= 4:
        dmg = d.roll((8 + (level - 3)), 6)
    text = f"{dmg} points of fire damage!"
    print(text)
    return fireball

def magic_missile(level:int):
    magic_missile = Spells("magic missile", level, 120, "1 action", True, True,
                           "None", "Instantaneous", "force")
    darts = []
    if level == 1:
        for i in range(0,3):
            dmg = d.roll(1, 4) + 1
            darts.append(dmg)
    elif level >= 2:
        for i in range(0, 3 + (level - 1)):
            dmg = d.roll(1, 4) + 1
            darts.append(dmg)
    text = f"{3 + (level - 1)} darts dealing {darts} points of force damage!"
    total_dmg = sum(darts)
    print(text)
    print(f"Total damage: {total_dmg}")
    return magic_missile