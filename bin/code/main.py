from tracemalloc import get_traced_memory,start,stop
from pygame.surface import Surface
from pygame.sprite import Group
from pygame.rect import Rect
from pygame.event import get
from pygame import init,quit
from pygame.locals import *
from pygame import display
from pygame import time
from functions import *
from icon import Icon
from json import load
from sys import exit
from entity import *
from ENUM import *

init()
start()
old_memory = 0
max_health = 0
self_health_value:float = 10.0 # 最大值由配置文件决定

def load_settings():
    '''加载游戏设置'''
    global max_health

    settings:dict
    with open('bin/data/settings.json', 'r', encoding = 'utf-8') as file:
        settings = load(file)
        file.close

    max_health = settings["max_health_value"]

def get_memory_usage():
    '''获取当前程序的内存使用情况'''
    global old_memory
    current, peak = get_traced_memory()
    #*转换为MB
    memory_usage = round(current / 1024, 2)
    if abs(memory_usage - old_memory) >= 5:
        old_memory = memory_usage
    else:return old_memory
    return memory_usage

class System:
    '''
    存储大量主要数据.\n
    包括接口函数,
    绘画函数等等.
    '''
    fps:float = 0.0
    memory:float = 0.0
    lables:list[Lable] = [Lable('bin/font/pixel.otf',"%NA",20,(255,255,255),(0,0),"FPS_counter"),
                          Lable('bin/font/vcr.ttf',"%NA",20,(255,255,255),(0,20),"memory_counter"),
                          Lable('bin/font/vcr.ttf',"%NA",20,(255,255,255),(0,40),"frame_interval")]
    camera_position = [0,0]
    active:bool = True
    windoe_mode = "normal" #代表了窗口的显示模式
    ticker = time.Clock() #计时器
    sys_window = display.set_mode((WIDTH,HEIGHT), 4) #窗口初始化
    window = Surface((WIDTH,HEIGHT), SRCALPHA)
    display.set_caption("Friday Night Funkie':PythonEngine")
    sprite_class_dict = { #类储存
        BACKGROUND : Background,
        BOYFRIEND : BoyFriend
    }
    list_with_enity = [] # 二维数组
    
    def __init__() -> None:
        '''初始化'''
        load_settings()

        bg_list = [__class__.sprite_class_dict[BACKGROUND]()] #背景列表
        cha_list = [] #角色列表
        cha_list.append(__class__.sprite_class_dict[BOYFRIEND]((400,100),1.0))
        icon_list = [Icon('bin/charater/bf/icon.png', (100, 300), 3)]
        __class__.list_with_enity = [bg_list, cha_list, icon_list]

    def draw(window:Surface) -> None:
        '''
        对所有的对象进行绘画
        :(包括了背景[纯色]的渲染)
        :需要传入surface对象
        '''
        # 背景
        __class__.window.fill((30,30,30))
        __class__.sys_window.fill((0,0,0,0))

        for list_enity in __class__.list_with_enity:
            for enity in list_enity:
                class_value = type(enity).__name__
                group:Group = enity.__class__.group # 尝试获取group值
                if group: # 有group属性才可以进行数据更新
                    #* 根据类的不同为其提供其所需的值
                    if class_value == "Icon":
                        group.update(self_health_value, max_health)
                    else:
                        group.update(frame_interval)
                    # 最后进行绘画,注意不能画在sys_window上
                    group.draw(window)

        c_x,c_y = __class__.camera_position
        __class__.sys_window.blit(__class__.window,
                                  Rect(0 - c_x,0 - c_y,
                                       __class__.sys_window.get_width(),
                                       __class__.sys_window.get_height()))
        
        # 调试信息的渲染
        for lable in __class__.lables:
            if lable.name == "FPS_counter":
                lable.change_text(f"FPS:{__class__.fps}",__class__.memory)

            elif lable.name == "memory_counter":
                lable.change_text(f"Memory:{__class__.memory}MB",__class__.memory)

            elif lable.name == "frame_interval":
                lable.change_text(f"Frame_interval:{frame_interval}")

            lable.draw(__class__.sys_window) # 不要画在window上

    def Key_detect() -> None:
        '''按键事件检测'''
        for event in get():
            if event.type == QUIT:
                stop()
                quit()
                exit()

            if event.type == K_F11:
                if __class__.windoe_mode == "normal":
                    display.set_mode((WIDTH,HEIGHT),FULLSCREEN)
                    __class__.windoe_mode = "fullscreen"
                else:
                    display.set_mode((WIDTH,HEIGHT))
                    __class__.windoe_mode = "normal"

    def update():
        '''数据更新函数'''
        global frame_interval
        temp = __class__

        temp.fps = round(temp.ticker.get_fps()) # round取舍
        try:frame_interval = round(1.0 / temp.fps, 6)
        except ZeroDivisionError:pass

        temp.memory = get_memory_usage()
                
    def main() -> None:
        '''
        程序主函数
        :接口函数
        '''
        temp = __class__
        temp.__init__()
        while True:
            temp.ticker.tick(60)
            temp.Key_detect()
            temp.draw(temp.window) # 优先级window < sys_window
            temp.update()
            display.flip()

if __name__ == "__main__":
    System.main()