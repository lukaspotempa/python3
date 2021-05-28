import pygame
import random

# define screen size
screen_width = 1280
screen_height = 960

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# define game relevant sizes
playerSize = (20, 200)
playerMargin = 20
startSpeed = 5
ballRadius = 15
borderMargin = 10


class player(object):
    def __init__(self):
        self.position = (playerMargin, int((screen_height / 2) - (playerSize[1] / 2)))

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, (self.position[0], self.position[1], playerSize[0], playerSize[1]))

    def move(self, pos_y):
        if (pos_y + (playerSize[1] / 3)) < screen_height and (pos_y - (playerSize[1] / 3)) > 0:
            self.position = (playerMargin, pos_y - (playerSize[1] / 2))
        else:
            return

    def get_position(self):
        return self.position


class ball(object):
    def __init__(self):
        self.position = (screen_width / 2, screen_height / 2)
        self.pitch = 0
        self.heading = 1
        self.score = 0
        self.speed = startSpeed

    def move(self, playerObj):
        if (self.position[0] > playerMargin) and (self.position[1] < borderMargin):  # Bounce top
            self.bounceBorder()

        if (self.position[0] > playerMargin) and (self.position[1] > (screen_height - borderMargin)):  # Bounce bottom
            self.bounceBorder()

        if self.position[0] > (screen_width - ballRadius):  # Bounces right side
            self.bouncePlayer(False)

        if self.position[0] < (playerMargin + playerSize[0] + ballRadius + 3) and (abs((playerObj.get_position()[1] + playerSize[1] / 2) - self.position[1])) < (playerSize[1] / 2):  # Bounces Player
            self.bouncePlayer(True)

        elif self.position[0] < (playerMargin + playerSize[0] + ballRadius) and (abs((playerObj.get_position()[1] + playerSize[1] / 2) - self.position[1])) > (playerSize[1] / 2):
            self.reset()

        oldPos = self.position
        self.position = (oldPos[0] + (self.speed * self.heading), oldPos[1] + (self.speed * self.pitch))

    def draw(self, surface):
        pygame.draw.circle(surface, RED, (self.position[0], self.position[1]), ballRadius)

    def bounceBorder(self):
        self.pitch *= -1
        #soundObj = pygame.mixer.Sound('Games/Pong/sounds/pong_blip_' + str(random.randint(1, 3)) + '.wav')
        #soundObj.play(0)

    def bouncePlayer(self, is_Player):
        self.heading *= -1
        #soundObj = pygame.mixer.Sound('Games/Pong/sounds/pong_blip_' + str(random.randint(1, 3)) + '.wav')
        #soundObj.play(0)
        if is_Player:
            self.pitch = random.uniform(0.5, -0.5)
            self.score += 1
            self.speed += 0.5

    def reset(self):
        self.score = 0
        self.position = (screen_width / 2, screen_height / 2)
        self.pitch = 0
        self.heading = 1
        self.speed = startSpeed

    def drawScore(self, surface):
        font = pygame.font.SysFont('Arial', 30)
        text = font.render('Score: ' + str(self.score), False, YELLOW)
        textDiv = text.get_rect()
        textDiv.center = (120, 20)
        surface.blit(text, textDiv)


def main():
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode([screen_width, screen_height])
    pygame.display.set_caption("Pong")

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    clock = pygame.time.Clock()

    playerObj = player()
    ballObj = ball()

    running = True

    while running:
        # limits the while loop
        clock.tick(100)

        # surface adjustments
        surface.fill((0, 0, 50))

        # draw player
        mousePos = pygame.mouse.get_pos()
        playerObj.move(mousePos[1])
        playerObj.draw(surface)

        # draw score
        ballObj.drawScore(surface)

        # draw ball
        ballObj.move(playerObj)
        ballObj.draw(surface)

        # update screen
        screen.blit(surface, (0, 0))
        pygame.display.update()  # Update

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                pygame.quit()
                running = False


main()
