from character import Character
from monster import Dragon
from monster import Goblin
from monster import Troll

import random
import os
import sys

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def draw(player, monster, message): 
    clear()

    print(player)
    print(monster)
    print('')
    print(message)


class Game:
    def setup(self):
        self.player = Character()
        self.monsters = [
            Goblin(),
            Troll(),
            Dragon()
        ]
        self.monster = self.get_next_monster()
        self.results = [0, 1]
        clear()

    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None
    
    def get_random_result(self):
        return random.choice(self.results)
    
    def monster_turn(self):
        monster_attack = self.get_random_result()
        if monster_attack:
            print("The monster is attacking!")
            player_dodge = raw_input("Do you want to dodge? Y/n " )
            if player_dodge.lower() == 'y':
                success = self.player.dodge()
                if success:
                    draw(self.player, self.monster, "You dodged the attack!")
                else:
                    self.player.hit_points -= 1
                    draw(self.player, self.monster, "You took a hit!")
        else:
            print("The monster isn't attacking")

    def player_attack(self):
        hit = self.player.attack()
        if hit:
            monster_dodge = self.monster.dodge()
            if monster_dodge:
                draw(self.player, self.monster, "{} dodged your attack!")
            else:
                self.monster.hit_points -= 1
                draw(self.player, self.monster, "You scored a hit on {}")
        else:
            print("You missed!")

    def player_turn(self):
        # let the player attack, rest, or quit
        player_move = raw_input("Do you want to [A]ttack, [R]est or [Q]uit? ").lower()
        # if they attack:
        if player_move in 'arq':
            if player_move == 'a':
                self.player_attack()
            elif player_move == 'r':
                self.player.rest()
            elif player_move == 'q':
                print('Bye')
                sys.exit()
        else:
            self.player_turn()               
                
            # see if the attack is successful
                # if so, see if the monster dodges
                    # if dodged, print that
                    # if not dodged, subtract the right number of hit points from the monster
                # if not a good attack, tell the player
        # if they rest:
            # call the player.rest() method
        # if they quit, exit the game
        # if they pick anything else, re-run this method

    def cleanup(self):
        # if the monster has no more hit points:
        if not self.monster.hit_points:
            self.player.experience += 1
            print('Get ready for the next monster!')
            self.monster = self.get_next_monster()
            # up the player's experience
            # print a message
            # get a new monster
        clear()

    def __init__(self):
        clear()
        self.setup()

        while self.player.hit_points and (self.monster or self.monsters):
            print(self.player)
            print(self.monster)
            print('')
            self.monster_turn()
            self.player_turn()
            self.cleanup()

        if self.player.hit_points:
            print("You win!")
        elif self.monsters or self.monster:
            print("You lose!")

game = Game()
