# -*- coding: utf-8 -*-
"""
Created on Wed May  4 18:45:16 2022

@author: Nevermore
"""

import dice as d
import time as t
import d6_roller

class Character:
    """Create a character in the Dungeons & Dragons 5th Edition format.
    """
    def __init__(self, name, level:int, random=False,
                 ability_scores={}, _ability_mods={},
                 proficiency_bonus=0):
        """Sets the initial state for a new character.
        """
        name = input("Character name: ")
        self._name = name
        level = int(input("Character level: "))
        self.level = level
        random = input("Generate random? Reply Y for yes or N for no. ").strip().lower()
        self.random = random
        if "y" in self.random:
            self.random = True
        elif "n" in self.random:
            self.random = False
        r = Race.choosing()
        self.race = r
        advantage = False
        self.advantage = advantage
        disadvantage = False
        self.disadvantage = disadvantage
        self.abilities()
        self.r_asi()
        return
       
    def abilities(self):
        """Allows the player to set their character's ability scores manually,
        then defines the respective ability modifiers according to those values.
        The way the ability modifiers are calculated is as described in the Player's Handbook:
        (ability score - 10), divided by 2 and rounded down.
        In case you chose to generate a random character, the ability scores will be decided for you instead.
        """
        if self.random == True:
            self.ability_scores = {}
            score = True
            while score:
                score = False
                self.ability_scores["Strength"] = d6_roller.ability_rolls()
                self.ability_scores["Dexterity"] = d6_roller.ability_rolls()
                self.ability_scores["Constitution"] = d6_roller.ability_rolls()
                self.ability_scores["Intelligence"] = d6_roller.ability_rolls()
                self.ability_scores["Wisdom"] = d6_roller.ability_rolls()
                self.ability_scores["Charisma"] = d6_roller.ability_rolls()
            t.sleep(1.5)
        
        else:
            print("Enter your ability scores:")
            t.sleep(1.2)
            self.ability_scores = {}
            score = True
            while score:
                score = False
                self.ability_scores["Strength"] = int(input("Strength: "))
                self.ability_scores["Dexterity"] = int(input("Dexterity: "))
                self.ability_scores["Constitution"] = int(input("Constitution: "))
                self.ability_scores["Intelligence"] = int(input("Intelligence: "))
                self.ability_scores["Wisdom"] = int(input("Wisdom: "))
                self.ability_scores["Charisma"] = int(input("Charisma: "))
        return self.ability_scores
    
    def ability_modifiers(self):
        self._ability_mods = {}
        modifier = True
        while modifier:
            modifier = False
            self._ability_mods["Strength"] = (self.ability_scores.get("Strength") - 10)//2
            self._ability_mods["Dexterity"] = (self.ability_scores.get("Dexterity") - 10)//2
            self._ability_mods["Constitution"] = (self.ability_scores.get("Constitution") - 10)//2
            self._ability_mods["Intelligence"] = (self.ability_scores.get("Intelligence") - 10)//2
            self._ability_mods["Wisdom"] = (self.ability_scores.get("Wisdom") - 10)//2
            self._ability_mods["Charisma"] = (self.ability_scores.get("Charisma") - 10)//2
            print("Ability modifiers:",self._ability_mods)
        return self._ability_mods
    
    def increase_one_score(self):
        """
        Method for increasing one of your ability scores by 2 points,
        based on player choice.
        Returns
        -------
        TYPE
            DESCRIPTION.
        """
        choice = input("Choose an ability score to increase by 2: ").strip().lower()
        if "strength" in choice:
            self.ability_scores["Strength"] = self.ability_scores.get("Strength") + 2
        elif "dexterity" in choice:
            self.ability_scores["Dexterity"] = self.ability_scores.get("Dexterity") + 2
        elif "constitution" in choice:
            self.ability_scores["Constitution"] = self.ability_scores.get("Constitution") + 2
        elif "intelligence" in choice:
            self.ability_scores["Intelligence"] = self.ability_scores.get("Intelligence") + 2
        elif "wisdom" in choice:
            self.ability_scores["Wisdom"] = self.ability_scores.get("Wisdom") + 2
        elif "charisma" in choice:
            self.ability_scores["Charisma"] = self.ability_scores.get("Charisma") + 2
        print("Ability scores:",self.ability_scores)
        self.ability_modifiers()
        return self.ability_scores
    
    def increase_two_scores(self):
        """
        Method for increasing two of your ability scores by 1 point,
        based on player choice.
        Returns
        -------
        TYPE
            DESCRIPTION.
        """
        choice = input("Choose two ability scores to increase by 1: ").strip().lower()
        if "strength" in choice:
            self.ability_scores["Strength"] = self.ability_scores.get("Strength") + 1
        if "dexterity" in choice:
            self.ability_scores["Dexterity"] = self.ability_scores.get("Dexterity") + 1
        if "constitution" in choice:
            self.ability_scores["Constitution"] = self.ability_scores.get("Constitution") + 1
        if "intelligence" in choice:
            self.ability_scores["Intelligence"] = self.ability_scores.get("Intelligence") + 1
        if "wisdom" in choice:
            self.ability_scores["Wisdom"] = self.ability_scores.get("Wisdom") + 1
        if "charisma" in choice:
            self.ability_scores["Charisma"] = self.ability_scores.get("Charisma") + 1
        print("Ability scores:",self.ability_scores)
        self.ability_modifiers()
        return self.ability_scores
        
    def proficiency(self):
        """
        Defines your character's proficiency bonus based on their level.
        
        Returns
        -------
        self.ability_scores: a dictionary with your character's abilities as
        the keys, and the scores as the associated values.
        
        """
        if self.level <=4:
            pb = 2
            return pb
        elif self.level >=5 and self.level <=8:
            pb = 3
            return pb
        elif self.level >=9 and self.level <=12:
            pb = 4
            return pb
        elif self.level >=13 and self.level <=16:
            pb = 5
            return pb
        elif self.level >=17 and self.level <=20:
            pb = 6
        self.proficiency_bonus = pb
        return pb
        
    def adv_dis(self):
        """
        Make a roll with either advantage or disadvantage.
        If you have both advantage and disadvantage, they cancel out.
        Advantage and disadvantage do not stack.
        Returns
        -------
        game_situation : the highest roll for advantage and the lowest
        roll for disadvantage.
        """
        if self.advantage == True:
            rolls = d.roll(2,20,True)
            game_situation = max(rolls)
            print("Rolling with advantage:",game_situation)
            if 20 in rolls:
                print("\033[1;32;40mNatural twenty! Critical success!\033[0m")
        elif self.disadvantage == True:
            rolls = d.roll(2,20,True)
            game_situation = min(rolls)
            print("Rolling with disadvantage:",game_situation)
            if 1 in rolls:
                print("\033[1;31;47mUh-oh, natural one! Critical fail!\033[0m")
            elif self.advantage == True and self.disadvantage == True:
                self.advantage == False
                self.disadvantage == False
        return game_situation
        
    
    def r_asi(self):
        if "dwarf" in self.race:
            r = Dwarf
            self.r = r
            Dwarf.dwarf_asi(self)
        elif "elf" in self.race:
            self.ability_scores["Dexterity"] = self.ability_scores.get("Dexterity") + 2
        elif "halfling" in self.race:
            self.ability_scores["Dexterity"] = self.ability_scores.get("Dexterity") + 2
        elif "human" in self.race:
            self.ability_scores["Strength"] = self.ability_scores.get("Strength") + 1
            self.ability_scores["Dexterity"] = self.ability_scores.get("Dexterity") + 1
            self.ability_scores["Constitution"] = self.ability_scores.get("Constitution") + 1
            self.ability_scores["Intelligence"] = self.ability_scores.get("Intelligence") + 1
            self.ability_scores["Wisdom"] = self.ability_scores.get("Wisdom") + 1
            self.ability_scores["Charisma"] = self.ability_scores.get("Charisma") + 1
        elif "dragonborn" in self.race:
            self.ability_scores["Strength"] = self.ability_scores.get("Strength") + 2
            self.ability_scores["Charisma"] = self.ability_scores.get("Charisma") + 1
        elif "gnome" in self.race:
            self.ability_scores["Intelligence"] = self.ability_scores.get("Intelligence") + 2
        elif "halfelf" in self.race or "half-elf" in self.race:
            self.ability_scores["Charisma"] = self.ability_scores.get("Charisma") + 2
            self.increase_two_scores()
        elif "halforc" in self.race or "half-orc" in self.race:
            self.ability_scores["Strength"] = self.ability_scores.get("Strength") + 2
            self.ability_scores["Constitution"] = self.ability_scores.get("Constitution") + 1
        elif "tiefling" in self.race:
            self.ability_scores["Intelligence"] = self.ability_scores.get("Intelligence") + 1
            self.ability_scores["Charisma"] = self.ability_scores.get("Charisma") + 2
        elif "aasimar" in self.race:
            self.ability_scores["Charisma"] = self.ability_scores.get("Charisma") + 2
        elif "goliath" in self.race:
            self.ability_scores["Strength"] = self.ability_scores.get("Strength") + 2
            self.ability_scores["Constitution"] = self.ability_scores.get("Constitution") + 1
        print("Ability scores:",self.ability_scores)
        self.ability_modifiers()
        return self.ability_scores
    
    def unarmed_attack(self):
        to_hit = d.roll(1, 20) + self._ability_mods.get("Strength")
        if to_hit >= 1:
            hit = True
        else:
            hit = False
        if hit:
            print(f"{self._name} rolled {to_hit} to hit")
            damage = d.roll(1, 4) + self._ability_mods.get("Strength")
        print(f"{damage} points of bludgeoning damage")
        return damage
    
class Race:
    def __init__(self, r_asi=True):
        self.race = self.choosing()
        return self.race
    
    def choosing():
        race = input("Choose your character's race: ").lower().strip()
        return race
        
            
class Dwarf:
    def __init__(self):
        self.speed = self.speed()
        self.darkvision = self.darkvision()
        self.dwarven_resilience = self.dwarven_resilience()
        self.dwarven_combat_training = self.dwarven_combat_training()
        self.languages = self.languages()
        return
    
    def speed(self):
        self.speed = 25
        return self.speed
    
    def darkvision(self):
        self.darkvision = True
        self.dv_distance = 60
        text = f"{self._name} can see in dim light within {self.dv_distance} feet of them as if it were bright light, and in darkness as if it were dim light."
        return text
    
    def dwarven_resilience(self):
        self.dwarven_resilience = True
        return self.dwarven_resilience()
    
    def dwarven_combat_training(self):
        self.dwarven_combat_training = True
        
    def languages(self):
        languages = ["Common", "Dwarvish"]
        self.languages = languages
        return self.languages
    
    def dwarf_asi(self):
        if "dwarf" in self.race:
            self.ability_scores["Constitution"] = self.ability_scores.get("Constitution") + 2

c1 = Character("name", 0)

c1.advantage = True
c1.adv_dis()
c1.increase_one_score()
c1.unarmed_attack()
    
c2 = Character("name", 0)

c2.disadvantage = True
c2.adv_dis()
c2.increase_two_scores()
c2.unarmed_attack()


if c2.ability_scores.get("Intelligence") < 10:
    print(f"{c2._name} is not very smart...")
    
print("Proficiency bonus:",c1.proficiency())
print(c1._name,"is ready to rock")

def main():
    print("Not affiliated with Wizards of the Coast LLC")

if __name__ == '__main__':
    main()