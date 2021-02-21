import pygame
import mathLibrary
import math

class Grenade(pygame.sprite.Sprite):
    def __init__(self, player, force, start_position, angle,mouse_pos, direction):
        super().__init__()
        self.player = player
        self.max_force = 5
        self.damage = 40
        self.force = force * self.max_force
        print('force ' + str(self.force))
        self.image = pygame.image.load('Assets/grenade1.png')
        self.rect = self.image.get_rect()
        self.rect.x = start_position.x
        self.rect.y = start_position.y
        self.angle = angle
        self.start_time = pygame.time.get_ticks()
        self.mouse_pos = mouse_pos
        self.direction = direction

    def move(self, surface):
        current_time = pygame.time.get_ticks() - self.start_time/ 1000
        magnitude = math.sqrt(math.pow((self.rect.x + self.force), 2) + math.pow((self.rect.y + self.force), 2))
        direction = [(self.rect.x / magnitude), (self.rect.y / magnitude)]
        speed = [self.force * direction[0], self.force * direction[1]]
        currentPos = mathLibrary.noWindPath(self.rect, speed, self.angle,
                                            current_time)

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
                or self.rect.y + self.rect.height > 600:
            self.remove()

    def remove(self):
        self.player.all_grenades.remove(self)