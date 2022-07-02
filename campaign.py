# -*- coding: utf-8 -*-
"""
Created on Wed May  4 18:45:16 2022

@author: Nevermore
"""

import time as t
from player_character import Player
from dungeon_master import DungeonMaster

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
    
    def set_characters(self, name, i):
        name = self.players[i].character
        return name
    
    def get_character_name(self, i):
        char_name = self.players[i].character._name
        return char_name
            
            # else:
            #     t.sleep(1.2)
            #     print("Players, create your characters: ")
            #     t.sleep(1.2)
            #     Player.create_character(self)
    
    def player_characters(self):
        pass

c = Campaign()
# for player in c.players:
#     character = c.get_character_name(i)
#      = c.set_characters(f"{c.players[i].character._name}", i)

def main():
    print("Not affiliated with Wizards of the Coast LLC")

if __name__ == '__main__':
    main()