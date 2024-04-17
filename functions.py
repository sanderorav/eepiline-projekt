import sys
import pygame
from player import Player
from coin import Coin
from robber import Robber

pygame.init()
ADDCOIN = pygame.USEREVENT + 1
pygame.time.set_timer(ADDCOIN, 500)
ADDROBBER = pygame.USEREVENT + 2
pygame.time.set_timer(ADDROBBER, 1500)

def check_events(game_settings, screen, player, coins, robbers, stats):
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
        elif event.type == ADDROBBER:
            add_robber(game_settings, screen, robbers, stats)

def update_screen(game_settings, screen, player, coins, robbers, clock, sb):
    screen.fill(game_settings.bg_colour)
    player.blit_me()
    if len(coins) > 0:
        for coin in coins:
            coin.blit_me()
    if len(robbers) > 0:
        for robber in robbers:
            robber.blit_me()
    sb.draw_score()
    clock.tick(120)
    pygame.display.flip()
    
def add_coin(game_settings, screen, coins, stats):
    new_coin = Coin(screen, game_settings, stats)
    coins.add(new_coin)
    
def add_robber(game_settings, screen, robbers, stats):
    new_robber = Robber(screen, game_settings, stats)
    robbers.add(new_robber)

def update_coins(player, coins, stats, sb, game_settings):
    hitted_coin = pygame.sprite.spritecollideany(player, coins)
    sb.prepare_score()
    if hitted_coin != None:
        stats.score += 1
        hitted_coin.kill()

def update_robbers(player, robbers, stats, sb, game_settings):
    hitted_robber = pygame.sprite.spritecollideany(player, robbers)
    if hitted_robber != None and not player.is_penalised:
        stats.score -= 5
        player.is_penalised = True
    elif hitted_robber == None:
        player.is_penalised = False
    sb.prepare_score()