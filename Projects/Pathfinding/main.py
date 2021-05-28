import pygame
import random
import math

screen_width = 800
screen_height = 900
top_margin = screen_height - screen_width
side_margin = 10
WHITE = (255, 255, 255)
RED = (255, 0, 0)
rsize = 10


def createRandomPoints():
    arr = []
    for i in range(1, 6, 1):
        arr.append(
            [random.randint(0, screen_width - side_margin), random.randint(top_margin, screen_height - side_margin)])
    return arr


def draw_circle(surface, p):
    for i in range(len(p)):
        color = WHITE
        if i == 0 or i == (len(p) - 1):
            color = RED
        pygame.draw.circle(surface, color, p[i], rsize)


def draw_line(surface, p1, p2):
    pygame.draw.line(surface, WHITE, p1, p2, 1)


def calculate_distance(p, px):
    x1 = p[0] - px[0]
    x2 = p[1] - px[1]
    res = (math.pow(x1, 2) + math.pow(x2, 2))
    distance = math.sqrt(res)
    return distance


def main():
    pygame.init()
    screen = pygame.display.set_mode([screen_width, screen_height])
    pygame.display.set_caption("Pathfinding")
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    points = createRandomPoints()

    clock = pygame.time.Clock()
    running = True
    simulate = True
    order = []
    inc = 0
    while running:
        clock.tick(1)
        surface.fill((0, 0, 50))

        if simulate:
            for p in range(0, len(points) - 1):
                for px in range(0, len(points) - 1):
                    if px == p:
                        pass
                    else:
                        distance = calculate_distance(points[p], points[px])
                        if p < len(order):
                            if order[p][1] > distance:
                                order[p] = [points[px], distance]
                        else:
                            order.insert(p, [points[px], distance])

        for o in order:
            draw_line(surface, points[order.index(o)], o[0])
        draw_circle(surface, points)

        screen.blit(surface, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass


main()
