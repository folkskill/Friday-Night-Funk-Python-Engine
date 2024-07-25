from pygame.sprite import Group
from pygame.image import load
from pygame.rect import Rect
from sprite import Sprite

class Icon(Sprite):
    '''
    小图标类,
    :继承了精灵类
    '''
    group:Group = Group()

    def __init__(self, imagepath: str, location: tuple, scale: float = 1):
        super().__init__(imagepath, location, scale)

        self.icon_surface = load(imagepath)
        self.group.add_internal(self)
        self.state_rect_dict:dict = {
            True: Rect(
                0, 0,
                150, 150
            ),
            False: Rect(
                150, 0,
                150, 150
            )
        }

    def update(self, heal_num, MAX_NUM):
        '''小图标更新函数'''
        bool_value:bool = (heal_num > MAX_NUM * 0.2)

        self.image = self.icon_surface.subsurface(self.state_rect_dict[bool_value])