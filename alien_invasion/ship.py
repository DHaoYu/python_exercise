import pygame

class Ship():

    def __init__(self,ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每个新飞船发放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #在飞船的属性center中设置小数值 
        self.center = float(self.rect.centerx)       
        #持续移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """依据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:#防止飞船出界
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0: #防止飞船出界
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置放置飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx