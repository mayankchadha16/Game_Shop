import pygame
import time
import random
from tkinter import *

cost = 0


class Snake():
    def __init__(self):
        self.length = 1
        self.positions = [((screen_width / 2), (screen_height / 2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (17, 24, 47)
        self.score = 0

    def head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def text_objects(self, text, font):
        textsurface = font.render(text, True, (34, 67, 90))
        return textsurface, textsurface.get_rect()

    def display_text(self, text):
        pygame.font.init()
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
        global cost
        cost = cost + 120
        # pygame.quit()
        # quit()
        game_shop()

    def move(self):
        cur = self.head_position()
        x, y = self.direction
        new = (((cur[0] + (x * gridsize)) % screen_width), (cur[1] + (y * gridsize)) % screen_height)
        if ((len(self.positions) > 2 and new in self.positions[2:]) or (new[0] < 5) or (new[0] > screen_width - 25) or (
                new[1] < 5) or (new[1] > screen_height - 25)):
            self.crash()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((screen_width / 2), (screen_height / 2))]
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
        self.position = (random.randint(1, grid_width - 2) * gridsize, random.randint(1, grid_height - 2) * gridsize)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)


def b_g(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x == 0 or x == grid_width - 1 or y == 0 or y == grid_height - 1):
                r = pygame.Rect((x * gridsize, y * gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, (255, 0, 0), r)
            else:
                rr = pygame.Rect((x * gridsize, y * gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, (255, 255, 255), rr)


screen_width = 800
screen_height = 600

gridsize = 20
grid_width = int(screen_width / gridsize)
grid_height = int(screen_height / gridsize)

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

snake = Snake()
food = Food()


def snake_game():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    b_g(surface)

    # snake = Snake()
    # food = Food()
    snake.display_text("WELCOME")

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
        text = myfont.render("Score {0}".format(snake.score), True, (0, 0, 0))
        screen.blit(text, (20, 15))
        pygame.display.update()


def game_2():
    import random
    import pygame

    pygame.init()
    window = pygame.display.set_mode([500, 500])

    pygame.display.set_caption("Rock, Paper and Scissor")

    image = pygame.image.load(r'rps.jpg')

    playing = True

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

        window.fill((255, 255, 255))
        window.blit(image, (0, 0))

        pygame.display.update()

    pygame.quit()

    print()

    print("**************************************************")
    print("Welcome to Game Number 2 --- Rock,Paper or Scissor")
    print("**************************************************")

    print()
    x = 'Y'

    while x == 'Y':
        print("Play with a friend --- Press 1")
        print("Play with computer --- Press 2")

        print()

        def game(p1, p2):
            if p1 == p2:
                return None

            elif p2 == 's':
                if p1 == 'p':
                    return False
                elif p1 == 'r':
                    return True

            elif p2 == 'r':
                if p1 == 's':
                    return False
                elif p1 == 'p':
                    return True

            elif p2 == 'p':
                if p1 == 'r':
                    return False
                elif p1 == 's':
                    return True

        i = int(input("Time To Play---"))

        print()

        opponent = random.randint(1, 3)

        if i == 1:
            player1 = input("Player1 Turn: Rock(r) Paper(p) or Scissor(s)---")
            print()
            player2 = input("Player2 Turn: Rock(r) Paper(p) or Scissor(s)---")
            print()
            a = game(player1, player2)

            if a is None:
                print("The game is a tie!")
            elif a:
                print("Player1 Wins!")
            else:
                print("Player2 Wins!")

        elif i == 2:
            print("Computer Turn: Rock(r) Paper(p) or Scissor(s)")

            print()

            if opponent == 1:
                comp = 'r'

            elif opponent == 2:
                comp = 'p'

            elif opponent == 3:
                comp = 's'
            player = input("Your Turn: Rock(r) Paper(p) or Scissor(s)---")
            a = game(comp, player)
            print(f"Computer chose {comp}")
            print(f"You chose {player}")

            if a is None:
                print("The game is a tie!")
            elif a:
                print("You Lose!")
            else:
                print("You Win!")
            print()

        x = input("Wanna play again Yes(Y) or No(N)---")
        print()

        if x == 'N':
            print("Thanks Sir/Mam!")
            print()
        global cost
        cost += 120

    game_shop()


def game_3():
    import pygame

    pygame.init()
    window = pygame.display.set_mode([720, 480])

    pygame.display.set_caption("Hangaroo")

    image = pygame.image.load(r'hangaroo.jpg')
    font = pygame.font.Font('freesansbold.ttf', 32)

    text = font.render('My Inspiration', True, (0, 255, 0), (0, 0, 128))

    textrect = text.get_rect()

    textrect.center = (720 // 2, 100 // 2)

    playing = True

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

        window.fill((255, 255, 255))
        window.blit(image, (0, 0))
        window.blit(text, textrect)

        pygame.display.update()

    pygame.quit()

    snake.display_text("WELCOME")
    global cost
    cost += 120

    def hangaroo(res=None):
        global ss, ll, ss1, n, ffdata, temps, first
        first = inpp.get()
        input1.delete(0, END)
        if n > 0:
            if first in ss:
                for i in range(ss1):
                    if ss[i] == first and ll[i] == '*':
                        ll.pop(i)
                        ll.insert(i, ss[i])
                        xx = ''.join(ll)
                        ss = list(ss)
                        ss.pop(i)
                        ss.insert(i, "*")
                        unknown.configure(text=xx)
                        if xx == temps:
                            # ans.configure(text='Congratulations')

                            if res:
                                chooseword()
                            else:
                                root.destroy()
                        else:
                            break
            else:
                n -= 1
                chances_left.configure(text='Left = {}'.format(n))
        if n <= 0:
            # ans.configure(text='Better luck next time')

            if res:
                chooseword()
            else:
                root.destroy()

    def jj(event):
        hangaroo()

    from tkinter import messagebox
    import random

    options = ['kumar', 'rahul', 'gupta', 'prem', 'keshav', 'sujit', 'eshita']

    root = Tk()
    root.geometry('800x500+300+100')
    root.configure(bg='cyan')
    root.title('Hangaroo')

    intro = Label(root, text='Welcome to Game Number 3---Hangaroo ', font=('arial', 25, 'bold'), bg='cyan')
    intro.place(x=100, y=0)

    unknown = Label(root, text='', font=('arial', 45, 'bold'), bg='cyan')
    unknown.place(x=300, y=150)

    chances_left = Label(root, text='', font=('arial', 25, 'bold'), bg='cyan')
    chances_left.place(x=650, y=100)

    ans = Label(root, text='', font=('arial', 25, 'bold'), bg='cyan')
    ans.place(x=100, y=440)

    inpp = StringVar()
    input1 = Entry(root, font=('arial', 25, 'bold'), relief=RIDGE, bd=5, bg='green', justify='center', fg='white',
                   textvariable=inpp)
    input1.place(x=210, y=250)

    bt1 = Button(root, text='Submit', font=('arial', 15, 'bold'), width=15, bd=5, bg='red', activebackground='blue'
                 , activeforeground='white', command=hangaroo)
    bt1.place(x=300, y=350)
    root.bind("<Return>", jj)

    def chooseword():
        global ss, ll, ss1, n, ffdata, temps
        ss = random.choice(options)
        ll = ["*" for i in ss]
        ss1 = len(ss)
        n = ss1
        temps = ss
        chances_left.configure(text='Left = {}'.format(n))
        ffdata = ''
        for i in ll:
            ffdata += i + ' '
        unknown.configure(text=ffdata)
        ans.configure(text='')

    chooseword()
    root.mainloop()
    game_shop()


def game_4():
    import tkinter
    import random

    snake.display_text("WELCOME")

    colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
               'Yellow', 'Orange', 'White', 'Purple', 'Brown']
    score = 0

    timeleft = 30

    def startGame(event):
        if timeleft == 30:
            countdown()
        nextColour()

    def nextColour():
        global score
        global timeleft

        if timeleft > 0:

            e.focus_set()

            if e.get().lower() == colours[1].lower():
                score += 1

            e.delete(0, tkinter.END)

            random.shuffle(colours)

            label.config(fg=str(colours[1]), text=str(colours[0]))

            scoreLabel.config(text="Score: " + str(score))

    def countdown():
        global timeleft

        if timeleft > 0:
            timeleft -= 1

            timeLabel.config(text="Time left: "
                                  + str(timeleft))

            timeLabel.after(1000, countdown)

    root = tkinter.Tk()

    root.title("COLORGAME")

    root.geometry("375x200")

    instructions = tkinter.Label(root, text="Type in the colour"
                                            "of the words, and not the word text!",
                                 font=('Helvetica', 12))
    instructions.pack()

    scoreLabel = tkinter.Label(root, text="Press enter to start",
                               font=('Helvetica', 12))
    scoreLabel.pack()

    timeLabel = tkinter.Label(root, text="Time left: " +
                                         str(timeleft), font=('Helvetica', 12))

    timeLabel.pack()

    label = tkinter.Label(root, font=('Helvetica', 60))
    label.pack()

    e = tkinter.Entry(root)

    root.bind('<Return>', startGame)
    e.pack()

    e.focus_set()

    root.mainloop()

    global cost
    cost += 120
    snake.display_text("GAME OVER")
    game_shop()


def Calculator():
    def click(event):
        global scvalue
        text = event.widget.cget("text")
        if text == "=":
            if scvalue.get().isdigit():
                value = int(scvalue.get())
            else:
                try:
                    value = eval(screen.get())

                except Exception as e:
                    print(e)
                    value = "Error"

            scvalue.set(value)
            screen.update()

        elif text == "C":
            scvalue.set("")
            screen.update()

        else:
            scvalue.set(scvalue.get() + text)
            screen.update()

    root = Tk()
    root.configure(background="spring green")
    root.geometry("320x360")

    root.title("CALCULATOR ")

    scvalue = StringVar()
    scvalue.set("")
    screen = Entry(root, textvar=scvalue, font="lucida 25 bold")
    screen.pack(fill=X, ipadx=5, pady=15, padx=5)

    f = Frame(root, bg="black")
    b = Button(f, text="9", padx=12, pady=2, font="lucida 15 bold")
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)

    b = Button(f, text="8", padx=12, pady=2, font="lucida 15 bold")
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)

    b = Button(f, text="7", padx=12, pady=2, font="lucida 15 bold")
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)

    f.pack()

    f = Frame(root, bg="black")
    b = Button(f, text="6", padx=12, pady=2, font="lucida 15 bold")
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)

    b = Button(f, text="5", padx=12, pady=2, font="lucida 15 bold")
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)

    b = Button(f, text="4", padx=12, pady=2, font="lucida 15 bold")
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)

    f.pack()

    f = Frame(root, bg="black")
    b = Button(f, text="3", padx=12, pady=2, font="lucida 15 bold")
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)

    b = Button(f, text="2", padx=12, pady=2, font="lucida 15 bold")
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)

    b = Button(f, text="1", padx=12, pady=2, font="lucida 15 bold")
    b.pack(side=LEFT, padx=18, pady=2)
    b.bind("<Button-1>", click)

    f.pack()

    f = Frame(root, bg="black")
    b = Button(f, text="0", padx=12, pady=2, font="lucida 15 bold")
    b.pack(side=LEFT, padx=20, pady=2)
    b.bind("<Button-1>", click)

    b = Button(f, text="C", padx=12, pady=2, font="white 15 bold")
    b.pack(side=LEFT, padx=14, pady=2)
    b.bind("<Button-1>", click)

    b = Button(f, text="=", padx=12, pady=2, font="lucida 15 bold")
    b.pack(side=LEFT, padx=19, pady=2)
    b.bind("<Button-1>", click)

    f.pack()

    f = Frame(root, bg="black")
    b = Button(f, text="/", padx=11, pady=2, font="lucida 15 bold")
    b.pack(side=LEFT, padx=42, pady=2)
    b.bind("<Button-1>", click)

    b = Button(f, text="*", padx=12, pady=2, font="lucida 15 bold")
    b.pack(side=LEFT, padx=42, pady=2)
    b.bind("<Button-1>", click)

    f.pack()

    f = Frame(root, bg="black")
    b = Button(f, text="+", padx=12, pady=2, font="white 15 bold")
    b.pack(side=LEFT, padx=41, pady=2)
    b.bind("<Button-1>", click)

    b = Button(f, text="-", padx=14, pady=2, font="lucida 15 bold")
    b.pack(side=LEFT, padx=41, pady=2)
    b.bind("<Button-1>", click)

    f.pack()

    root.mainloop()
    game_shop()


def game_shop():
    clock = pygame.time.Clock()
    gameDisplay = pygame.display.set_mode((display_width, display_height), 0, 32)

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            gameDisplay.fill(white)
            pygame.font.init()
            largeText = pygame.font.Font('freesansbold.ttf', 115)
            TextSurf, TextRect = text_objects("THE GAME SHOP", largeText)
            TextRect.center = ((display_width / 2), (display_height / 2))
            gameDisplay.blit(TextSurf, TextRect)

        def button(msg, x, y, w, h, ic, ac, action=None):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if x + w > mouse[0] > x and y + h > mouse[1] > y:
                pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
                if click[0] == 1 and action != None:
                    action()
            else:
                pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

            smallText = pygame.font.Font("freesansbold.ttf", 20)
            textSurf, textRect = text_objects(msg, smallText)
            textRect.center = ((x + (w / 2)), (y + (h / 2)))
            gameDisplay.blit(textSurf, textRect)

        button("4. R_P_S", 750, 450, 200, 100, green, dark_green, game_2)
        button("3. COLOUR GAME", 50, 450, 200, 100, green, dark_green, game_4)
        button("2. HANGAROO", 750, 50, 200, 100, green, dark_green, game_3)
        button("1. SNAKE GAME", 50, 50, 200, 100, green, dark_green, snake_game)
        button("CALCULATOR", 400, 450, 200, 100, green, dark_green, Calculator)
        button("GENERATE BILL", 400, 50, 200, 100, green, dark_green, generate_bill)

        pygame.display.update()
        clock.tick(15)


white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
dark_green = (0, 200, 0)
display_width = 1000
display_height = 600


def text_objects(text, font):
    textsurface = font.render(text, True, (34, 67, 90))
    return textsurface, textsurface.get_rect()

def generate_bill():
    global cost
    cost += 20
    str = f"The Total cost generated is {cost}"
    snake.display_text(str)
    pygame.quit()
    quit()

game_shop()
