# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 15:46:19 2022

@author: Nevermore
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
    
    def set_class(self):
        if self.char_class == "barbarian":
            self.c_class = Barbarian
        elif self.char_class == "bard":
            self.c_class = Bard
        elif self.char_class == "cleric":
            self.c_class = Cleric
        elif self.char_class == "druid":
            self.c_class = Druid
        elif self.char_class == "fighter":
            self.c_class = Fighter
        elif self.char_class == "monk":
            self.c_class = Monk
        elif self.char_class == "paladin":
            self.c_class = Paladin
        elif self.char_class == "rogue":
            self.c_class = Rogue
        elif self.char_class == "sorcerer":
            self.c_class = Sorcerer
        elif self.char_class == "warlock":
            self.c_class = Warlock
        elif self.char_class == "wizard":
            self.c_class = Wizard
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
        self.hp_total = hp
        return self.hp_total
    
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
        if self.hp_current == 0:
            rage = False
        self.rage = rage
        return self.rage
        
    def unarmored_defense(self):
        ac = 10 + self._ability_mods.get("Dexterity") + self._ability_mods.get("Constitution")
        self.ac = ac
        return self.ac
    
    def reckless_attack(self):
        if self.level >= 2:
            ra = input("Reckless? ")
            if "y" in ra:
                self.reckless = True
            else:
                self.reckless = False
            if self.reckless == True:
                print("Melee weapon attacks using Strength for this turn made with advantage. Attacks against you have advantage until your next turn.")
        return self.reckless
    
    def danger_sense(self):
        if self.level >= 2:
            print("Advantage on Dex saves against effects you can see. Cannot be blinded, deafened or incapacitated.")
            self.dex_save_adv = True
        return self.dex_save_adv
    
    def extra_attack(self):
        pass
    
    def fast_movement(self):
        if self.level >= 5:
            self.speed = self.speed + 10
        return self.speed
    
    def feral_instinct(self):
        pass
    
    def brutal_critical(self):
        pass
    
    def relentless_rage(self):
        pass
    
    def persistent_rage(self):
        pass
    
    def indomitable_might(self):
        pass
    
    def primal_champion(self):
        if self.level == 20:
            self.ability_scores["Strength"] = self.ability_scores.get("Strength") + 4
            self.ability_scores["Constitution"] = self.ability_scores.get("Constitution") + 4
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
        return self.ability_scores

class Bard:
    def __init__(self):
        self.simple_weapons_proficiency = True
        self.hand_xbow_proficiency = True
        self.longsword_proficiency = True
        self.rapier_proficiency = True
        self.shortsword_proficiency = True
        self.spellcasting = True
        return
    
    def bardic_inspiration(self):
        if self._ability_mods.get("Charisma") < 1:
            self.uses = 1
        else:
            self.uses = self._ability_mods.get("Charisma")
        if self.level < 5:
            inspiration_die = "d6"
        elif self.level >= 5 and self.level < 10:
            inspiration_die = "d8"
        elif self.level >= 10 and self.level < 15:
            inspiration_die = "d10"
        elif self.level >= 15:
            inspiration_die = "d12"
        self.inspiration_die = inspiration_die
        return self.inspiration_die
    
    def inspire(self, character):
        self.inspiration = self.bardic_inspiration()
        self.uses = self.uses - 1
        return self.inspiration
    
    def jack_of_all_trades(self, skill):
        if self.level >= 2:
            if self.skill_proficiencies.get(f"{skill}") == False:
                self.skill_proficiencies[f"{skill}"] = "jack"
            else:
                return self.skill_proficiencies
        return self.skill_proficiencies
            
    def song_of_rest(self):
        if self.level >=2 and self.level < 9:
            sor_die = "1d6"
        elif self.level >= 9 and self.level < 13:
            sor_die = "1d8"
        elif self.level >= 13 and self.level < 17:
            sor_die = "1d10"
        elif self.level >= 17:
            sor_die = "1d12"
        self.sor_die = sor_die
        return self.sor_die
    
    def expertise(self, skill_1, skill_2):
        if self.level >= 3 and self.level < 10:
            if self.skill_proficiencies.get(f"{skill_1}") == True:
                self.skill_proficiencies[f"{skill_1}"] = "expertise"
            if self.skill_proficiencies.get(f"{skill_2}") == True:
                self.skill_proficiencies[f"{skill_2}"] = "expertise"
        elif self.level >= 10:
            if self.skill_proficiencies.get(f"{skill_1}") == True:
                self.skill_proficiencies[f"{skill_1}"] = "expertise"
            if self.skill_proficiencies.get(f"{skill_2}") == True:
                self.skill_proficiencies[f"{skill_2}"] = "expertise"
        return self.skill_proficiencies
    
    def font_of_inspiration(self):
        pass
    
    def countercharm(self):
        pass
    
    def magical_secrets(self):
        pass
    
    def superior_inspiration(self):
        pass
    
class Cleric:
    def __init__(self):
        self.light_armor_proficiency = True
        self.medium_armor_proficiency = True
        self.shield_proficiency = True
        self.simple_weapons_proficiency = True
        self.spellcasting = True
        return
    
    def turn_undead(self):
        pass
    
    def destroy_undead(self):
        pass
    
    def divine_intervention(self):
        if self.level >= 10 and self.level <= 19:
            divine = d.roll(1, 100)
            if divine <= self.level:
                print("Divine intervention was successful...")
            else:
                print("Your deity cannot assist you...")
        return divine
    
class Druid:
    def __init__(self):
        self.light_armor_proficiency = True
        self.medium_armor_proficiency = True
        self.shield_proficiency = True
        self.club_proficiency = True
        self.dagger_proficiency = True
        self.darts_proficiency = True
        self.javelin_proficiency = True
        self.mace_proficiency = True
        self.quarterstaff_proficiency = True
        self.scimitar_proficiency = True
        self.sickle_proficiency = True
        self.sling_proficiency = True
        self.spear_proficiency = True
        self.herbalism_kit_proficiency = True
        self.spellcasting = True
        return
    
    def wild_shape(self):
        self.wild_shape_uses = 2
        max_cr = self.level/8
        if self.level >= 2 and self.level < 4:
            self.limitations = {"Max. CR":max_cr, "Flying Speed":0,
                                "Swimming Speed":0}
        elif self.level >= 4 and self.level < 8:
            self.limitations = {"Max. CR":max_cr, "Flying Speed":0}
        elif self.level >= 8:
            self.limitations = {"Max. CR":max_cr}
        return self.limitations
    
    def use_wild_shape(self, shape):
        self.wild_shape_uses = self.wild_shape_uses - 1
        return self.wild_shape_uses
    
    def timeless_body(self):
        pass
    
    def beast_spells(self):
        pass
    
    def archdruid(self):
        if self.level == 20:
            self.wild_shape_uses = "unlimited"
        return self.wild_shape_uses
    
class Fighter:
    def __init__(self):
        self.light_armor_proficiency = True
        self.medium_armor_proficiency =  True
        self.heavy_armor_proficiency = True
        self.simple_weapons_proficiency = True
        self.martial_weapons_proficiency = True
        return
    
    def fighting_style(self):
        self.style = input("Choose one of the following - Archery, Defense, Dueling, Great Weapon Fighting, Protection, Two-Weapon Fighting: ")
        return self.style
    
    def second_wind(self):
        recover = d.roll(1, 10) + self.level
        if (self.hp_current + recover) > self.hp_total:
            self.hp_current = self.hp_total
        else:
            self.hp_current = self.hp_current + recover
        return self.hp_current
    
    def action_surge(self):
        pass
    
    def extra_attack(self):
        pass
    
    def indomitable(self):
        pass
    
class Monk:
    def __init__(self):
        self.simple_weapons_proficiency = True
        self.shortsword_proficiency = True
        return
    
    def unarmored_defense(self):
        ac = 10 + self._ability_mods.get("Dexterity") + self._ability_mods.get("Wisdom")
        self.ac = ac
        return self.ac
    
    def martial_arts(self):
        if self.level < 5:
            unarmed_strike_dmg = d.roll(1, 4) + self._ability_mods.get("Dexterity")
        elif self.level >= 5 and self.level < 11:
            unarmed_strike_dmg = d.roll(1, 6) + self._ability_mods.get("Dexterity")
        elif self.level >= 11 and self.level < 16:
            unarmed_strike_dmg = d.roll(1, 8) + self._ability_mods.get("Dexterity")
        elif self.level >= 17:
            unarmed_strike_dmg = d.roll(1, 10) + self._ability_mods.get("Dexterity")
        self.unarmed_strike_dmg = unarmed_strike_dmg
        return self.unarmed_strike_dmg
    
    def ki(self):
        if self.level >= 2:
            self.ki_save_dc = 8 + self.proficiency_bonus + self._ability_mods.get("Wisdom")
            self.ki_points = self.level
        return self.ki_save_dc
    
    def flurry_of_blows(self):
        self.ki_points = self.ki_points - 1
        return self.ki_points
    
    def patient_defense(self):
        self.ki_points = self.ki_points - 1
        return self.ki_points
    
    def step_of_the_wind(self):
        self.ki_points = self.ki_points - 1
        return self.ki_points
    
    def deflect_missiles(self):
        if self.level >= 3:
            reduction = d.roll(1, 10) + self._ability_mods.get("Dexterity") + self.level
        if reduction == 0:
            self.ki_points = self.ki_points - 1
        return reduction
    
    def slow_fall(self):
        if self.level >= 4:
            reduction = self.level * 5
        return reduction
    
    def extra_attack(self):
        pass
    
    def stunning_strike(self):
        self.ki_points = self.ki_points - 1
        return self.ki_points
    
    def ki_empowered_strikes(self):
        pass
    
    def evasion(self):
        if self.level >= 7:
            if self.saving_throw >= self.spell_save_dc:
                dmg_taken = 0
            else:
                dmg_taken = self.spell_dmg//2
        self.hp_current = self.hp_current - dmg_taken
        return self.hp_current

    def stillness_of_mind(self):
        pass
    
    def purity_of_body(self):
        self.immunity_poison = True
        self.immunity_disease = True
        return self.immunity_poison, self.immunity_disease
    
    def tongue_of_sun_and_moon(self):
        pass
    
    def diamond_soul(self):
        if self.level >= 14:
            self.save_proficiencies["Constitution"] = True
            self.save_proficiencies["Intelligence"] = True
            self.save_proficiencies["Wisdom"] = True
            self.save_proficiencies["Charisma"] = True
        return self.save_proficiencies
    
    def timeless_body(self):
        pass
    
    def empty_body(self):
        pass
    
class Paladin:
    def __init__(self):
        self.light_armor_proficiency = True
        self.medium_armor_proficiency =  True
        self.heavy_armor_proficiency = True
        self.simple_weapons_proficiency = True
        self.martial_weapons_proficiency = True
        self.spellcasting = True
        return
    
    def divine_sense(self):
        pass
    
    def lay_on_hands(self, healing:int):
        self.total_loh_pool = self.level * 5
        self.current_loh_pool = self.total_loh_pool
        self.current_loh_pool = self.current_loh_pool - healing
        return self.current_loh_pool, self.total_loh_pool
    
    def fighting_style(self):
        self.style = input("Choose one of the following - Defense, Dueling, Great Weapon Fighting, Protection")
        return self.style
    
    def divine_smite(self):
        if self.level >= 2:
            ds_dmg_type = "radiant"
            ds_dmg = d.roll(2, 8)
        print(f"{ds_dmg} points of {ds_dmg_type} damage!")
        return ds_dmg
    
    def divine_health(self):
        self.immunity_disease = True
        return self.immunity_disease
    
    def extra_attack(self):
        pass
    
    def aura_of_protection(self):
        pass
    
    def aura_of_courage(self):
        pass
    
    def improved_divine_smite(self):
        extra_dmg = d.roll(1, 8)
        ds_dmg_type = "radiant"
        return extra_dmg, ds_dmg_type
    
    def cleansing_touch(self):
        pass
    
class Rogue:
    def __init__(self):
        self.light_armor_proficiency = True
        self.simple_weapons_proficiency = True
        self.hand_xbow_proficiency = True
        self.longsword_proficiency = True
        self.rapier_proficiency = True
        self.shortsword_proficiency = True
        self.thieves_tools_proficiency = True
        return
    
    def expertise(self, skill_1, skill_2):
        if self.level >= 1 and self.level < 6:
            if self.skill_proficiencies.get(f"{skill_1}") == True:
                self.skill_proficiencies[f"{skill_1}"] = "expertise"
            if self.skill_proficiencies.get(f"{skill_2}") == True:
                self.skill_proficiencies[f"{skill_2}"] = "expertise"
        elif self.level >= 6:
            if self.skill_proficiencies.get(f"{skill_1}") == True:
                self.skill_proficiencies[f"{skill_1}"] = "expertise"
            if self.skill_proficiencies.get(f"{skill_2}") == True:
                self.skill_proficiencies[f"{skill_2}"] = "expertise"
        return self.skill_proficiencies
    
    def sneak_attack(self):
        if self.level < 3:
            sneak_atk_dmg = d.roll(1, 6)
        elif self.level == 3 or self.level == 4:
            sneak_atk_dmg = d.roll(2, 6)
        elif self.level == 5 or self.level == 6:
            sneak_atk_dmg = d.roll(3, 6)
        elif self.level == 7 or self.level == 8:
            sneak_atk_dmg = d.roll(4, 6)
        elif self.level == 9 or self.level == 10:
            sneak_atk_dmg = d.roll(5, 6)
        elif self.level == 11 or self.level == 12:
            sneak_atk_dmg = d.roll(6, 6)
        elif self.level == 13 or self.level == 14:
            sneak_atk_dmg = d.roll(7, 6)
        elif self.level == 15 or self.level == 16:
            sneak_atk_dmg = d.roll(8, 6)
        elif self.level == 17 or self.level == 18:
            sneak_atk_dmg = d.roll(9, 6)
        elif self.level == 19 or self.level == 20:
            sneak_atk_dmg = d.roll(10, 6)
        print(f"\033[1;31;47mSneak attack! {sneak_atk_dmg} points of damage!")
        return sneak_atk_dmg
    
    def thieves_cant(self):
        pass
    
    def cunning_action(self):
        pass
    
    def uncanny_dodge(self):
        pass
    
    def evasion(self):
        if self.level >= 7:
            if self.saving_throw >= self.spell_save_dc:
                dmg_taken = 0
            else:
                dmg_taken = self.spell_dmg//2
        self.hp_current = self.hp_current - dmg_taken
        return self.hp_current
    
    def reliable_talent(self, skill):
        pass
    
    def blindsense(self):
        pass
    
    def slippery_mind(self):
        if self.level >= 15:
            self.save_proficiencies["Wisdom"] = True
        return self.save_proficiencies
    
    def elusive(self):
        pass
    
    def stroke_of_luck(self):
        pass
    
class Sorcerer:
    def __init__(self):
        self.dagger_proficiency = True
        self.darts_proficiency = True
        self.sling_proficiency = True
        self.quarterstaff_proficiency = True
        self.light_xbow_proficiency = True
        self.spellcasting = True
        return
    
    def font_of_magic(self):
        if self.level >= 2:
            self.sorcery_points = self.level
        # flexible_casting
        return self.sorcery_points
    
    def metamagic(self):
        metamagic = ["Careful Spell", "Distant Spell", "Empowered Spell",
                     "Extended Spell", "Heightened Spell", "Quickened Spell", 
                     "Subtle Spell", "Twinned Spell"]
        if self.level >= 3 and self.level < 17:
            choice = input(f"Choose two of the following - {metamagic}: ")
            return choice
        elif self.level >= 17:
            new_choice = input(f"Choose another metamagic option - {metamagic}: ")
            return new_choice
        
    def sorcerous_restoration(self):
        pass
    
class Warlock:
    def __init__(self):
        self.light_armor_proficiency = True
        self.simple_weapons_proficiency = True
        self.spellcasting = True
        return
    
    def eldritch_invocations(self):
        if self.level >= 2:
            pass
    
    def pact_boon(self):
        pass
    
    def mystic_arcanum(self):
        pass
    
    def eldritch_master(self):
        pass
    
class Wizard:
    def __init__(self):
        self.dagger_proficiency = True
        self.darts_proficiency = True
        self.sling_proficiency = True
        self.quarterstaff_proficiency = True
        self.light_xbow_proficiency = True
        self.spellcasting = True
        return
    
    def arcane_recovery(self):
        pass
    
    def spell_mastery(self):
        pass
    
    def signature_spells(self):
        pass

def main():
    print("Rogues and Bards are op...")
    
if __name__ == '__main__':
    main()