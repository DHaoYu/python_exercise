import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
 
    #bg_color = (230, 230, 230)
    #创建飞船对象
    ship = Ship(ai_settings, screen)
    #创建外星人对象编组（多个外星人）
    aliens = Group()
    #创建一个用于存储子弹的编组
    bullets = Group()
    gf.create_fleet(ai_settings, screen, aliens)
    #创建游戏信息对象
    stats = GameStats(ai_settings)

    #开始游戏主循环
    while True:
        if stats.game_active:
            gf.check_events(ai_settings, screen, ship, bullets)
            ship.update()
            bullets.update()
            gf.check_hit(ai_settings, screen, aliens, bullets)
            gf.update_aliens(ai_settings, ship, aliens, stats, bullets, screen)
            gf.update_screen(ai_settings, screen, ship, aliens, bullets)
#help(pygame)
run_game()