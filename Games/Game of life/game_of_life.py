import pygame
import math

screen_width = 1000
screen_height = 1000

cellSize = 20

grids = [100, 100]

DEAD = (0, 0, 0)
ALIVE = (255, 255, 255)

keepAlive = []


class cell(object):
    def __init__(self, position, state, n):
        self.position = position
        self.state = state
        self.n = n

    def draw(self, surface):
        pygame.draw.rect(surface, self.state, [self.position[0] * cellSize, self.position[1] * cellSize, cellSize, cellSize], 0)

    def update(self):
        if self.state == ALIVE and self.n < 2:
            self.state = DEAD
        if self.state == ALIVE and self.n > 3:
            self.state = DEAD
        if self.n == 3:
            self.state = ALIVE
        return self.state

    def set_n(self, _n):
        self.n = _n

    def toggle_state(self):
        if self.state == ALIVE:
            self.state = DEAD
        else:
            self.state = ALIVE
        return self.state

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state


def mouse_input(mouse):
    if mouse[0]:
        return True
    else:
        return False


def main():
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('Arial', 30)

    screen = pygame.display.set_mode([screen_width, screen_height])
    pygame.display.set_caption("Conway's game of life")

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    clock = pygame.time.Clock()
    done = False
    simulate = False
    cells = []
    alive = []
    tempToggle = []
    mouseToggle = ALIVE
    generation = 0
    speed = 100
    lastSim = 0

    for i in range(grids[0]):
        for j in range(grids[1]):
            if [i, j] in keepAlive:
                cellObj = cell([i, j], ALIVE, 0)
                alive.append(cellObj.position)
            else:
                cellObj = cell([i, j], DEAD, 0)
            cells.append(cellObj)

    while not done:
        clock.tick(500)
        surface.fill((0, 0, 0))
        cooldown = 1000 / speed

        for i in range(grids[0]):
            for j in range(grids[1]):
                pygame.draw.rect(surface, (255, 255, 255), [i * cellSize, j * cellSize, cellSize, cellSize], 2)

        for c in cells:
            c.draw(surface)

        screen.blit(surface, (0, 0))
        pygame.display.update()  # Update

        if mouse_input(pygame.mouse.get_pressed()):
            pos = pygame.mouse.get_pos()
            scaled_pos = [math.floor(pos[0] / cellSize), math.floor(pos[1] / cellSize)]
            for c in cells:
                if c.position == scaled_pos:
                    if c.get_state() == ALIVE and mouseToggle is not ALIVE and scaled_pos not in tempToggle:
                        alive.remove(scaled_pos)
                        mouseToggle = DEAD
                        tempToggle.append(scaled_pos)
                        c.toggle_state()
                    elif c.get_state() == DEAD and mouseToggle is not DEAD and scaled_pos not in tempToggle:
                        alive.append(scaled_pos)
                        mouseToggle = ALIVE
                        tempToggle.append(scaled_pos)
                        c.toggle_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    simulate = not simulate
                elif event.key == pygame.K_DELETE:
                    for c in cells:
                        c.set_state(DEAD)
                        alive = []
                        generation = 0
                elif event.key == pygame.K_DOWN:
                    if speed > 10:
                        speed -= 10
                elif event.key == pygame.K_UP:
                    if speed < 1000:
                        speed += 10
            elif event.type == pygame.MOUSEBUTTONUP:
                mouseToggle = None
                tempToggle = []

        if simulate and cooldown < (pygame.time.get_ticks() - lastSim):
            print(generation)
            generation += 1
            for c in cells:  # check for neighbours
                pos = c.position
                n = 0
                for i in range(-1, 2, 1):
                    for j in range(-1, 2, 1):
                        if [pos[0] - i, pos[1] - j] in alive and [pos[0] - i, pos[1] - j] != pos:
                            n += 1
                c.set_n(n)

            for c in cells:
                state = c.update()
                if state == ALIVE and c.position not in alive:
                    alive.append(c.position)
                elif state == DEAD and c.position in alive:
                    alive.pop(alive.index(c.position))
            lastSim = pygame.time.get_ticks()


main()
