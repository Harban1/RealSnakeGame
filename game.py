import pygame, random
pygame.init()

green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
lightblue = (91, 211, 245)

snakeBoxSize = 25

# difficulty = 5

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


def drawtext(font, colour, x, y, text, surface):
    textObject = font.render(text, True, colour)
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

        if self.direction == "left" :
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

def gameLoop(difficulty):

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

        GAMEWIN.fill(white)

        for segment in bob.snakebody:
            pygame.draw.rect(GAMEWIN, green, pygame.Rect(segment[0], segment[1], snakeBoxSize, snakeBoxSize))

        pygame.draw.rect(GAMEWIN, red, pygame.Rect(food[0], food[1], snakeBoxSize, snakeBoxSize))
        drawtext(fontSmall, black, 70, 25, f"Score: {score}", GAMEWIN)

        pygame.display.update()

        fpsController.tick(difficulty)

    return score

def gameOver(score, highscore):
    while True:
       GAMEWIN.fill(black)
       drawtext(fontLarge, white, WINWIDTH//2, WINHEIGHT//2 - 60, "GAME OVER", GAMEWIN)
       drawtext(fontSmall, white, WINWIDTH//2, WINHEIGHT//2, f"score: {score}  highscore: {highscore}", GAMEWIN)

       playButton = pygame.Rect(WINWIDTH//2 - 100, WINHEIGHT//2 + 100, 200, 50)
       quitButton = pygame.Rect(WINWIDTH//2 - 100, WINHEIGHT//2 + 170, 200, 50)
       pygame.draw.rect(GAMEWIN, white, playButton)
       pygame.draw.rect(GAMEWIN, white, quitButton)

       drawtext(fontSmall, black, playButton.centerx, playButton.centery, "PLAY AGAIN", GAMEWIN)
       drawtext(fontSmall, black, quitButton.centerx, quitButton.centery, "QUIT", GAMEWIN)

       pygame.display.update()
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               return False 
           if event.type == pygame.MOUSEBUTTONDOWN:
               mx, my = event.pos
               if playButton.collidepoint(mx, my):
                   return True
               if quitButton.collidepoint(mx, my):
                   return False 
              
def startscreen():
    """
    display start screen
    shows player differnt levels
    3 keys for different difficulties, when you press game starts
    """



    while True:
        GAMEWIN.fill(lightblue)
        drawtext(fontLarge, white, WINWIDTH//2, WINHEIGHT//2 - 60, "SNAKE GAME !!", GAMEWIN)

        # playButton =  pygame.Rect(WINWIDTH//2 - 100, WINHEIGHT//2 + 100, 200, 50)
        # pygame.draw.rect(GAMEWIN, white, playButton)
        # drawtext(fontSmall, black, playButton.centerx, playButton.centery, "PLAY", GAMEWIN)

        drawtext(fontSmall, white, WINWIDTH//2, WINHEIGHT//2 - 20, "Select difficulty: ", GAMEWIN)
        drawtext(fontSmall, white, WINWIDTH//2, WINHEIGHT//2 + 40, "Press 1 for easy ", GAMEWIN)
        drawtext(fontSmall, white, WINWIDTH//2, WINHEIGHT//2 + 70, "Press 2 for medium ", GAMEWIN)
        drawtext(fontSmall, white, WINWIDTH//2, WINHEIGHT//2 + 100, "Press 3 for hard ", GAMEWIN)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1:
                    difficulty = 3 
                    return difficulty
                
                elif event.key == pygame.K_2:
                    difficulty = 5 
                    return difficulty
                
                elif event.key == pygame.K_3:
                    difficulty = 7
                    return difficulty
                
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return None





def main():
    highscore = 0

    difficulty = startscreen()

    if difficulty == None:
        pygame.quit()
    
    while True:
        result = gameLoop(difficulty)

        if result is None:
            break

        if result > highscore:
            highscore = result

        playagain = gameOver(result, highscore)

        if not playagain:
            break

        difficulty = startscreen()

        if difficulty == None:
            break


    pygame.quit()

if __name__ == "__main__":
    main()