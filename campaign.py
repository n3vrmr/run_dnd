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
        return self.players
            
            # else:
            #     t.sleep(1.2)
            #     print("Players, create your characters: ")
            #     t.sleep(1.2)
            #     Player.create_character(self)
    
    def player_characters(self):
        pass
    
    # def unarmed_attack(self):
    #     to_hit = d.roll(1, 20) + self._ability_mods.get("Strength")
    #     if to_hit >= 0:
    #         hit = True
    #     else:
    #         hit = False
    #     if hit:
    #         print(f"{self._name} rolled {to_hit} to hit")
    #         damage = d.roll(1, 4) + self._ability_mods.get("Strength")
    #     print(f"{damage} points of bludgeoning damage")
    #     return damage

c = Campaign()

def main():
    print("Not affiliated with Wizards of the Coast LLC")

if __name__ == '__main__':
    main()