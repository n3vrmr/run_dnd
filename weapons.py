# -*- coding: utf-8 -*-
"""
Created on Wed May 25 17:26:29 2022

@author: Nevermore
"""

import dice as d

class Weapon:
    def __init__(self, name, kind=True):
        self.name = name
        
        
class SimpleMelee:
    def __init__(self, name):
        simple_melee = ["Club", "Dagger", "Greatclub", "Handaxe", "Javelin",
                  "Light hammer", "Mace", "Quarterstaff", "Sickle", "Spear"]
        pass
        
class SimpleRanged:
    def __init__(self, name):
        simple_ranged = ["Crossbow (light)", "Dart", "Shortbow", "Sling"]
        pass        

class MartialMelee:
    def __init__(self, name):
        martial_melee = ["Battleaxe", "Flail", "Glaive", "Greataxe",
                         "Greatsword", "Halberd", "Lance", "Longsword", "Maul",
                         "Morningstar", "Pike", "Rapier", "Scimitar",
                         "Shortsword", "Trident", "War pick", "Warhammer",
                         "Whip"]
        return martial_melee
    
class Battleaxe:
    def __init__(self, versatile=True, damage_type="slashing"):
        self.damage_type = damage_type
        two_handed = input("Two-handed? ").lower().strip()
        if "y" in two_handed:
            two_handed = True
        elif "n" in two_handed:
            two_handed = False
        self.two_handed = two_handed
        self.roll_to_hit()
        self.damage()
        pass
    
    def roll_to_hit(self):
        die = d.roll(1, 20)
        print(die)
        return die
    
    def damage(self):
        if self.two_handed == True:
            damage = d.roll(1, 10)
        else:
            damage = d.roll(1, 8)
        print(f"Dealt {damage} points of {self.damage_type} damage!")
        return damage
    
    
class MartialRanged:
    def __init__(self, name):
        martial_ranged = ["Blowgun", "Crossbow (hand)", "Crossbow (heavy)",
                          "Longbow", "Net"]
        pass