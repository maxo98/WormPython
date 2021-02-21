import pygame
from rocket import Rocket
from grenade import Grenade
import math

pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, game, player, image_path, init_x):
        super().__init__()
        self.game = game
        self.player = player
        self.health = 100
        self.max_health = 100
        self.velocity = 3
        self.all_rockets = pygame.sprite.Group()
        self.all_grenades = pygame.sprite.Group()
        self.direction = True
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = init_x
        self.rect.y = 540

    def update_health_bar(self, surface):
        bar_color = (111, 210, 46)
        back_color = (90, 122, 78)
        bar_position = [self.rect.x - 10, self.rect.y - 20, self.health, 5]
        back_position = [self.rect.x - 10, self.rect.y - 20, self.max_health, 5]
        pygame.draw.rect(surface, back_color, back_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def rocket_launch(self, time_before_launch, mouse_pos, wind_force):
        if time_before_launch > 2000:
            time_before_launch = 2000
        rocker_launch_force = time_before_launch / 2000
        projectile_start_position = pygame.math.Vector2(self.rect.x + (self.rect.width / 2),
                                                        self.rect.y + (self.rect.height / 2))
        angle = math.atan2(mouse_pos[0] - projectile_start_position[0],
                           mouse_pos[1] - projectile_start_position[1])

        self.all_rockets.add(Rocket(self, rocker_launch_force, projectile_start_position, angle, wind_force,
                                    mouse_pos, self.direction))

    def grenade_launch(self, time_before_launch, mouse_pos):
        if time_before_launch > 2000:
            time_before_launch = 2000
        grenade_launch_force = time_before_launch / 2000
        projectile_start_position = pygame.math.Vector2(self.rect.x + (self.rect.width / 2),
                                                        self.rect.y + (self.rect.height / 2))
        angle = math.atan2(mouse_pos[0] - projectile_start_position[0],
                           mouse_pos[1] - projectile_start_position[1])

        self.all_grenades.add(Grenade(self, grenade_launch_force, projectile_start_position, angle,
                                      mouse_pos, self.direction))

    def move_right(self):
        self.rect.x += self.velocity
        if self.player == 1:
            if self.game.check_collision(self, self.game.player2):
                self.rect.x = self.game.player2.rect.x - self.rect.width
        if self.player == 2:
            if self.game.check_collision(self, self.game.player1):
                self.rect.x = self.game.player1.rect.x - self.rect.width
        if self.direction:
            self.image = pygame.transform.flip(self.image, True, False)
        self.direction = False

    def move_left(self):
        self.rect.x -= self.velocity
        if self.player == 1:
            if self.game.check_collision(self, self.game.player2):
                self.rect.x = self.game.player2.rect.x + self.game.player2.rect.width + self.rect.width
        if self.player == 2:
            if self.game.check_collision(self, self.game.player1):
                self.rect.x = self.game.player1.rect.x + self.game.player1.rect.width + self.rect.width
        if not self.direction:
            self.image = pygame.transform.flip(self.image, True, False)
        self.direction = True
