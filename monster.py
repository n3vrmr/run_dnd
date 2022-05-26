# -*- coding: utf-8 -*-
"""
Created on Wed May 25 18:10:09 2022

@author: Nevermore
"""

import dice as d

class Monster:
    def __init__(self, size, kind, cr):
        self.size = size
        self.kind = kind
        self.cr = cr
        return
    
class Beholder():
    def __init__(self, ac=18, hp=180, speed_fly=20):
        self._ac = ac
        self._hp = hp
        self._speed_fly = speed_fly
        self._ability_scores = {"Strength":10, "Dexterity":14, "Constitution":18,
                                "Intelligence":17, "Wisdom":15, "Charisma":17}
        self._ability_mods = {"Strength":0, "Dexterity":2, "Constitution":4,
                                "Intelligence":3, "Wisdom":2, "Charisma":3}
        self._proficiency_bonus = 5
        self._save_proficiencies = {"Strength":False, "Dexterity":False, "Constitution":False,
                                "Intelligence":True, "Wisdom":True, "Charisma":True}
        self._skill_proficiencies = {"Perception":True}
        self._condition_immunities = {"prone":True}
        self._darkvision = True, 120
        self._passive_perception = 22
        self._languages = ["Deep Speech", "Undercommon"]
        return
    
    def antimagic_cone(self):
        print("")
        pass
    
beholder=Beholder()
print(beholder._ac)