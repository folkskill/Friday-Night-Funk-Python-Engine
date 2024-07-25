import pygame,os,json
# 设置空白图片的大小和背景颜色
WIDTH, HEIGHT = 600,142
# 定义颜色
GREEN = (0, 255, 0)
TRANSPARENT = (0, 0, 0, 0)
class Animation:
    def __init__(self) -> None:
        pygame.init() 
        # 加载空白图片
        aid_image = pygame.Surface((WIDTH,HEIGHT), pygame.SRCALPHA)
        # 设置文件夹路径和文件名前缀
        name = "豌豆射手"
        folder_path = os.path.abspath(f'animation/data/{name}')
        # 获取文件夹中的所有PNG图片路径
        png_files = [f for f in os.listdict(folder_path) if f.endswith('.png')]

        # 遍历图片并将它们绘制到空白图片上
        data = []  # 用于存储图片的rect属性
        x, y = 0, 0  # 起始位置
        for idx, png_file in enumerate(png_files):
            image_path = os.path.join(folder_path, png_file)
            image = pygame.image.load(image_path)
            rect = image.get_rect()
            rect.topleft = (x, y)
            aid_image.blit(image, rect)
            data.append(rect)
            
            # 更新下一个图片的位置
            x += rect.width
            if x >= WIDTH:  # 如果当前行放不下了，换到下一行
                x = 0
                y += rect.height

        pygame.image.save(aid_image, f'bin/data/{name}/animation.png')

        # 要写入的数据
        data_list = []
        for rect in data:
            data_list.append(f"{rect.x},{rect.y},{rect.width},{rect.height}")
        dict = {'rect_list':data_list}
        # 将数据写入 JSON 文件
        with open(f'bin/data/{name}/animation.json', 'w') as f:
            json.dump(dict, f)
        pygame.quit()
Animation()