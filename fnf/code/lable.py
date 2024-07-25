from pygame.surface import Surface
from pygame.color import Color
from pygame.font import Font
from pygame.rect import Rect

class Lable():
    '''
    游戏用文字类\n
    具有绘画，字体选择，自动生成图像功能
    '''
    def __init__(self,
                 style_path:str,
                 text:str,size:int,
                 lable_color:Color,
                 position:tuple,
                 name:str = "default"):
        self.font:Font = Font(style_path,size)
        self.lable_surface:Surface = self.font.render(text,True,lable_color)
        self.position:tuple = position
        self.color = lable_color
        self.name:str = name
        self.text:str = text
        self.special_num:int = 0

    def change_text(self,text,special_num:int | str = "default"):
        if self.text != text:
            #新的展示内容
            if special_num != self.special_num and type(special_num) != str:
                if abs(special_num - self.special_num) >= 2:
                    self.text = text
                    self.lable_surface:Surface = self.font.render(text,True,self.color)
            elif special_num == "default":
                self.text = text
                self.lable_surface:Surface = self.font.render(text,True,self.color)

    def draw(self,window:Surface):
        x,y = self.position
        window.blit(self.lable_surface,
                    Rect(x,y,
                         self.lable_surface.get_width(),
                         self.lable_surface.get_height()))