import pygame

pygame.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

rows = 3
columns = 3


# Set the height and width of the screen
size = [600, 600]
rect = [200, 200]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tic Tac Toe")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
pos = None
offsetCircle = 100
offsetCross = 50
radius = 50
width = 2
turnCounter = 0
field = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
]
turn = 'X'

def checkequal(a, b, c):
    return a == b and b == c and a == c and a != ''

def checkWinner():
    winner = None
    for i in range(len(field)):
        if checkequal(field[i][0], field[i][1], field[i][2]):
            winner = field[i][0]
    for i in range(len(field)):
        if checkequal(field[0][i], field[1][i], field[2][i]):
            winner = field[0][i]
    if turnCounter >= 9:
        winner = -1
    return winner

while not done:

    # This limits the while loop to a max of 200 times per second.
    clock.tick(200)

    for i in range(columns): #Draw TicTacToe playfield
        for j in range(rows):
            pygame.draw.rect(screen, WHITE, [size[0] / 3 * i, size[1] / 3 * j, rect[0], rect[1]], 2)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONUP: # Mouse click
            pos = pygame.mouse.get_pos() # Store mouse pos in variable
            fieldpos = field[int(pos[1] / 200)][int(pos[0] / 200)]
            if turn == 'X':
                if fieldpos == '': # Set X and set turn to O
                    field[int(pos[1] / 200)][int(pos[0] / 200)] = 'X'
                    turn = 'O'
                    turnCounter += 1
            else:
                if fieldpos == '': # Set O and set turn to X
                    field[int(pos[1] / 200)][int(pos[0] / 200)] = 'O'
                    turn = 'X'
                    turnCounter += 1

    for col in range(len(field)): #Draw X or O
        for x in range(len(field[col])):
            if field[col][x] == 'O':
                #draw O
                pygame.draw.circle(screen, WHITE, [size[0] / 3 * x + offsetCircle, size[1] / 3 * col + offsetCircle], radius, width)
            elif field[col][x] == 'X':
                #draw X
                pygame.draw.line(screen, WHITE, [size[0] / 3 * x + offsetCross, size[1] / 3 * col + offsetCross],
                                 [size[0] / 3 * (x + 1) - offsetCross, size[1] / 3 * (col + 1) - offsetCross],
                                 width) # left cross line
                pygame.draw.line(screen, WHITE, [size[1] / 3 * (x+1) - offsetCross, size[1] / 3 * col + offsetCross],
                                 [size[0] / 3 * x + offsetCross, size[1] / 3 * (col + 1) - offsetCross],
                                 width)  # left cross line
    pygame.display.flip() # update

    # Check board for win
    winner = checkWinner()
    if winner != None and winner != -1:
        print('The winner is: ' + winner)
        done = True
    elif winner == -1:
        print('draw')
        done = True

pygame.quit()