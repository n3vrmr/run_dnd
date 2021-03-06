# -*- coding: utf-8 -*-
"""
Created on Wed May  4 18:45:16 2022

@author: Nevermore
"""

from IPython.display import display
import pandas as pd
import time as t
from player_character import Player
from dungeon_master import DungeonMaster
from monster import Beholder

class Campaign:
    def __init__(self):
        dm = DungeonMaster()
        self.dm = dm
        self.add_players()
        return
    
    def add_players(self):
        players = []
        self.players = players
        t.sleep(1.5)
        print("Add a player to your campaign")
        t.sleep(1.5)
        add = True
        while add:
            add = False
            name = input("Enter the player name: ")
            player = Player(f"{name}")
            self.players.append(player)
            cont = input("Add another player? ").lower().strip()
            if "y" in cont:
                add = True
            else:
                add = False
        for i in range(0,len(self.players)):
            print(f"{self.players[i].name} has joined the campaign as {self.players[i].character._name}, a {self.players[i].character.race} {self.players[i].character.char_class}!")
            globals()[f'{self.players[i].character._name}'] = self.players[i].character
        return self.players
    
    def create_initiative(self):
        self.initiative_values = []
        self.characters = []
        for i in range(0,len(self.players)):
            name = self.players[i].character._name
            print(f"Initiative for {name}")
            value = self.players[i].character.initiative()
            self.initiative_values.append(value)
            self.characters.append(name)
        open_initiative = pd.DataFrame({"Character":self.characters,
                                        "Initiative":self.initiative_values})
        self.initiative = open_initiative.sort_values("Initiative", ascending=False)
        display(self.initiative)
        return
    
    def initiative_add_monsters(self, monster):
        print(f"Initiative for {monster}")
        if monster == "Beholder":
            self.beholder = Beholder()
            monster_initiative = self.beholder.initiative()
            add_to_initiative = pd.DataFrame({"Character":"Beholder",
                                              "Initiative":monster_initiative}, index=[0])
        concat = pd.concat([self.initiative, add_to_initiative], ignore_index=True)
        ordered = concat.sort_values("Initiative", ascending=False)
        self.initiative = ordered
        display(self.initiative)
        return
    
    def start_combat(self):
        self.combat = True
        while self.combat:
            for character in self.initiative["Character"]:
                print(f"{character}'s turn \n")
                ask = input(f"{character}, what would you like to do?\n")
                if ask == "End.":
                    break
                    self.combat = False
        
    def get_character_name(self, i):
        char_name = self.players[i].character._name
        return char_name

c = Campaign()

def main():
    print("Not affiliated with Wizards of the Coast LLC")

if __name__ == '__main__':
    main()