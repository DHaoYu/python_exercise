
class Settings():
    """存储所有设置的类"""
    def __init__(self):#类内成员函数
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #飞船的设置
        self.ship_speed_factor = 0.8
        self.ship_limit = 3

        #子弹的设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3 #允许子弹在屏幕中的最大数

        #外星人设置
        self.alien_speed_factor = 0.3
        self.fleet_drop_speed = 10
        # 1表示右移 -1表示左移
        self.fleet_direction = 1
