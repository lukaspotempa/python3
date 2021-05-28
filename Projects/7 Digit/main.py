import pygame

screen_width = 300
screen_height = 500
margin = 20
gap = 5

# obj sizes
height = 20
width = 100

ON = (255, 0, 0)
OFF = (255, 255, 255)

segmentDef = {
    'a': [margin, margin, width, height],
    'b': [margin + width + gap, margin, height, width],
    'c': [margin + width, margin + height + gap, height, width],
    'd': [margin - width, margin + (height*2) + gap, width, height],
    'e': [margin - width - gap, margin + height + gap, height, width],
}


class segment(object):
    def __init__(self, position, index):
        self.position = position
        self.index = index
        self.on = OFF

    def draw(self, surface):
        pygame.draw.rect(surface, OFF, [self.position[0], self.position[1], height, width], 0)


def main():
    pygame.init()
    screen = pygame.display.set_mode([screen_width, screen_height])
    pygame.display.set_caption("Seven Segment Display")
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    segments = []

    for s in segmentDef:
        segObj = segment(segmentDef[s], s)
        segments.append(segObj)

    clock = pygame.time.Clock()

    done = False
    while not done:
        surface.fill((0, 0, 0))
        clock.tick(25)
        for s in segments:
            pygame.draw.rect(surface, OFF, [s.position[0], s.position[1], s.position[2], s.position[3]], 0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True

        screen.blit(surface, (0, 0))
        pygame.display.update()  # Update


main()