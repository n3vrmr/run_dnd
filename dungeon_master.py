# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 14:26:06 2022

@author: Nevermore
"""
import time as t
from player_character import Character

class DungeonMaster:
    def __init__(self):
        game_control = True
        self.game_control = game_control
        self.dm = self.set_dm()
        return
    
    def set_dm(self):
        dm = input("Who will be the Dungeon Master for this Campaign? ")
        self.dm = dm
        print(f"\033[1;35;47m{self.dm} will be the DM.\033[0m")
        return self.dm
    
    def weather_set(self, weather):
        self.weather = weather
        text = f"It is {self.weather} at the moment."
        print(text)
        return self.weather
    
    def ambient_set(self, environment):
        self.environment = environment
        vowels = ["a", "e", "i", "o", "u"]
        split = list(self.environment)
        if split[0] in vowels:
            text = f"You are at an {self.environment}."
        else:
            text = f"You are at a {self.environment}"
        print(text)
        closed_spaces = ["cave", "tavern"]
        if self.environment in closed_spaces:
            self.override_sunlight(False)
        return self.environment
    
    def time_set(self, time):
        self.time = time
        text = f"The time of day is {self.time}"
        print(text)
        convert = int(self.time.replace(":", ""))
        if convert >= 600 and convert <= 1800:
            self.override_sunlight(True)
        else:
            self.override_sunlight(False)
        return self.time
    
    def check_sunlight(self):
        if self.sunlight == True:
            text = "The light of day is shining."
        else:
            text = "There is no daylight to be seen."
        print(text)
        return self.sunlight
    
    def override_sunlight(self, sunlight:bool):
        self.sunlight = sunlight
        self.check_sunlight()
        return self.sunlight
    
    def visibility_set(self):
        pass
    
    def create_npc(self):
        npcs = []
        self.npcs = npcs
        print("Add an NPC to your campaign")
        t.sleep(1.5)
        add = True
        while add:
            add = False
            name = input("Enter the NPC name: ")
            self.name = name
            npc = Character(f"{name}", 0)
            self.npcs.append(npc)
            cont = input("Add another NPC? ").lower().strip()
            if "y" in cont:
                add = True
            else:
                add = False
        return self.npcs
    
    def create_initiative(self):
        pass
    
    def add_to_initiative(self):
        pass
    
    def remove_from_initiative(self):
        pass
    
    def end_initiative(self):
        pass
    
def main():
    print("How do you wanna do this?")
    
if __name__ == '__main__':
    main()