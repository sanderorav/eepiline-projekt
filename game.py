import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from player import Player
from coin import Coin
from robber import Robber
import functions as func

def run_game():
    pygame.init()
    gm_settings = Settings()

    screen = pygame.display.set_mode([gm_settings.screen_width, gm_settings.screen_height])
    pygame.display.set_caption(gm_settings.caption)
    
    clock = pygame.time.Clock()
    
    stats = GameStats()
    
    sb = Scoreboard(gm_settings, screen, stats)
    
    player = Player(screen)
    
    coins = pygame.sprite.Group()
    
    robbers = pygame.sprite.Group()
    
    while True:
        func.check_events(gm_settings, screen, player, coins, robbers, stats)
        func.update_screen(gm_settings, screen, player, coins, robbers, clock, sb)
        player.update()
        func.update_coins(player, coins, stats, sb, gm_settings)
        coins.update()
        func.update_robbers(player, robbers, stats, sb, gm_settings)
        robbers.update()
    
run_game()