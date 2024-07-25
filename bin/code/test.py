import pygame
import time

pygame.init()

# 设置窗口尺寸
window_size = (400, 300)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Pygame Timer Example')

# 设置字体和字体大小
font = pygame.font.Font(None, 36)

# 计时器起始时间
start_time = time.time()

# 游戏循环
running = True
while running:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 清屏
    screen.fill((255, 255, 255))

    # 计算当前经过的时间
    current_time = time.time()
    elapsed_time = current_time - start_time

    # 将时间转换为字符串格式
    timer_text = "Time: {:.2f}".format(elapsed_time)

    # 渲染文本
    text_surface = font.render(timer_text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(window_size[0] // 2, window_size[1] // 2))

    # 将文本绘制到屏幕上
    screen.blit(text_surface, text_rect)

    # 刷新屏幕
    pygame.display.flip()

# 退出Pygame
pygame.quit()
