# -*- coding: utf-8 -*-
"""
Created on Wed May 25 18:10:09 2022

@author: Nevermore
"""

import dice as d

class Monster:
    def __init__(self, size, kind):
        self.size = size
        self.kind = kind
        return
    
class Beholder():
    def __init__(self, ac=18, hp=180, speed_fly=20):
        self.ac = ac
        self._hp_total = hp
        self.hp_current = self._hp_total
        self._speed_fly = speed_fly
        self._ability_scores = {"Strength":10, "Dexterity":14, "Constitution":18,
                                "Intelligence":17, "Wisdom":15, "Charisma":17}
        self._ability_mods = {"Strength":0, "Dexterity":2, "Constitution":4,
                                "Intelligence":3, "Wisdom":2, "Charisma":3}
        self._proficiency_bonus = 5
        self._save_proficiencies = {"Strength":False, "Dexterity":False, "Constitution":False,
                                "Intelligence":True, "Wisdom":True, "Charisma":True}
        self._skill_proficiencies = {"acrobatics":False, "animal handling":False,
                                    "arcana":False, "athletics":False,
                                    "deception":False, "history":False,
                                    "insight":False, "intimidation":False,
                                    "investigation":False, "medicine":False,
                                    "nature":False, "perception":True,
                                    "performance":False, "persuasion":False,
                                    "religion":False, "sleight of hand":False,
                                    "stealth":False, "survival":False}
        self._immunity_prone = True
        self._darkvision = [True, 120]
        self._passive_perception = 10 + self._proficiency_bonus + self._ability_mods.get("Wisdom")
        self._languages = ["Deep Speech", "Undercommon"]
        self.save_dc = 16
        return
    
    def antimagic_cone(self):
        pass
    
    def eye_rays(self):
        rays = d.roll(3, 10, True)
        for ray in rays:
            if ray == 1:
                print(f"Charm Ray, make a Wisdom save! (DC {self.save_dc})")
            elif ray == 2:
                print(f"Paralyzing Ray, make a Constitution save! (DC {self.save_dc})")
            elif ray == 3:
                print(f"Fear Ray, make a Wisdom save! (DC {self.save_dc})")
            elif ray == 4:
                print(f"Slowing Ray, make a Dexterity save! (DC {self.save_dc})")
            elif ray == 5:
                dmg = d.roll(8, 8)
                dmg_type = "necrotic"
                print(f"Ennervation Ray, make a Constitution save! Fail takes {dmg} points of {dmg_type} damage, {dmg//2} on success. (DC {self.save_dc})")
            elif ray == 6:
                print(f"Telekinetic Ray, make a Strength save! (DC {self.save_dc})")
            elif ray == 7:
                print(f"Sleep Ray, make a Wisdom save! (DC {self.save_dc})")
            elif ray == 8:
                print(f"Petrification Ray, make a Dexterity save! (DC {self.save_dc})")
            elif ray == 9:
                dmg = d.roll(10, 8)
                dmg_type = "force"
                print(f"Disintegration Ray, make a Dexterity save! Fail takes {dmg} points of {dmg_type} damage, {dmg//2} on success. (DC {self.save_dc})")
            elif ray == 10:
                dmg = d.roll(10, 10)
                dmg_type = "necrotic"
                print(f"Death Ray, make a Dexterity save! Fail takes {dmg} points of {dmg_type} damage, {dmg//2} damage on success. (DC {self.save_dc})")
        return rays
    
    def random_eye_ray(self):
        rays = d.roll(1, 10, True)
        for ray in rays:
            if ray == 1:
                print(f"Charm Ray, make a Wisdom save! (DC {self.save_dc})")
            elif ray == 2:
                print(f"Paralyzing Ray, make a Constitution save! (DC {self.save_dc})")
            elif ray == 3:
                print(f"Fear Ray, make a Wisdom save! (DC {self.save_dc})")
            elif ray == 4:
                print(f"Slowing Ray, make a Dexterity save! (DC {self.save_dc})")
            elif ray == 5:
                dmg = d.roll(8, 8)
                dmg_type = "necrotic"
                print(f"Ennervation Ray, make a Constitution save! Fail takes {dmg} points of {dmg_type} damage, {dmg//2} on success. (DC {self.save_dc})")
            elif ray == 6:
                print(f"Telekinetic Ray, make a Strength save! (DC {self.save_dc})")
            elif ray == 7:
                print(f"Sleep Ray, make a Wisdom save! (DC {self.save_dc})")
            elif ray == 8:
                print(f"Petrification Ray, make a Dexterity save! (DC {self.save_dc})")
            elif ray == 9:
                dmg = d.roll(10, 8)
                dmg_type = "force"
                print(f"Disintegration Ray, make a Dexterity save! Fail takes {dmg} points of {dmg_type} damage, {dmg//2} on success. (DC {self.save_dc})")
            elif ray == 10:
                dmg = d.roll(10, 10)
                dmg_type = "necrotic"
                print(f"Death Ray, make a Dexterity save! Fail takes {dmg} points of {dmg_type} damage, {dmg//2} damage on success. (DC {self.save_dc})")
        return rays
    
beholder = Beholder()

def main():
    print("Beauty is in the eye of the Beholder...")
    
if __name__ == '__main__':
    main()