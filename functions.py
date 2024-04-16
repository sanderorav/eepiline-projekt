import sys
import pygame

pygame.init()

def update_screen(game_settings, screen):
    screen.fill(game_settings.bg_colour)
    pygame.display.flip()
    
def check_events(game_settings, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()