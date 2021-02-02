import pygame

pygame.init()

# generate window
pygame.display.set_caption("Worms")
pygame.display.set_mode((1080, 720))

running = True

# game loop
while running:
    # close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
