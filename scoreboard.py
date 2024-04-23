import pygame.font

class Scoreboard():
    def __init__(self, game_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 46)
        self.prepare_score()
        self.prepare_level()
        self.prepare_record()
        
    def prepare_score(self):
        score_str = str(self.stats.score)
        temp_surface = self.font.render(score_str, True, self.text_color)
        self.score_image = pygame.Surface(temp_surface.get_size(), pygame.SRCALPHA)
        self.score_image.fill((255, 255, 255, 0))
        self.score_image.blit(temp_surface, (0, 0))
        self.score_coin = pygame.image.load('coin_parem_kui_varem.png').convert_alpha()
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.left = self.screen_rect.left + 70
        self.score_image_rect.top = 20
        self.score_coin_rect = self.score_coin.get_rect()
        self.score_coin_rect.left = self.screen_rect.left + 10
        self.score_coin_rect.top = 10
        
    def prepare_level(self):
        level_str = str(self.stats.level)
        temp_surface = self.font.render('LEVEL: ' + level_str, True, self.text_color)
        self.level_image = pygame.Surface(temp_surface.get_size(), pygame.SRCALPHA)
        self.level_image.fill((255, 255, 255, 0))
        self.level_image.blit(temp_surface, (0, 0)) 
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.screen_rect.left + 10
        self.level_rect.top = 60
    
    def prepare_record(self):
        record_str = str(self.stats.record)
        temp_surface = self.font.render('HI-SCORE: ' + record_str, True, self.text_color)
        self.record_image = pygame.Surface(temp_surface.get_size(), pygame.SRCALPHA)
        self.record_image.fill((255, 255, 255, 0))
        self.record_image.blit(temp_surface, (0, 0))
        self.record_rect = self.record_image.get_rect()
        self.record_rect.right = self.screen_rect.right - 10
        self.record_rect.top = 20
        
    def draw_score(self):
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.score_coin, self.score_coin_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.record_image, self.record_rect)