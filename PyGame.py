import pygame
pygame.init()

largura = 640
altura = 480

display = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake')

gameloop = True


def draw():
    display.fill([14, 5, 54])


if __name__ == '__main__':
    while gameloop:
        draw()
        pygame.display.update()