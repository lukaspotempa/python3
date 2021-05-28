import pygame
import random
import math

# Screen sizes
screen_width = 810
screen_height = 810

# Misc
caption = 'Sudoku'

# Grid def
grid_size = 90
slim = 1
norm = 2
thick = 3
fill = 0

# Color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_WHITE = (140, 140, 140)
GREY = (60, 60, 60)
LIGHT_GREY = (150, 150, 150)
RED = (255, 0, 0)

# Settings koef
settings = {
    'easy': 4,
    'medium': 3,
    'hard': 2
}


def draw_grid(surface, selected):  # Draws all grids
    if selected is not None:
        pos = index_to_pos(selected)
        pygame.draw.rect(surface, LIGHT_GREY, [pos[0], pos[1], grid_size - slim, grid_size - slim], fill)
    for i in range(9):
        group_pos = [i % 3 * (3 * grid_size), math.floor(i / 3) * (grid_size * 3)]
        for n in range(9):
            n_pos = [group_pos[0] + (n % 3 * grid_size), group_pos[1] + math.floor(n / 3) * grid_size]
            pygame.draw.rect(surface, GREY, [n_pos[0], n_pos[1], grid_size, grid_size], slim)
        pygame.draw.rect(surface, BLACK, [group_pos[0], group_pos[1], grid_size * 3, grid_size * 3], thick)


def draw_num(surface, num_array):
    for group in range(len(num_array)):
        group_pos = [group % 3 * (3 * grid_size), math.floor(group / 3) * (grid_size * 3)]
        for n in range(len(num_array[group])):
            n_pos = [group_pos[0] + (n % 3 * grid_size), group_pos[1] + math.floor(n / 3) * grid_size]

            font = pygame.font.SysFont('sans-serif', 60)
            text = font.render(str(num_array[group][n]), False, BLACK)
            textDiv = text.get_rect()
            textDiv.center = (n_pos[0] + grid_size / 2, n_pos[1] + grid_size / 2)
            surface.blit(text, textDiv)


def get_index(pos):  # returns index from relative mouse pos
    # Calculate indices
    y = math.floor(pos[1] / (grid_size * 3))
    x = math.floor(pos[0] / (grid_size * 3))
    index_group = int(y * (screen_width / (grid_size * 3)) + x)

    y = math.floor((pos[1] / grid_size) % 3)
    x = math.floor((pos[0] / grid_size) % 3)
    index_cell = int(y * (screen_width / (grid_size * 3)) + x)

    x = math.floor(pos[0] / grid_size)
    y = math.floor(pos[1] / grid_size)
    index_global = int(y * screen_width + x)

    # Format: [group, cell, global]
    return index_group, index_cell, index_global


def index_to_pos(index):  # returns the gridded position for given (global) index
    y = index / screen_width * grid_size
    x = index % screen_width * grid_size
    return x, y


def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(caption)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    clock = pygame.time.Clock()

    selected = None
    nums = []

    for i in range(9):
        sub_arr = []
        for j in range(9):
            sub_arr.append(j)
        nums.append(sub_arr)

    running = True

    while running:
        clock.tick(500)
        surface.fill(WHITE)
        pygame.display.update()
        draw_grid(surface, selected)
        draw_num(surface, nums)
        screen.blit(surface, (0, 0))

        events = pygame.event.get()
        for e in events:
            if e.type == pygame.MOUSEBUTTONUP:
                index_array = get_index(pygame.mouse.get_pos())
                selected = index_array[2]

            if e.type == pygame.QUIT:
                pygame.quit()
                running = False


main()
