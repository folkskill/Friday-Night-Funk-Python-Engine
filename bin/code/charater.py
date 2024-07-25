from pygame.surface import Surface
from pygame.sprite import Group
from pygame.rect import Rect
from sprite import Sprite
from functions import *
from ENUM import *

frame_interval:float = 0.0 # 储存帧运行的时间间隔

class Charater(Sprite):
    """角色类"""
    animation_surface:Surface = None
    group:Group = Group()
    surface_dict:dict = {}
    tick_dict:dict = {}
    add_dict:dict = {}

    @staticmethod
    def class_init(animation_surface:Surface, rect_dict:dict):
        '''对静态对象进行初始化'''
        for key in rect_dict.keys():
            surface_list:list[Surface] = []
            # 遍历str矩形值
            for rect_str in rect_dict[key]:
                # 生成图片动画表
                rect_str:str
                rect_list:list = rect_str.split(',')
                pygame_rect:Rect = Rect(int(rect_list[0]),int(rect_list[1]),int(rect_list[2]),int(rect_list[3]))
                # 裁切图像
                new_surface = animation_surface.subsurface(pygame_rect)
                surface_list.append(new_surface)

            # 一个动画的图像完成了初始化
            __class__.surface_dict[key] = surface_list

    def __init__(self, animation_surface:Surface, json_dict:dict, location:tuple, scale:float = 1.0) -> None:
        super(Charater, self).__init__('bin/data/sys/Error.png', location, scale)
        self.animation_surface = animation_surface
        # 动画图裁切
        self.class_init(animation_surface, json_dict['rect_dict'])
        # 私有及静态属性初始化
        __class__.tick_dict = json_dict["animation_speed_dict"]
        __class__.add_dict = json_dict["animation_add"]
        self.tick_num = 0
        self.state = HEY
        self.old_state = self.state
        self.index = 0
        self.position:tuple = self.rect.topleft
        # 加入组
        self.group.add_internal(self)

    def update(self,frame_interval):
        '''根据下标和属性进行动画图更改'''
        if frame_interval == 0.0:
            return
        
        frame_interval *= 100

        if self.tick_num - 1 >= 0:
            # 没到时间
            self.tick_num -= 1
        else:
            # 到时间了
            self.tick_num = floor(self.tick_dict[self.state] * frame_interval)
            # 检测是不是中途更改了动画状态
            if self.state != self.old_state:
                # 如果更改就直接回满index
                self.index = 0
            else:
                # *没有的话就接着下一个index
                self.index += 1
                if self.index + 1 >= len(self.surface_dict[self.state]):
                    # 播放完了，重播
                    self.index = 0
            # 图画更新
            self.image = self.surface_dict[self.state][self.index]
            # 位置更新
            x, y = self.position
            w, h = self.rect.size
            add_x, add_y = self.add_dict[self.state][self.index].split(',')
            self.rect = Rect(
                x + int(add_x),
                y + int(add_y),
                w, h
            )
            # 最后同步状态
            self.old_state = self.state