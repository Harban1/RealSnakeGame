import pygame, random
pygame.init()
# 10 % 3 = 1
# 10 // 3 = 3

score = 0 

snakeBoxSize = 50

difficulty = 2

fpsController = pygame.time.Clock()

WINWIDTH = 800
WINHEIGHT = 600

def spawnfood():
    foodSpawn = [random.randrange(0, (WINWIDTH//snakeBoxSize))*snakeBoxSize  , random.randrange(0, (WINHEIGHT//snakeBoxSize))*snakeBoxSize]
    return foodSpawn

food = spawnfood()


GAMEWIN = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
pygame.display.set_caption("Snake Game")

green = (0, 255, 0)
red = (255, 0, 0)

direction = "left"

class Snake:
    def __init__(self, direction):
        self.direction = direction
        Startx = ((WINWIDTH // 2) // snakeBoxSize) * snakeBoxSize
        Starty = ((WINHEIGHT // 2) // snakeBoxSize) * snakeBoxSize
        self.snakebody = [(Startx, Starty)]
        self.growing = False

    def move(self):

        head = self.snakebody[0]
        headx = head[0]
        heady = head[1]
        #head_x, head_y = self.snakebody[0]

        if self.direction == "up":
            newHead = (head[0], head[1] - snakeBoxSize)
            heady -= snakeBoxSize

        if self.direction == "down":
            newHead = (head[0], head[1] + snakeBoxSize)
            heady += snakeBoxSize

        if self.direction == "left":
            newHead = (head[0] - snakeBoxSize , head[1])
            headx -= snakeBoxSize

        if self.direction == "right":
            newHead = (head[0] + snakeBoxSize, head[1])
            headx += snakeBoxSize

        self.snakebody.insert(0, newHead)
        #self.snakebody.pop()

        # if self.growing == False:
        #     self.snakebody.pop()

        if self.growing:
            self.growing = False
        else:
            self.snakebody.pop()

    def grow(self):

        #self.snakebody.insert(0, list(head))
        self.growing = True

bob = Snake("left")

# class Food:
#     def __init__(self, foodSpawn):
#         self.foodSpawn = foodSpawn

    

RUNNING = True
while RUNNING:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("The up arrow key has been pressed")
                bob.direction = "up"
                # bob.move()

            if event.key == pygame.K_DOWN:
                print("The down arrow key has been pressed")
                bob.direction = "down"
                # bob.move()

            if event.key == pygame.K_RIGHT:
                print("The right arrow key has been pressed")
                bob.direction = "right"
                # bob.move()


            if event.key == pygame.K_LEFT:
                print("The left arrow key has been pressed")
                bob.direction = "left"
                # bob.move()

            if event.key == pygame.K_ESCAPE:
                RUNNING = False

        if event.type == pygame.QUIT:
            RUNNING = False

    bob.move()

    
    head = bob.snakebody[0]

    if food[0] == head:
        score += 1
        bob.grow()
        food = spawnfood() 

    # if bob.x == foodSpawn[0] and bob.y == foodSpawn[1]:
    #     score += 1
    #     bob.grow()

    # if bob.x not in range(0, WINWIDTH) or bob.y not in range(0, WINHEIGHT):
    #     RUNNING = False




    GAMEWIN.fill((255, 255, 255))
    # pygame.draw.rect(GAMEWIN, green, pygame.Rect(bob.x, bob.y, snakeBoxSize, snakeBoxSize))

    for segment in bob.snakebody:
        pygame.draw.rect(GAMEWIN, green, pygame.Rect(segment[0], segment[1], snakeBoxSize, snakeBoxSize))


    pygame.draw.rect(GAMEWIN, red, pygame.Rect(food[0], food[1], snakeBoxSize, snakeBoxSize))
    pygame.display.update()

    fpsController.tick(difficulty)

pygame.quit()