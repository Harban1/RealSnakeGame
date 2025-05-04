import pygame, random
pygame.init()

green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

snakeBoxSize = 50

difficulty = 2

fpsController = pygame.time.Clock()

direction = "left"

fontLarge = pygame.font.SysFont(None, 72)

fontSmall = pygame.font.SysFont(None, 36)

WINWIDTH = 800
WINHEIGHT = 600
GAMEWIN = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
pygame.display.set_caption("Snake Game")


def spawnfood():
    foodx = random.randrange(0, (WINWIDTH//snakeBoxSize))*snakeBoxSize  
    foody = random.randrange(0, (WINHEIGHT//snakeBoxSize))*snakeBoxSize
    return (foodx, foody)


def drawtext(size, colour, x, y, text, surface):
    textObject = size.render(text, True, colour)
    textRect = textObject.get_rect(center = (x, y))
    surface.blit(textObject, textRect)

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

def gameLoop():

    bob = Snake(direction)

    food = spawnfood()

    score = 0

    RUNNING = True
    while RUNNING:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bob.direction = "up"
                    
                if event.key == pygame.K_DOWN:
                    bob.direction = "down"
                   
                if event.key == pygame.K_RIGHT:
                    bob.direction = "right"
                    
                if event.key == pygame.K_LEFT:
                    bob.direction = "left"
                   
                if event.key == pygame.K_ESCAPE:
                    RUNNING = False

            if event.type == pygame.QUIT:
                RUNNING = False

        bob.move()

        head = bob.snakebody[0]

        if food == head:
            score += 1
            bob.grow()
            food = spawnfood() 

        if head[0] not in range(0, WINWIDTH) or head[1] not in range(0, WINHEIGHT):
            RUNNING = False

        GAMEWIN.fill((255, 255, 255))

        for segment in bob.snakebody:
            pygame.draw.rect(GAMEWIN, green, pygame.Rect(segment[0], segment[1], snakeBoxSize, snakeBoxSize))

        pygame.draw.rect(GAMEWIN, red, pygame.Rect(food[0], food[1], snakeBoxSize, snakeBoxSize))
        drawtext(fontSmall, black, 70, 25, f"Score: {score}", GAMEWIN)

        pygame.display.update()

        fpsController.tick(difficulty)

    return score

def main():
    highscore = 0
    while True:
        result = gameLoop()
        pygame.quit()
        if result is None:
            break


    pygame.quit()

if __name__ == "__main__":
    main()