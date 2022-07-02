# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 19:50:49 2022

@author: Nevermore
"""

import dice as d
import time as t
import spell_cast
from classes import Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Rogue, Sorcerer, Warlock, Wizard

class Subclasses:
    def choosing_subclass(self):
        level_1 = ["cleric", "sorcerer", "warlock"]
        level_2 = ["druid", "wizard"]
        level_3 = ["barbarian", "bard", "fighter", "monk", "paladin", "rogue"]
        if self.char_class in level_1 and self.level >= 1:
            char_subclass = input("Choose your subclass: ").strip().lower()
        elif self.char_class in level_2 and self.level >= 2:
            char_subclass = input("Choose your subclass: ").strip().lower()
        elif self.char_class in level_3 and self.level >= 3:
            char_subclass = input("Choose your subclass: ").strip().lower()
        else:
            char_subclass = "None"
        self.char_subclass = char_subclass
        return self.char_subclass
    
    def set_subclass(self):
        if "berserker" in self.char_subclass:
            self.c_subclass = PathOfTheBerserker
        elif "tragedy" in self.char_subclass:
            self.c_subclass = CollegeOfTragedy
        elif "light" in self.char_subclass:
            self.c_subclass = LightDomain
        elif "moon" in self.char_subclass:
            self.c_subclass = CircleOfTheMoon
        elif "champion" in self.char_subclass:
            self.c_subclass = Champion
        elif "open hand" in self.char_subclass:
            self.c_subclass = WayOfTheOpenHand
        elif "vengeance" in self.char_subclass:
            self.c_subclass = OathOfVengeance
        elif "assassin" in self.char_subclass:
            self.c_subclass = Assassin
        elif "wild magic" in self.char_subclass:
            self.c_subclass = WildMagic
        elif "fiend" in self.char_subclass:
            self.c_subclass = TheFiend
        elif "evocation" in self.char_subclass:
            self.c_subclass = SchoolOfEvocation
        else:
            return self.char_subclass
        return self.c_subclass

class PathOfTheBerserker(Barbarian):
    def frenzy(self):
        pass
    
    def mindless_rage(self):
        pass
    
    def intimidating_presence(self):
        pass
    
    def retaliation(self):
        pass

class CollegeOfTragedy(Bard):
    def poetry_in_misery(self):
        pass
    
    def sorrowful_fate(self):
        pass
    
    def tale_of_hubris(self):
        pass
    
    def impending_misfortune(self):
        pass
    
    def nimbus_of_pathos(self):
        pass

class LightDomain(Cleric):
    def bonus_cantrip(self):
        cantrip = "light"
        return cantrip
    
    def warding_flare(self):
        pass
    
    def radiance_of_the_dawn(self):
        if self.level >= 2:
            dmg = d.roll(2, 10) + self.level
            dmg_type = "radiant"
            text = f"{dmg} points of {dmg_type} damage!"
            print(text)
        return dmg
    
    def improved_flare(self):
        pass
    
    def potent_spellcasting(self):
        pass
    
    def corona_of_light(self):
        pass
    
class CircleOfTheMoon(Druid):
    def combat_wild_shape(self):
        pass
    
    def circle_forms(self):
        pass
    
    def primal_strike(self):
        pass
    
    def elemental_wild_shape(self):
        pass
    
    def thousand_forms(self):
        pass
    
class Champion(Fighter):
    def improved_critical(self):
        print("Critical at 19")
        return
    
    def remarkable_athlete(self):
        pass
    
    def additional_fighting_style(self):
        pass
    
    def superior_critical(self):
        pass
    
    def survivor(self):
        if self.level >= 18:
            if self.hp_current <= self.hp_total//2:
                regain = 5 + self._ability_mods.get("Constitution")
                self.hp_current = self.hp_current + regain
        return self.hp_current
    
class WayOfTheOpenHand(Monk):
    def open_hand_technique(self):
        pass
    
    def wholeness_of_body(self):
        if self.level >= 6:
            regain = self.level * 3
            heal = self.hp_current + regain
            if heal > self.hp_total:
                self.hp_current = self.hp_total
            else:
                self.hp_current = heal
        return self.hp_current
    
    def tranquility(self):
        if self.level >= 11:
            save_dc = 8 + self._ability_mods.get("Wisdom") + self.proficiency_bonus
            return save_dc
    
    def quivering_palm(self):
        if self.level >= 17:
            days = self.level
            dmg = d.roll(10, 10)
            dmg_type = "necrotic"
            text = f"{dmg} points of {dmg_type} damage!"
            print(text)
            return dmg
        
class OathOfVengeance(Paladin):
    def channel_divinity(self, option):
        if option == "abjure enemy":
            pass
        elif option == "vow of enmity":
            pass
        
    def relentless_avenger(self):
        pass
    
    def soul_of_vengeance(self):
        pass
    
    def avenging_angel(self):
        pass
    
class Assassin(Rogue):
    def bonus_proficiencies(self):
        self.disguise_kit_proficiency = True
        self.poisoner_kit_proficiency = True
        return
    
    def assassinate(self):
        pass
    
    def infiltration_expertise(self):
        pass
    
    def impostor(self):
        pass
    
    def death_strike(self):
        if self.level >= 17:
            death_strike_dc = 8 + self._ability_mods.get("Dexterity") + self.proficiency_bonus
        return death_strike_dc
    
class WildMagic(Sorcerer):
    def wild_magic_surge(self):
        roll = d.roll(1, 20)
        if roll == 1:
            chance = d.roll(1, 100)
            t.sleep(1.2)
            if chance == 1 or chance == 2:
                print("Roll again for the next minute, ignore these results")
            elif chance == 3 or chance == 4:
                print("You can see inivisible creatures in line of sight")
            elif chance == 5 or chance == 6:
                print("A Modron appears")
            elif chance == 7 or chance == 8:
                spell_cast.fireball(3)
                print("Fireball centered on yourself")
            elif chance == 9 or chance == 10:
                spell_cast.magic_missile(5)
                print("Magic missile 5th level")
            elif chance == 11 or chance == 12:
                height = d.roll(1, 10)
                print(f"Height changes {height} inches")
            elif chance == 13 or chance == 14:
                # cast("confusion")
                print("Confusion centered on yourself")
            elif chance == 15 or chance == 16:
                regain = 5
                heal = self.hp_current + regain
                if heal > self.hp_total:
                    self.hp_current = self.hp_total
                else:
                    self.hp_current = heal
                return self.hp_current
            elif chance == 17 or chance == 18:
                print("Grow a beard of feathers")
            elif chance == 19 or chance == 20:
                # cast("grease")
                print("Grease centered on yourself")
            elif chance == 21 or chance == 22:
                print("Disadvantage against your spells")
            elif chance == 23 or chance == 24:
                print("Skin turns blue")
            elif chance == 25 or chance == 26:
                print("Eye on the forehead")
            elif chance == 27 or chance == 28:
                print("1 action spells -> 1 bonus action")
            elif chance == 29 or chance == 30:
                print("Teleport up to 60 feet")
            elif chance == 31 or chance == 32:
                print("Transported to Astral Plane until next turn")
            elif chance == 33 or chance == 34:
                print("Next spell has maximum damage")
            elif chance == 35 or chance == 36:
                age = d.roll(1, 10)
                print(f"Your age changes by {age} years.")
            elif chance == 37 or chance == 38:
                flumphs = d.roll(1, 6)
                print(f"{flumphs} flumphs appear!")
            elif chance == 39 or chance == 40:
                regain = d.roll(2, 10)
                heal = self.hp_current + regain
                if heal > self.hp_total:
                    self.hp_current = self.hp_total
                else:
                    self.hp_current = heal
                return self.hp_current
            elif chance == 41 or chance == 42:
                print("Turn into a potted plant until next turn")
            elif chance == 43 or chance == 44:
                print("Teleport up to 20 feet as bonus action for 1 minute")
            elif chance == 45 or chance == 46:
                # spell_cast.levitate()
                pass
            elif chance == 47 or chance == 48:
                print("An unicorn appears!")
            elif chance == 49 or chance == 50:
                print("Can't speak, only pink bubbles for 1 minute")
            elif chance == 51 or chance == 52:
                self.ac = self.ac + 2
                print("Immune to magic missile")
                return self.ac
            elif chance == 53 or chance == 54:
                alcohol_immunity = d.roll(5, 6)
                print(f"Immune to alcohol intoxication for {alcohol_immunity} days.")
            elif chance == 55 or chance == 56:
                print("Hair falls out, back in 24h.")
            elif chance == 57 or chance == 58:
                print("Midas touch, but it's fire instead of gold (if object is flammable, not being worn or carried)")
            elif chance == 59 or chance == 60:
                print("Regain lowest level spell slot")
            elif chance == 61 or chance == 62:
                print("Shout when you speak for the next minute")
            elif chance == 63 or chance == 64:
                # spell_cast.fog_cloud()
                pass
            elif chance == 65 or chance == 66:
                bolts = []
                for i in range(0,3):
                    dmg = d.roll(4, 10)
                    bolts.append(dmg)
                dmg_type = "lightning"
                text = f"Up to 3 creatures within 30 feet of you take {bolts} points of {dmg_type} damage!"
                print(text)
                return sum(bolts)
            elif chance == 67 or chance == 68:
                print("Frightened by the nearest creature until next turn")
            elif chance == 69 or chance == 70:
                print("Every creature within 30 feet turns invisible")
            elif chance == 71 or chance == 72:
                print("Resistance to all damage for 1 minute")
            elif chance == 73 or chance == 74:
                poison = d.roll(1, 4)
                print(f"Creature within 60 feet of you is poisoned for {poison} hours")
            elif chance == 75 or chance == 76:
                print("Glow for 30 feet. Turn end within 5 feet blinds")
            elif chance == 77 or chance == 78:
                # spell_cast.polymorph(sheep)
                pass
            elif chance == 79 or chance == 80:
                print("Illusory butterflies and petals for 10 minutes")
            elif chance == 81 or chance == 82:
                print("1 extra action immediately")
            elif chance == 83 or chance == 84:
                creatures = []
                within_radius = True
                while within_radius:
                    names = input("Write the name of creature within 30 feet: ").lower().strip()
                    creatures.append(names)
                    ask = input("Are there more creatures in range? ").lower().strip()
                    if "y" in ask:
                        within_radius = True
                    elif "n" in ask:
                        within_radius = False
                for i in range(0, len(creatures)):
                    life = []
                    dmg = d.roll(1, 10)
                    life.append(dmg)
                dmg_type = "necrotic"
                text = f"Dark energy strikes for {life} points of {dmg_type} damage!"
                print(text)
                print("Total damage:", sum(life))
                regain = sum(life)
                heal = self.hp_current + regain
                if heal > self.hp_total:
                    self.hp_current = self.hp_total
                else:
                    self.hp_current = heal
                return self.hp_current
            elif chance == 85 or chance == 86:
                # spell_cast.mirror_image()
                pass
            elif chance == 87 or chance == 88:
                # spell_cast.fly()
                pass
            elif chance == 89 or chance == 90:
                print("Become invisible for 1 minute. No one can hear you.")
            elif chance == 91 or chance == 92:
                print("Uno reverse card on death for 1 minute")
                # spell_cast.reincarnate()
            elif chance == 93 or chance == 94:
                print("Size category increased by one for 1 minute")
            elif chance == 95 or chance == 96:
                print("You and creatures within 30 feet vulnerable to piercing damage for 1 minute")
            elif chance == 97 or chance == 98:
                print("Surrounded by faint, ethereal music for 1 minute")
            elif chance == 99 or chance == 100:
                print("Regain all sorcery points")
            return
    
    def tides_of_chaos(self):
        pass
    
    def bend_luck(self):
        alter = d.roll(1, 4)
        return alter
    
    def controlled_chaos(self):
        pass
    
    def spell_bombardment(self):
        pass
    
class TheFiend(Warlock):
    def expanded_spell_list(self):
        pass
    
    def dark_blessing(self):
        self.hp_temp = self.level + self._ability_mods.get("Charisma")
        return self.hp_temp
    
    def dark_own_luck(self):
        pass
    
    def fiendish_resilience(self):
        pass
    
    def hurl_through_hell(self):
        dmg = d.roll(10, 10)
        dmg_type = "psychic"
        text = f"{dmg} points of {dmg_type} damage!"
        print(text)
        return dmg
    
class SchoolOfEvocation(Wizard):
    def evocation_savant(self):
        pass
    
    def sculpt_spells(self):
        pass
    
    def potent_cantrip(self):
        pass
    
    def empowered_evocation(self):
        pass
    
    def overchannel(self):
        pass
    
def main():
    print("THE SPINNING WHEEL OF WILD MAGIC!")

if __name__ == '__main__':
    main()