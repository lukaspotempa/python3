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

# game relevant sizes
player_margin = 30
player_size = (20, 50)
ship_speed = 4
dir_left = -1
dir_right = 1
projectile_speed = 3
shooting_cd = 100

comets = {
    # 'key': [sizeX, sizeY, speedX, speedY, hp]
    'small': [30, 30, 0.5, 0.2, 1],
    'medium': [40, 40, 0.5, 0.2, 2],
    'large': [60, 60, 0.5, 0.2, 3]
}

player_img = pygame.image.load('./img/player.png')
player_img = pygame.transform.scale(player_img, (player_size[0], player_size[1]))


class projectile:
    def __init__(self, playerPos):
        self.position = (playerPos[0] + (player_size[0] / 2), playerPos[1] - 8)

    def update(self):
        oldPos = self.position
        self.position = (oldPos[0], oldPos[1] - (1 * projectile_speed))

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, (self.position[0], self.position[1], 2, 10), 0)


class ship:
    def __init__(self):
        self.position = ((screen_width / 2) - (player_size[0] / 2), screen_height - player_margin - player_size[1])
        self.projectiles = []

    def move(self, direction):
        if direction == dir_left and (self.position[0] - player_size[0] < -15):
            return
        if direction == dir_right and (self.position[0] + player_size[0]) > screen_width:
            return
        pos = self.position
        self.position = (pos[0] + (direction * ship_speed), pos[1])

    def draw(self, surface):
        surface.blit(player_img, (self.position[0], self.position[1])) # Draw space ship

        for p in self.projectiles:
            pygame.draw.rect(surface, WHITE, (p[0], p[1], 2, 10), 0)

    def handle_input(self, keys):
        if keys[pygame.K_a]:
            self.move(dir_left)
        if keys[pygame.K_d]:
            self.move(dir_right)

    def update(self):
        for p in range(len(self.projectiles)):
            cur = self.projectiles[p]
            self.projectiles[p] = (self.projectiles[p][0], self.projectiles[p][1] - (1 * projectile_speed))


class comet:
    def __init__(self):
        self.type = random.choice(list(comets.values()))
        self.size = (self.type[0], self.type[1])
        self.position = (random.randint(self.size[0], screen_width - self.size[0]), - self.size[1])
        # self.pitch = random.uniform(-0.5, 0.5)
        self.pitch = 0
        self.speed = (self.type[2], self.type[3])
        self.hp = self.type[4]

    def update(self):
        if self.position[0] < (self.size[0]) or self.position[0] > (screen_width - self.size[0]):  # Bounce left
            self.bounceBorder()

        if self.position[1] > (screen_height - player_margin):  # Game over
            pass
        oldPos = self.position
        self.position = (oldPos[0] + (self.pitch * self.speed[0]), oldPos[1] + (self.speed[1] * 1))

    def bounceBorder(self):
        self.pitch *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, WHITE, (self.position[0], self.position[1]), self.size[0])

    def hit(self):
        if self.hp > 0:
            self.hp -= 1
            return False
        else:
            return True


def main():
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode([screen_width, screen_height])
    pygame.display.set_caption("Space Fighter")

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    clock = pygame.time.Clock()

    shipObj = ship()

    running = True

    projectiles = []
    cometsList = []

    cometObj = comet()
    cometsList.append(cometObj)

    lastShot = 0
    lastSpawn = 0
    comet_cd = random.randint(0, 1500)

    while running:

        # limits the while loop
        clock.tick(100)

        # surface adjustments
        surface.fill((10, 10, 10))

        # create random comets
        if (pygame.time.get_ticks() - lastSpawn) > comet_cd:
            cometObj = comet()
            cometsList.append(cometObj)
            lastSpawn = pygame.time.get_ticks()
            comet_cd = random.randint(5000, 15000)

        # draw player space ship
        shipObj.draw(surface)
        shipObj.handle_input(pygame.key.get_pressed())
        shipObj.update()

        # draw and update comets
        for c in cometsList:
            c.update()
            c.draw(surface)
            pos = c.position
            if pos[1] < -50:  # Remove from list if out of view
                cometsList.pop(cometsList.index(c))

        # draw and update projectiles
        for p in projectiles:
            # hit detection
            for c in cometsList:
                distanceX = abs(p.position[0] - c.position[0])
                distanceY = p.position[1] - (c.position[1] + c.size[1] / 2)
                if distanceX < 5 and distanceY < 0:
                    projectiles.pop(projectiles.index(p))
                    dead = c.hit()
                    if dead:
                        cometsList.pop(cometsList.index(c))
            p.update()
            p.draw(surface)
            pos = p.position
            if pos[1] < -50:  # Remove from list if out of view
                projectiles.pop(projectiles.index(p))

        # update screen
        screen.blit(surface, (0, 0))
        pygame.display.update()  # Update

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                pygame.quit()
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if shooting_cd < (pygame.time.get_ticks() - lastShot):
                        projectileObj = projectile(shipObj.position)
                        projectiles.append(projectileObj)
                        lastShot = pygame.time.get_ticks()


main()
