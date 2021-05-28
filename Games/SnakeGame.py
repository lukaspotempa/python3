import random
import pygame


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the height and width of the screen
size = [520, 520]

# Map stuff
fieldSize = [100, 100]
rectSize = [20, 20]

MOVE_UP = (0, -1)
MOVE_DOWN = (0, 1)
MOVE_LEFT = (-1, 0)
MOVE_RIGHT = (1, 0)


class food(object):
    def __init__(self):
        self.position = self.random_pos()

    def draw(self, surface):
        pygame.draw.rect(surface, RED, [self.position[0], self.position[1], rectSize[0], rectSize[1]], 0)

    def random_pos(self):
        return random.randrange(0, size[0], rectSize[0]), random.randrange(0, size[1], rectSize[1])

    def set_pos(self, pos):
        self.position = pos


class snake(object):

    def __init__(self):
        self.length = 1
        self.positions = [(size[0] / 2, size[1] / 2)]
        self.direction = MOVE_DOWN
        self.color = WHITE

    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, WHITE, [p[0], p[1], rectSize[0], rectSize[1]], 0)

    def get_head_position(self):
        return self.positions[0]

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (cur[0] + (x * rectSize[0]), cur[1] + (y * rectSize[1]))
        if len(self.positions) > 2 and new in self.positions[2:]:
            pass
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [(size[0] / 2, size[1] / 2)]
        self.direction = MOVE_DOWN

    def handle_input(self):
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.turn(MOVE_UP)
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.turn(MOVE_DOWN)
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.turn(MOVE_LEFT)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.turn(MOVE_RIGHT)

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point


def drawGrid(surface):
    for i in range(fieldSize[0]):
        for j in range(fieldSize[1]):
            pygame.draw.rect(surface, WHITE, [rectSize[0] * j, rectSize[1] * i, rectSize[0], rectSize[1]], 1)


def main():
    # Init game window
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Snake")

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    snakeObj = snake()
    foodObj = food()

    clock = pygame.time.Clock()

    while True:

        # limits the while loop
        clock.tick(5)

        # Handle input
        snakeObj.handle_input()

        surface.fill((0, 0, 0))

        foodObj.draw(surface)

        snakeObj.move()
        snakeObj.draw(surface)

        if snakeObj.get_head_position() == foodObj.position:
            snakeObj.length += 1
            foodObj.set_pos(foodObj.random_pos())

        drawGrid(surface)
        screen.blit(surface, (0, 0))
        pygame.display.update()  # Update


main()