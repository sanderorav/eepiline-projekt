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

def check_events(game_settings, screen, player, coins, robbers, stats, play_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.moving_right = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.moving_left = True
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.moving_up = True
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.moving_right = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.moving_left = False
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.moving_up = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.moving_down = False
        elif event.type == ADDCOIN:
            add_coin(game_settings, screen, coins, stats)
        elif event.type == ADDROBBER:
            add_robber(game_settings, screen, robbers, stats)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y)
            
def check_play_button(stats, play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True

def update_screen(game_settings, screen, player, coins, robbers, clock, sb, play_button, stats):
    screen.fill(game_settings.bg_colour)
    player.blit_me()
    if len(coins) > 0:
        for coin in coins:
            coin.blit_me()
    if len(robbers) > 0:
        for robber in robbers:
            robber.blit_me()
    if not stats.game_active:
        play_button.draw_button()
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
        if stats.score > 5:
            stats.score -= 5
            player.is_penalised = True
        else:
            stats.score = 0
            player.is_penalised = True
    elif hitted_robber == None:
        player.is_penalised = False
    sb.prepare_score()