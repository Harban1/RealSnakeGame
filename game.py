import pygame, random
pygame.init()
# 10 % 3 = 1
# 10 // 3 = 3

score = 0 

snakeBoxSize = 10

snakehead = (0,0)

difficulty = 10

fpsController = pygame.time.Clock()

WINWIDTH = 800
WINHEIGHT = 600

foodSpawn = [(random.randrange(1, (WINWIDTH//snakeBoxSize)*snakeBoxSize)), (random.randrange(1, (WINHEIGHT//snakeBoxSize)*snakeBoxSize))]
foodSpawnCondition = True

GAMEWIN = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
pygame.display.set_caption("Snake Game")

green = (0, 255, 0)
red = (255, 0, 0)

direction = "left"

class Snake:
    def __init__(self, snakebody, direction, x, y):
        self.snakebody = [snakebody]
        self.direction = direction
        self.y = y
        self.x = x

    def move(self):

        head = self.snakebody[0]
        
        if self.direction == "up":
            newHead = (head[0], head[1] + 1 )
            self.y -= snakeBoxSize

        if self.direction == "down":
            newHead = (head[0], head[1] - 1)
            self.y += snakeBoxSize

        if self.direction == "left":
            newHead = (head[0] - 1 , head[1])
            self.x -= snakeBoxSize

        if self.direction == "right":
            newHead = (head[0] + 1, head[1])
            self.x += snakeBoxSize

        self.snakebody.insert(0, newHead)
        self.snakebody.pop()

bob = Snake(snakehead, "left", 365, 265)

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

    if bob.x == foodSpawn[0] and bob.y == foodSpawn[1]:
        score += 1

    if bob.x not in range(0, WINWIDTH) and bob.y not in range(0, WINHEIGHT):
        RUNNING = False


    GAMEWIN.fill((255, 255, 255))
    pygame.draw.rect(GAMEWIN, green, pygame.Rect(bob.x, bob.y, snakeBoxSize, snakeBoxSize))
    pygame.display.update()

    fpsController.tick(difficulty)

pygame.quit()