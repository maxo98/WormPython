import pygame
from player import Player
import random


class Game:
    def __init__(self):
        # generate players
        self.player1 = Player(self, 1, 'Assets/player1.png', 50)
        self.player2 = Player(self, 2, 'Assets/player2.png', 1000)
        self.wind_force = random.random()
        self.pressed = {}
        self.turn_timer = 30000

    def check_collisionWithRocket(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def check_collision(self, player1, player2):
        return player1.rect.x <= player2.rect.x <= player1.rect.x + player1.rect.width

    def check_end_game(self):
        if self.player1.health <= 0:
            print('player 2 win !')
            return True
        elif self.player1.health <= 0:
            print('player 1 win !')
            return True
        return False
