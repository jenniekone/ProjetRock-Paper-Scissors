# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 17:33:01 2018
@author: Jennie
"""
import random

moves = ['rock', 'paper', 'scissors']


# Create player class
class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# Create random player class
class RandomPlayer:
    def __init__(self):
        Player.__init__(self)

    def move(self):
        # use imported random function & choice
        choices = ['rock', 'paper', 'scissors']
        random_player = random.choice(choices)
        # Computer choice is either rock, paper, or scissors
        if random_player == ("rock"):
            print("Opponent played rock")

        elif random_player == ("paper"):
            print("Opponent played paper")

        else:
            print("Opponent played scissors")

        # return value
        return random_player


# Create human player class
class HumanPlayer:
    def __init__(self):
        Player.__init__(self)

    def move(self):
        while True:
            human_player = input("'rock', 'paper', or 'scissors' ")
        # Detect invalid entry
            if human_player.lower() not in moves:
                print('Please choose EITHER paper, rock or scissors')
            else:
                break

        return human_player


# class that remembers what move the opponent played last round
class ReflectPlayer:
    def __init__(self, ReflectPlayer):
        Player.__init__(self)
        self.ReflectPlayer = ReflectPlayer

    # def move
    def move(self, move):
        self.move = move

    def getmove(self, move):
        return self.move


# define cycleplayer class that remembers what move it played last round,
# and cycles through the different moves.
class CyclePlayer:
    def __init__(self, CyclePlayer):
        Player.__init__(self)
        self.CyclePlayer = CyclePlayer
        # stores the frequency of human player moves
        self.human_player_history = {}
        for move in moves:
            self.human_player_history[move] = 0

    def move(self, max_move):
        max_move = max(self.human_player_history.items(), key=lambda elem: elem[1])[0]
        if max_move == 'rock':
            return 'paper'
        if max_move == 'scissors':
            return 'rock'
        if max_move == 'paper':
            return 'rock'


def beats(move1, move2):
    if ((move1 == 'rock' and move2 == 'scissors') or

        (move1 == 'scissors' and move2 == 'paper') or

        (move1 == 'paper' and move2 == 'rock')):

        return "** Human WINS **"

    else:

        return "** Opponent WINS **"


# Create game class
class Game:
    def __init__(self, human_player, random_player):
        self.player1 = human_player
        self.player2 = random_player
        self.player1_score = 0
        self.player2_score = 0

    def play_round(self):
        move1 = self.player1.move()
        move2 = self.player2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        if (move1 == move2):
            print("it's a tie!")

        elif beats(move1, move2):
            self.player1_score += 1
            print("Human Wins this round!")

        elif beats(move2, move1):
            self.player2_score += 1
            print("RandomPlayer Wins this round!")

        print(f"Scores, HumanPlayer: {self.player1_score} RandomPlayer: {self.player2_score}")

    def play_game(self):
        print("Game start!")
        for round in range(4):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()