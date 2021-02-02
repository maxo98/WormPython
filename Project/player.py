import pygame

pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('')  # mettre le chemin vers l'image du joueur
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

# Dans la boucle tant que après avoir appliqué la fenetre du jeu :
# appliquer l'image du joueur : screen.blit(game.player.image, game.player.rect)
