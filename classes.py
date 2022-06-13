# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 15:46:19 2022

@author: Nevermore, Luiza
"""
# This is the third file

import dice as d

class Classes:
    def __init__(self):
        self.set_class()
        return
    
    def choosing(self):
        if self.level >= 1:
            char_class = input("Choose your class: ").lower().strip()
        self.char_class = char_class
        return self.char_class
    
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
    
    def set_class(self):
        if self.char_class == "barbarian":
            self.c_class = Barbarian
        elif self.char_class == "bard":
            pass
        return self.c_class
    
    def hitpoints(self):
        d6 = ["sorcerer", "wizard"]
        d8 = ["bard", "cleric", "druid", "monk", "rogue", "warlock"]
        d10 = ["fighter", "paladin"]
        d12 = ["barbarian"]
        if self.char_class in d6:
            if self.level == 1:
                hp_first = 6 + self._ability_mods.get("Constitution")
                hp = hp_first
            elif self.level > 1:
                hp_first = 6 + self._ability_mods.get("Constitution")
                hp = hp_first + (d.roll((self.level - 1), 6)) + (self.level - 1) * (self._ability_mods.get("Constitution"))
        elif self.char_class in d8:
            if self.level == 1:
                hp_first = 8 + self._ability_mods.get("Constitution")
                hp = hp_first
            elif self.level > 1:
                hp_first = 8 + self._ability_mods.get("Constitution")
                hp = hp_first + (d.roll((self.level - 1), 8)) + (self.level - 1) * (self._ability_mods.get("Constitution"))
        elif self.char_class in d10:
            if self.char_class == 1:
                hp_first = 10 + self._ability_mods.get("Constitution")
                hp = hp_first
            elif self.level > 1:
                hp_first = 10 + self._ability_mods.get("Constitution")
                hp = hp_first + (d.roll((self.level - 1), 10)) + (self.level - 1) * (self._ability_mods.get("Constitution"))
        elif self.char_class in d12:
            if self.level == 1:
                hp_first = 12 + self._ability_mods.get("Constitution")
                hp = hp_first
            elif self.level > 1:
                hp_first = 12 + self._ability_mods.get("Constitution")
                hp = hp_first + (d.roll((self.level - 1), 12)) + (self.level - 1) * (self._ability_mods.get("Constitution"))
        print(f"{self._name} has {hp} hitpoints.")
        self.hp = hp
        return self.hp
    
    def saves(self):
        if self.char_class == "barbarian":
            self.save_proficiencies["Strength"] = True
            self.save_proficiencies["Constitution"] = True
        elif self.char_class == "bard":
            self.save_proficiencies["Dexterity"] = True
            self.save_proficiencies["Charisma"] = True
        elif self.char_class == "cleric":
            self.save_proficiencies["Wisdom"] = True
            self.save_proficiencies["Charisma"] = True
        elif self.char_class == "druid":
            self.save_proficiencies["Intelligence"] = True
            self.save_proficiencies["Wisdom"] = True
        elif self.char_class == "fighter":
            self.save_proficiencies["Strength"] = True
            self.save_proficiencies["Constitution"] = True
        elif self.char_class == "monk":
            self.save_proficiencies["Strength"] = True
            self.save_proficiencies["Dexterity"] = True
        elif self.char_class == "paladin":
            self.save_proficiencies["Wisdom"] = True
            self.save_proficiencies["Charisma"] = True
        elif self.char_class == "rogue":
            self.save_proficiencies["Dexterity"] = True
            self.save_proficiencies["Intelligence"] = True
        elif self.char_class == "sorcerer":
            self.save_proficiencies["Constitution"] = True
            self.save_proficiencies["Charisma"] = True
        elif self.char_class == "warlock":
            self.save_proficiencies["Wisdom"] = True
            self.save_proficiencies["Charisma"] = True
        elif self.char_class == "wizard":
            self.save_proficiencies["Intelligence"] = True
            self.save_proficiencies["Wisdom"] = True
        return self.save_proficiencies
    
    def skills(self):
        if self.char_class == "barbarian":
            player_choice = input("Skill proficiencies - Choose two from Animal Handling, Athletics, Intimidation, Nature, Perception, and Survival: ").lower()
        elif self.char_class == "bard":
            player_choice = input("Skill proficiencies - Choose any three: ").lower()
        elif self.char_class == "cleric":
            player_choice = input("Skill proficiencies - Choose two from History, Insight, Medicine, Persuasion, Religion: ").lower()
        elif self.char_class == "druid":
            player_choice = input("Skill proficiencies - Choose two from Arcana, Animal Handling, Insight, Medicine, Nature, Perception, Religion, and Survival: ").lower()
        elif self.char_class == "fighter":
            player_choice = input("Skill proficiencies - Choose two from Acrobatics, Animal Handling, Athletics, History, Insight, Intimidation, Perception, and Survival: ").lower()
        elif self.char_class == "monk":
            player_choice = input("Skill proficiencies - Choose two from Acrobatics, Athletics, History, Insight, Religion, and Stealth: ").lower()
        elif self.char_class == "paladin":
            player_choice = input("Skill proficiencies - Choose two from Athletics, Insight, Intimidation, Medicine, Persuasion, and Religion: ").lower()
        elif self.char_class == "rogue":
            player_choice = input("Skill proficiencies - Choose four from Acrobatics, Athletics, Deception, Insight, Intimidation, Investigation, Perception, Performance, Persuasion, Sleight of Hand, and Stealth: ").lower()
        elif self.char_class == "sorcerer":
            player_choice = input("Skill proficiencies - Choose two from Arcana, Deception, Insight, Intimidation, Persuasion, and Religion: ").lower()
        elif self.char_class == "warlock":
            player_choice = input("Skill proficiencies - Choose two from Arcana, Deception, History, Intimidation, Investigation, Nature, and Religion: ").lower()
        elif self.char_class == "wizard":
            player_choice = input("Skill proficiencies - Choose two from Arcana, History, Insight, Investigation, Medicine, and Religion: ").lower()
        if "acrobatics" in player_choice:
            self.skill_proficiencies["acrobatics"] = True
        if "animal handling" in player_choice:
            self.skill_proficiencies["animal handling"] = True
        if "arcana" in player_choice:
            self.skill_proficiencies["arcana"] = True
        if "athletics" in player_choice:
            self.skill_proficiencies["athletics"] = True
        if "deception" in player_choice:
            self.skill_proficiencies["deception"] = True
        if "history" in player_choice:
            self.skill_proficiencies["history"] = True
        if "insight" in player_choice:
            self.skill_proficiencies["insight"] = True
        if "intimidation" in player_choice:
            self.skill_proficiencies["intimidation"] = True
        if "medicine" in player_choice:
            self.skill_proficiencies["medicine"] = True
        if "nature" in player_choice:
            self.skill_proficiencies["nature"] = True
        if "perception" in player_choice:
            self.skill_proficiencies["perception"] = True
        if "performance" in player_choice:
            self.skill_proficiencies["performance"] = True
        if "persuasion" in player_choice:
            self.skill_proficiencies["persuasion"] = True
        if "religion" in player_choice:
            self.skill_proficiencies["religion"] = True
        if "sleight of hand" in player_choice:
            self.skill_proficiencies["sleight of hand"] = True
        if "stealth" in player_choice:
            self.skill_proficiencies["stealth"] = True
        if "survival" in player_choice:
            self.skill_proficiencies["survival"] = True
        return self.skill_proficiencies
            
class Barbarian:
    def __init__(self):
        self.light_armor_proficiency = True
        self.medium_armor_proficiency = True
        self.shield_proficiency = True
        self.simple_weapons_proficiency = True
        self.martial_weapons_proficiency = True
        return
        
    def rage(self):
        if self.level < 3:
            ragesp_day = 2
        elif self.level >= 3 and self.level <= 5:
            ragesp_day = 3
        elif self.level >= 6 and self.level <= 11:
            ragesp_day = 4
        elif self.level >= 12 and self.level <= 16:
            ragesp_day = 5
        elif self.level >= 17 and self.level <= 19:
            ragesp_day = 6
        else:
            ragesp_day = "Unlimited"
        if self.level >= 1 and self.level <= 8:
            rage_damage = 2
        elif self.level >= 9 and self.level <= 15:
            rage_damage = 3
        elif self.level >= 16:
            rage_damage = 4
        if ragesp_day != 0:
            ask = input("Would you like to rage? ")
            if "y" in ask:
                rage = True
                if self.level < 20:
                    ragesp_day = ragesp_day - 1
            if rage:
              print("You have advantage on Strength checks and saving throws. Use d.roll(2,20,True,True) and select advantage when making those rolls.")  
              print(f"When you make a melee weapon attack while raging and hit, add {rage_damage} to your total damage.")
              self.bludgeoning_resistance = True
              self.piercing_resistance = True
              self.slashing_resistance = True
        if self.hp == 0:
            rage = False
        self.rage = rage
        return self.rage
        
    def unarmored_defense(self):
        ac = 10 + self._ability_mods.get("Dexterity") + self._ability_mods.get("Constitution")
        self.ac = ac
        return self.ac

def main():
    print("Rogues and Bards are op...")
    
if __name__ == '__main__':
    main()