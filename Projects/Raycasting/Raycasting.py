import pygame
import math
import numpy as np

screen_width = 1600
screen_height = 1000

WHITE = (255, 255, 255)


class boundary:
    def __init__(self, x1, y1, x2, y2):
        self.start = np.array([x1, y1])
        self.stop = np.array([x2, y2])

    def draw(self, surface):
        pygame.draw.line(surface, WHITE, self.start, self.stop)


class ray:
    def __init__(self, x, y, heading):
        self.pos = np.array([x, y])
        self.heading = np.array([0, 1])

    def look_at(self, x, y):
        self.heading[0] = x - self.pos[0]
        self.heading[1] = y - self.pos[1]

    def cast(self, wall):
        x1 = wall.start[0]
        y1 = wall.start[1]
        x2 = wall.stop[0]
        y2 = wall.stop[1]
        x3 = self.pos[0]
        y3 = self.pos[1]
        x4 = self.pos[0] + self.heading[0]
        y4 = self.pos[1] + self.heading[1]
        d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if d == 0:
            return False
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / d
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / d
        if 0 < t < 1 and u > 0:
            px = x1 + t * (x2 - x1)
            py = y1 + t * (y2 - y1)
            return px, py
        else:
            return False

    def draw(self, surface):
        pygame.draw.line(surface, WHITE, self.pos, self.pos + self.heading * 10)


def main():
    pygame.init()
    screen = pygame.display.set_mode([screen_width, screen_height])
    pygame.display.set_caption('Ray Casting 2D')
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    clock = pygame.time.Clock()

    running = True
    wall = boundary(800, 800, 800, 400)
    r = ray(500, 500, 0)
    while running:
        clock.tick(100)
        surface.fill((0, 0, 0))
        wall.draw(surface)
        r.look_at(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        r.draw(surface)
        p = r.cast(wall)
        if p:
            pygame.draw.circle(surface, WHITE, p, 5)
        # update screen
        screen.blit(surface, (0, 0))
        pygame.display.update()  # Update

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False


main()
