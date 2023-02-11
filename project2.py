#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        import random
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        pick = ""
        while pick not in moves:
            pick = input("Rock, Paper, Scissors? ")
        return pick


class ReflectPlayer(Player):
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        if their_move == 'paper':
            return 'paper'
        elif their_move == 'scissors':
            return 'scissors'
        elif their_move == 'rock':
            return 'rock'


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move_p1 = self.p1.move()
        move_p2 = self.p2.move()
        if beats(move_p1, move_p2):
            self.p1_score += 1
            print("Player 1 win this round!")
        elif beats(move_p2, move_p1):
            self.p2_score += 1
            print("Player 2 win this round!")
        else:
            print("Tie Round")
        print(f"Player 1: {move_p1}  Player 2: {move_p2}")
        self.p1.learn(move_p1, move_p2)
        self.p2.learn(move_p2, move_p1)

    def play_game(self):
        print("Game start!")
        self.p1_score = 0
        self.p2_score = 0
        for round in range(1, 99):
            print(f"Round {round}:")
            self.play_round()
            if self.p1_score == 3:
                print("wow! Player1 just win!!!")
                break
            elif self.p2_score == 3:
                print("wow! Player2 just win!!!")
                break
            print(f"Score- Player1: {self.p1_score}, Player2: {self.p2_score}")
        print(f"Score- Player1: {self.p1_score}, Player2: {self.p2_score}")
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()