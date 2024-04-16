import pygame
from settings import Settings
import functions as func

def run_game():
    pygame.init()
    gm_settings = Settings()

    screen = pygame.display.set_mode([gm_settings.screen_width, gm_settings.screen_height])
    pygame.display.set_caption(gm_settings.caption)
    
    while True:
        func.check_events(gm_settings, screen)
        func.update_screen(gm_settings, screen)
    
run_game()