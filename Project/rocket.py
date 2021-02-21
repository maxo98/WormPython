import pygame
import mathLibrary
import math


class Rocket(pygame.sprite.Sprite):
    def __init__(self, player, force, start_position, angle, wind_force, mouse_pos, direction):
        super().__init__()
        self.player = player
        self.max_force = 10
        self.damage = 20
        self.force = force * self.max_force
        print('force ' + str(self.force))
        self.image = pygame.image.load('Assets/rocket1.png')
        self.rect = self.image.get_rect()
        self.rect.x = start_position.x
        self.rect.y = start_position.y
        self.angle = angle
        self.start_time = pygame.time.get_ticks()
        self.wind_force = wind_force
        self.mouse_pos = mouse_pos
        self.direction = direction

    def move(self, surface):
        current_time = pygame.time.get_ticks() - self.start_time
        y = math.tan(self.angle) * self.force
        speed = [self.force, y]
        currentPos = mathLibrary.noWindPath(self.rect, speed, self.angle,
                                            current_time / 1000)
        # self.rect.x = currentPos[0]
        # self.rect.y = currentPos[1]

        if self.direction:
            self.rect.x -= self.force
        else:
            self.rect.x += self.force

        if self.player.player == 1:
            if self.player.game.check_collision(self, self.player.game.player2):
                self.player.game.player2.health -= self.damage
                self.remove()
        if self.player.player == 2:
            if self.player.game.check_collision(self, self.player.game.player1):
                self.player.game.player1.health -= self.damage
                self.remove()

        if self.rect.x + self.rect.width < 0 or self.rect.y + self.rect.height < 0 or self.rect.x > surface.get_width()\
                or self.rect.y > surface.get_height():
            self.remove()

    def remove(self):
        self.player.all_rockets.remove(self)