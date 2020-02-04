import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """检测鼠标按下"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #判断子弹在屏幕中有几颗
        if len(bullets) < ai_settings.bullet_allowed:
            #创建一个子弹并将其加入bullets中
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """检测鼠标抬起"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_ESCAPE:
        sys.exit()

def check_play_botton(stats, play_button, mouse_x, mouse_y, aliens, bullets, ship):
    """每次单机play按钮时开始游戏"""
    #在每次游戏结束后单机play都会重新开始
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #隐藏光标
        pygame.mouse.set_visible(False)
        #重置所有游戏信息至最开始
        stats.reset_stats()
        stats.game_active = True
        #清空子弹和外星人
        aliens.empty()
        bullets.empty()
        ship.center_ship()

def check_events(ai_settings, screen, ship, bullets, aliens, stats, play_button):
    """监视键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_botton(stats, play_button, mouse_x, mouse_y, aliens, bullets, ship)

def create_fleet(ai_settings, screen, aliens):
    """创建外星人群"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    number_aliens_x = get_number_aline_x(ai_settings, alien_width)
    number_aliens_row = get_number_aline_row(ai_settings, alien_height)
    #创建外星人
    for row_number in range(number_aliens_row):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_aline_x(ai_settings, alien_width):
    """计算一行除去左右留白 中间可以放下的最多外星人"""
    avaliable_space_x = ai_settings.screen_width - alien_width
    number_aliens_x = int(avaliable_space_x / (2*alien_width))
    return number_aliens_x

def get_number_aline_row(ai_settings, alien_height):
    """计算能够容纳多少行外星人"""
    avaliable_space_y = ai_settings.screen_height - 3*alien_height
    number_aliens_y = int(avaliable_space_y / (2*alien_height))
    return number_aliens_y

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建外星人"""
    alien = Alien(ai_settings, screen)
    alien.x = alien.rect.width + 2*alien.rect.width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)

def check_fleet_edges(ai_settings, aliens):
    """检测外星人是否触碰到边缘"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def update_aliens(ai_settings, ship, aliens, stats, bullets, screen):
    """检查外星人位置 更新外星人群的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    #检测飞船是否被外星人撞击
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(stats, ship, aliens, bullets)
    check_aliens_bottom(stats, ship, aliens, bullets, screen)

def ship_hit(stats, ship, aliens, bullets):
    """飞船被撞击之后游戏信息处理"""
    stats.ships_left -= 1
    if stats.ships_left > 0:
        aliens.empty()
        bullets.empty()
        ship.center_ship()
        #暂停0.5秒
        sleep(0.5)
    else:
        #将flags信息调整为最初状态
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(stats, ship, aliens, bullets, screen):
    """检查是否有外星人到达屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(stats, ship, aliens, bullets)

def change_fleet_direction(ai_settings, aliens):
    """将整个外星人下移 并改变左右的方向"""
    for alien in aliens.sprites():
        alien.rect.y += alien.ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_hit(ai_settings, screen, aliens, bullets):
    """将命中的子弹以及外星人删除"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, aliens)

def check_button_active(stats, paly_button):
    """检查是否为最开始 开始按钮是否应该存在"""
    if not stats.game_active:
        paly_button.draw_button()


def update_screen(ai_settings, screen, ship, aliens, bullets, stats, paly_button):
    """用于每次循环时将屏幕上的图像进行更新"""
    screen.fill(ai_settings.bg_color)

    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #将越界的子弹进行删除
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    ship.blitme()
    aliens.draw(screen)

    #检查是否为最开始
    check_button_active(stats, paly_button)

    pygame.display.flip()#刷新屏幕
