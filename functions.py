import sys
import pygame

pygame.init()

def update_screen(game_settings, screen):
    screen.fill(game_settings.bg_colour)
    pygame.display.flip()