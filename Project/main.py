import pygame
from game import Game

pygame.init()

# generate window
pygame.display.set_caption("Worms")
screen = pygame.display.set_mode((1080, 720))

pygame.time.Clock()

# load game
game = Game()

# import background
background = pygame.image.load('Assets/background.png')
color = (25, 51, 0)

running = True
player_turn = 1
time_at_player_turn = 0
rocket_time_pressed = 0

# game loop
while running:
    delta_time = pygame.time.get_ticks()
    if delta_time > time_at_player_turn + game.turn_timer:
        if player_turn == 1:
            print(' player 2 turn ')
            player_turn = 2

        else:
            print(' player 2 turn ')
            player_turn = 1
        time_at_player_turn = delta_time

    if game.check_end_game():
        running = False
        pygame.quit()

    # draw background
    screen.blit(background, (0, -300))
    pygame.draw.rect(screen, color, pygame.Rect(0, 600, 1080, 120))

    # draw players
    screen.blit(game.player1.image, game.player1.rect)
    screen.blit(game.player2.image, game.player2.rect)

    # update and draw rockets
    for projectile in game.player1.all_rockets:
        projectile.move(screen)

    game.player1.all_rockets.draw(screen)

    for projectile in game.player2.all_rockets:
        projectile.move(screen)

    game.player2.all_rockets.draw(screen)

    # draw and update health bars
    game.player1.update_health_bar(screen)
    game.player2.update_health_bar(screen)

    # move players
    if game.pressed.get(pygame.K_d):
        if player_turn == 1 and game.player1.rect.x + game.player1.rect.width < screen.get_width():
            game.player1.move_right()
        elif player_turn == 2 and game.player2.rect.x + game.player2.rect.width < screen.get_width():
            game.player2.move_right()
    elif game.pressed.get(pygame.K_q):
        if player_turn == 1 and game.player1.rect.x > 0:
            game.player1.move_left()
        elif player_turn == 2 and game.player2.rect.x > 0:
            game.player2.move_left()

    # update screen
    pygame.display.flip()

    # close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # inputs
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_a:
                rocket_time_pressed = pygame.time.get_ticks()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

            if event.key == pygame.K_a and rocket_time_pressed != 0:
                if player_turn == 1:
                    game.player1.rocket_launch(pygame.time.get_ticks() - rocket_time_pressed,
                                               pygame.mouse.get_pos(), game.wind_force)
                    player_turn = 2
                else:
                    game.player2.rocket_launch(pygame.time.get_ticks() - rocket_time_pressed,
                                               pygame.mouse.get_pos(), game.wind_force)
                    player_turn = 1
                time_at_player_turn = delta_time
                rocket_time_pressed = 0
