import sys
import pygame
from player import Player
from coin import Coin

pygame.init()
ADDCOIN = pygame.USEREVENT + 1
pygame.time.set_timer(ADDCOIN, 500)

def check_events(game_settings, screen, player, coins, stats):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.moving_right = True
            if event.key == pygame.K_LEFT:
                player.moving_left = True
            if event.key == pygame.K_UP:
                player.moving_up = True
            if event.key == pygame.K_DOWN:
                player.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            if event.key == pygame.K_LEFT:
                player.moving_left = False
            if event.key == pygame.K_UP:
                player.moving_up = False
            if event.key == pygame.K_DOWN:
                player.moving_down = False
        elif event.type == ADDCOIN:
            add_coin(game_settings, screen, coins, stats)

def update_screen(game_settings, screen, player, coins, clock):
    screen.fill(game_settings.bg_colour)
    player.blit_me()
    if len(coins) > 0:
        for coin in coins:
            coin.blit_me()
    clock.tick(120)
    pygame.display.flip()
    
def add_coin(game_settings, screen, coins, stats):
    new_coin = Coin(screen, game_settings, stats)
    coins.add(new_coin)

def update_coins(player, coins, stats, game_settings):
    hitted_coin = pygame.sprite.spritecollideany(player, coins)
    if hitted_coin != None:
        hitted_coin.kill()