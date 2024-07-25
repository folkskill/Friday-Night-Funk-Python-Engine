import pygame
import numpy as np

def apply_blur_filter(surface, kernel_size=3):
    pixel_array = pygame.PixelArray(surface)
    width, height = surface.get_size()
    kernel = np.ones((kernel_size, kernel_size)) / (kernel_size ** 2)

    # 循环遍历每个像素点
    for x in range(width):
        for y in range(height):
            # 初始化卷积结果的 RGB 值
            r, g, b, a = 0, 0, 0, 0
            # 循环遍历核矩阵
            for i in range(kernel_size):
                for j in range(kernel_size):
                    # 计算卷积结果的 RGB 值
                    nx = min(max(x + i - kernel_size // 2, 0), width - 1)
                    ny = min(max(y + j - kernel_size // 2, 0), height - 1)
                    color = surface.get_at((nx, ny))
                    r += color.r * kernel[i][j]
                    g += color.g * kernel[i][j]
                    b += color.b * kernel[i][j]
                    a += color.a * kernel[i][j]
            # 更新像素点的 RGB 值
            pixel_array[x, y] = (int(r), int(g), int(b), int(a))
    del pixel_array  # 删除像素数组以更新表面

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    clock = pygame.time.Clock()

    # 加载图像
    image = pygame.image.load('bin/Picture/Move/植物/Light/1.png').convert_alpha()

    # 应用模糊滤镜
    apply_blur_filter(image, kernel_size=20)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        screen.blit(image, (0, 0))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
