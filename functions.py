import sys
import pygame
from player import Player
from coin import Coin
from robber import Robber
from terrorist import Terrorist

pygame.init()
pygame.mixer.init(44100, -16, 2, 2048)
pygame.mixer.music.load('music.wav')
ADDCOIN = pygame.USEREVENT + 1
pygame.time.set_timer(ADDCOIN, 500)
ADDROBBER = pygame.USEREVENT + 2
pygame.time.set_timer(ADDROBBER, 1500)
ADDTERRORIST = pygame.USEREVENT + 3
pygame.time.set_timer(ADDTERRORIST, 2500)

def check_events(game_settings, screen, player, coins, robbers, terrorists, stats, play_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            update_record_and_quit(stats)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.moving_right = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.moving_left = True
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player.moving_up = True
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player.moving_down = True
            if event.key == pygame.K_m:
                stats.music_on = not stats.music_on
                check_music(stats)
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
        elif event.type == ADDTERRORIST:
            add_terrorist(game_settings, screen, terrorists, stats)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y)
            
def check_play_button(stats, play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True

def update_screen(game_settings, screen, player, coins, robbers, terrorists, clock, sb, play_button, stats):
    screen.fill(game_settings.bg_colour)
    player.blit_me()
    if len(coins) > 0:
        for coin in coins:
            coin.blit_me()
    if len(robbers) > 0:
        for robber in robbers:
            robber.blit_me()
    if len(terrorists) > 0:
        for terrorist in terrorists:
            terrorist.blit_me()
    if not stats.game_active:
        play_button.draw_button()
    if stats.game_active == True:
        sb.draw_score()
    clock.tick(120)
    pygame.display.flip()
    
def add_coin(game_settings, screen, coins, stats):
    new_coin = Coin(screen, game_settings, stats)
    coins.add(new_coin)
    
def add_robber(game_settings, screen, robbers, stats):
    new_robber = Robber(screen, game_settings, stats)
    robbers.add(new_robber)

def add_terrorist(game_settings, screen, terrorists, stats):
    new_terrorist = Terrorist(screen, game_settings, stats)
    terrorists.add(new_terrorist)

def update_coins(player, coins, stats, sb, game_settings):
    hitted_coin = pygame.sprite.spritecollideany(player, coins)
    sb.prepare_score()
    if hitted_coin != None:
        stats.score += 1
        if (int(stats.score / game_settings.bonus_score)) > stats.bonus:
            stats.level += 1
            sb.prepare_level()
            stats.bonus += 1
            stats.min_speed += 1
            stats.max_speed += 1
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
    
def update_terrorists(player, terrorists, stats, sb, game_settings):
    hitted_terrorist = pygame.sprite.spritecollideany(player, terrorists)
    if hitted_terrorist != None:
        update_record(stats)
        stats.score = 0
        stats.level = 1
        stats.bonus = 0
        stats.min_speed = 1
        stats.max_speed = 5
        stats.game_active = False
        hitted_terrorist.kill()
    sb.prepare_score()
    sb.prepare_level()
    
def check_music(stats):
    if stats.music_on == True:
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.stop()

def update_record(stats):
    stats.record_saver(stats.score)

def update_record_and_quit(stats):
    stats.record_saver(stats.score)
    sys.exit()