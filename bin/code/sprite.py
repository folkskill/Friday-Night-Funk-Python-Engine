'''
改写的精灵类
'''
import pygame
class Sprite(pygame.sprite.Sprite):
    def __init__(self, imagepath:str, location:tuple, scale:float = 1.0):
        '''
        精灵类：
        imagepath:图片文件路径
        location:坐标
        '''
        super().__init__()
        self.scale = scale
        self.image:pygame.surface.Surface = pygame.image.load(imagepath).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location