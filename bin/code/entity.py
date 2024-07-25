'''
v0.2\n
储存了游戏中所有可能会用到的精灵
'''
from charater import Charater,frame_interval,Group # frame_interval不可删除
from pygame.image import load as image_load
from sprite import Sprite
from lable import Lable
from json import load

class Background(Sprite):
    group = Group()
    main_thread:str = "None"
    def __init__(self):
        super().__init__('bin/weeks/week1/images/stagefront.png',(-800,200))
        self.group.add_internal(self)

class BoyFriend(Charater):
    '''
    boyfriend!
    :I love you--aaaa!!!
    '''

    def __init__(self, location:tuple, scale:float = 1.0) -> None:
        animation_surface = image_load('bin/charater/bf/animation.png')
        json_dict = {}
        with open('bin/charater/bf/animation.json', 'r', encoding = 'utf-8') as file:
            json_dict = load(file)
            file.close()

        super(BoyFriend, self).__init__(animation_surface, json_dict, location, scale)
