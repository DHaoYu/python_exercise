import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """飞船发射子弹的类"""
    def __init__(self, ai_settings, screen, ship):
        """在飞船的头部位置创建子弹对象"""
        super().__init__()
        self.screen = screen

        #先在0,0处创建子弹对象,在进行正确设置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #存储用小数（非像素点）表示的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """更新向上移动的子弹"""
        self.y -= self.speed_factor
        #将子弹位置更新到图像相应位置
        self.rect.y = self.y

    def draw_bullet(self):
        """绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)