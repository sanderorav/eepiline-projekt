import pygame.font

class Scoreboard():
    def __init__(self, game_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 46)
        self.prepare_score()
        
    def prepare_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.game_settings.bg_colour)
        self.score_coin = pygame.image.load('coin.png').convert_alpha()
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.left = self.screen_rect.left + 70
        self.score_image_rect.top = 20
        self.score_coin_rect = self.score_coin.get_rect()
        self.score_coin_rect.left = self.screen_rect.left + 10
        self.score_coin_rect.top = 10
        
    def draw_score(self):
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.score_coin, self.score_coin_rect)