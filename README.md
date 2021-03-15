import pygame
import random
import time

class Snake():
    def __init__(self):
        self.length = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (17, 24, 47)
        self.score = 0

    def head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    def text_objects(self, text, font):
        textsurface = font.render(text, True, (34, 67, 90))
        return textsurface, textsurface.get_rect()
    def display_text(self, text):
        largetext = pygame.font.Font("freesansbold.ttf", 50)
        textsurf, textrect = self.text_objects(text, largetext)
        textrect.center = ((screen_width / 2), (screen_height / 2))
        screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
        screen.blit(textsurf, textrect)
        pygame.display.update()
        time.sleep(2)

    def crash(self):
        time.sleep(1)
        self.display_text("GAME OVER")
        self.display_text("YOUR SCORE : " + str(self.score))
        pygame.quit()
        quit()

    def move(self):
        cur = self.head_position()
        x, y = self.direction
        new = (((cur[0]+(x*gridsize)) % screen_width), (cur[1] + (y*gridsize)) % screen_height)
        if ((len(self.positions) > 2 and new in self.positions[2:]) or (new[0] < 5) or (new[0] > screen_width - 25) or (new[1] < 5) or (new[1] > screen_height - 25)):
            self.crash()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize, gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (23, 116, 228), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)

class Food():
    def __init__(self):
        self.position = (0, 0)
        self.color = (0, 0, 255)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(1, grid_width - 2)*gridsize, random.randint(1, grid_height - 2)*gridsize)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

def b_g(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x == 0 or x == grid_width - 1 or y == 0 or y == grid_height - 1):
                r = pygame.Rect((x*gridsize, y*gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, (255, 0, 0), r)
            else:
                rr = pygame.Rect((x*gridsize, y*gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, (255, 255, 255), rr)

screen_width = 600
screen_height = 400

gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

def game():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    b_g(surface)

    snake = Snake()
    food = Food()

    snake.display_text("THE SNAKE GAME")

    myfont = pygame.font.SysFont("monospace", 16)

    while (True):
        clock.tick(10)
        snake.handle_keys()
        b_g(surface)
        snake.move()
        if snake.head_position() == food.position:
            snake.length += 1
            if snake.score % 30 == 0 and snake.score != 0:
                snake.score += 10
            else:
                snake.score += 5
            if (snake.score) % 30 == 0:
                food.color = (255, 0, 0)
            else:
                food.color = (0, 0, 255)
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0, 0))
        text = myfont.render("Score {0}".format(snake.score), 1, (0, 0, 0))
        screen.blit(text, (20, 15))
        pygame.display.update()

game()
