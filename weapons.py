# -*- coding: utf-8 -*-
"""
Created on Wed May 25 17:26:29 2022

@author: Nevermore
"""

import dice as d

class Weapon:
    def __init__(self, magical=False):
        self.magical = magical
        return
    
class Club(Weapon):
    def attack_roll(self):
        if self.proficiency_club == True or self.proficiency_simple_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 4) + self._ability_mods.get("Strength")
        return dmg
    
class Dagger(Weapon):
    def attack_roll(self):
        if self.proficiency_dagger == True or self.proficiency_simple_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 4) + self._ability_mods.get("Dexterity")
        return dmg
    
class Greatclub(Weapon):
    def attack_roll(self):
        if self.proficiency_greatclub == True or self.proficiency_simple_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 8) + self._ability_mods.get("Strength")
        return dmg

class Handaxe(Weapon):
    def attack_roll(self):
        if self.proficiency_handaxe == True or self.proficiency_simple_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 6) + self._ability_mods.get("Strength")
        return dmg
    
class Javelin(Weapon):
    def attack_roll(self):
        if self.proficiency_javelin == True or self.proficiency_simple_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 6) + self._ability_mods.get("Strength")
        return dmg
    
class LightHammer(Weapon):
    def attack_roll(self):
        if self.proficiency_light_hammer == True or self.proficiency_simple_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 4) + self._ability_mods.get("Strength")
        return dmg
    
class Mace(Weapon):
    def attack_roll(self):
        if self.proficiency_mace == True or self.proficiency_simple_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 6) + self._ability_mods.get("Strength")
        return dmg
    
class Quarterstaff(Weapon):
    def attack_roll(self):
        if self.proficiency_quarterstaff == True or self.proficiency_simple_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
        return roll
    
    def damage(self):
        hands = input("One or two hands? ")
        if 1 in hands or "one" in hands:
            dmg = d.roll(1, 6) + self._ability_mods.get("Dexterity")
        elif 2 in hands or "two" in hands:
            dmg = d.roll(1, 8) + self._ability_mods.get("Dexterity")
        return dmg
    
class Sickle(Weapon):
    def attack_roll(self):
        if self.proficiency_sickle == True or self.proficiency_simple_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 4) + self._ability_mods.get("Dexterity")
        return dmg
    
class Spear(Weapon):
    def attack_roll(self):
        if self.proficiency_spear == True or self.proficiency_simple_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
        return roll
    
    def damage(self):
        hands = input("One or two hands? ")
        if 1 in hands or "one" in hands:
            dmg = d.roll(1, 6) + self._ability_mods.get("Strength")
        elif 2 in hands or "two" in hands:
            dmg = d.roll(1, 8) + self._ability_mods.get("Strength")
        return dmg
    
class LightCrossbow(Weapon):
    def attack_roll(self):
        if self.proficiency_light_xbow == True or self.proficiency_simple_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 8) + self._ability_mods.get("Dexterity")
        return dmg
        
class Dart(Weapon):
    def attack_roll(self):
        if self.proficiency_darts == True or self.proficiency_simple_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 4) + self._ability_mods.get("Dexterity")
        return dmg
    
class Shortbow(Weapon):
    def attack_roll(self):
        if self.proficiency_shortbow == True or self.proficiency_simple_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 8) + self._ability_mods.get("Dexterity")
        return dmg
    
class Sling(Weapon):
    def attack_roll(self):
        if self.proficiency_sling == True or self.proficiency_simple_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 4) + self._ability_mods.get("Dexterity")
        return dmg
    
class Battleaxe(Weapon):
    def attack_roll(self):
        if self.proficiency_battleaxe == True or self.proficiency_martial_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
        return roll
    
    def damage(self):
        hands = input("One or two hands? ")
        if 1 in hands or "one" in hands:
            dmg = d.roll(1, 8) + self._ability_mods.get("Strength")
        elif 2 in hands or "two" in hands:
            dmg = d.roll(1, 10) + self._ability_mods.get("Strength")
        return dmg
    
class Flail(Weapon):
    def attack_roll(self):
        if self.proficiency_flail == True or self.proficiency_martial_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 8) + self._ability_mods.get("Strength")
        return dmg
    
class Glaive(Weapon):
    def attack_roll(self):
        if self.proficiency_glaive == True or self.proficiency_martial_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 10) + self._ability_mods.get("Strength")
        return dmg
    
class Greataxe(Weapon):
    def attack_roll(self):
        if self.proficiency_greataxe == True or self.proficiency_martial_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 12) + self._ability_mods.get("Strength")
        return dmg
    
class Greatsword(Weapon):
    def attack_roll(self):
        if self.proficiency_greatsword == True or self.proficiency_martial_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
        return roll
    
    def damage(self):
        dmg = d.roll(2, 6) + self._ability_mods.get("Strength")
        return dmg
    
class Halberd(Weapon):
    def attack_roll(self):
        if self.proficiency_halberd == True or self.proficiency_martial_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 10) + self._ability_mods.get("Strength")
        return dmg

class Lance(Weapon):
    def attack_roll(self):
        if self.proficiency_lance == True or self.proficiency_martial_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 12) + self._ability_mods.get("Strength")
        return dmg
    
class Longsword(Weapon):
    def attack_roll(self):
        if self.proficiency_longsword == True or self.proficiency_martial_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
        return roll
    
    def damage(self):
        hands = input("One or two hands? ")
        if 1 in hands or "one" in hands:
            dmg = d.roll(1, 8) + self._ability_mods.get("Strength")
        elif 2 in hands or "two" in hands:
            dmg = d.roll(1, 10) + self._ability_mods.get("Strength")
        return dmg

class Maul(Weapon):
    def attack_roll(self):
        if self.proficiency_maul == True or self.proficiency_martial_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
        return roll
    
    def damage(self):
        dmg = d.roll(2, 6) + self._ability_mods.get("Strength")
        return dmg
    
class Morningstar(Weapon):
    def attack_roll(self):
        if self.proficiency_morningstar == True or self.proficiency_martial_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 8) + self._ability_mods.get("Strength")
        return dmg
    
class Pike(Weapon):
    def attack_roll(self):
        if self.proficiency_pike == True or self.proficiency_martial_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 10) + self._ability_mods.get("Strength")
        return dmg
    
class Rapier(Weapon):
    def attack_roll(self):
        if self.proficiency_rapier == True or self.proficiency_martial_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 8) + self._ability_mods.get("Dexterity")
        return dmg

class Scimitar(Weapon):
    def attack_roll(self):
        if self.proficiency_scimitar == True or self.proficiency_martial_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 6) + self._ability_mods.get("Dexterity")
        return dmg
    
class Shortsword(Weapon):
    def attack_roll(self):
        if self.proficiency_shortsword == True or self.proficiency_martial_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 6) + self._ability_mods.get("Dexterity")
        return dmg
    
class Trident(Weapon):
    def attack_roll(self):
        if self.proficiency_trident == True or self.proficiency_martial_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
        return roll
    
    def damage(self):
        hands = input("One or two hands? ")
        if 1 in hands or "one" in hands:
            dmg = d.roll(1, 6) + self._ability_mods.get("Strength")
        elif 2 in hands or "two" in hands:
            dmg = d.roll(1, 8) + self._ability_mods.get("Strength")
        return dmg
    
class WarPick(Weapon):
    def attack_roll(self):
        if self.proficiency_war_pick == True or self.proficiency_martial_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 8) + self._ability_mods.get("Strength")
        return dmg
    
class Warhammer(Weapon):
    def attack_roll(self):
        if self.proficiency_warhammer == True or self.proficiency_martial_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Strength")
        return roll
    
    def damage(self):
        hands = input("One or two hands? ")
        if 1 in hands or "one" in hands:
            dmg = d.roll(1, 8) + self._ability_mods.get("Strength")
        elif 2 in hands or "two" in hands:
            dmg = d.roll(1, 10) + self._ability_mods.get("Strength")
        return dmg
    
class Whip(Weapon):
    def attack_roll(self):
        if self.proficiency_whip == True or self.proficiency_martial_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 4) + self._ability_mods.get("Dexterity")
        return dmg
    
class Blowgun(Weapon):
    def attack_roll(self):
        if self.proficiency_blowgun == True or self.proficiency_martial_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
        return roll
    
    def damage(self):
        dmg = 1
        return dmg
    
class HandCrossbow(Weapon):
    def attack_roll(self):
        if self.proficiency_hand_xbow == True or self.proficiency_martial_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 6) + self._ability_mods.get("Dexterity")
        return dmg
    
class HeavyCrossbow(Weapon):
    def attack_roll(self):
        if self.proficiency_heavy_xbow == True or self.proficiency_martial_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 10) + self._ability_mods.get("Dexterity")
        return dmg
    
class Longbow(Weapon):
    def attack_roll(self):
        if self.proficiency_longbow == True or self.proficiency_martial_weapons == True:
            roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity") + self.proficiency_bonus
        else:
           roll = d.roll(2, 20, True, True) + self._ability_mods.get("Dexterity")
        return roll
    
    def damage(self):
        dmg = d.roll(1, 8) + self._ability_mods.get("Dexterity")
        return dmg

def main():
    print("Dagger, dagger, dagger")
    
if __name__ == '__main__':
    main()