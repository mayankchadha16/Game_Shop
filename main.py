# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/





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
        if (self.score < 100):
            self.display_text("Pay : " + str(100))
        elif(self.score >= 100 and self.score < 300):
            self.display_text("Pay : " + str(200))
        else:
            self.display_text("Pay : " + str(300))
        pygame.quit()
        # quit()

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

def snake_game():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    b_g(surface)

    snake = Snake()
    food = Food()
    snake.display_text("WELCOME TO GAME-1")
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

snake_game()

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
cost = 0
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

    cost += 100
cost += 20

print(f"Pay:{cost}")



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

print()

print("*************************************")
print("Welcome to Game Number 3 --- Hangaroo")
print("*************************************")

print()

print("Loading the gaming window............")
print("Please Wait")

cost = 100


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
                        ans.configure(text='Congratulations')
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
        ans.configure(text='Better luck next time')
        if res:
            chooseword()
        else:
            root.destroy()


def jj(event):
    hangaroo()


from tkinter import *
from tkinter import messagebox
import random

options = ['kumar', 'rahul', 'prem', 'keshav', 'sujit', 'eshita']

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
print()
print("Pay:", cost)

import tkinter
import random

print("********************************************")
print("Welcome to Game Number 4 --- The Colour Game")
print("********************************************")

print()

print("Loading the gaming window...................")
print("Please Wait")

cost = 0

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

cost += 100

print("Pay:", cost)


# clculator

from tkinter import *


def click(event):
    global sc_value
    text = event.widget.cget('text')
    if text == '=':
        if sc_value.get().isdigit():
            value = int(sc_value.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"
        sc_value.set(value)
        screen.update()
    elif text == 'C':
        sc_value.set("")
        screen.update()
    elif text == '<--':
        sc_value.set(sc_value.get()[:-1])
        screen.update()
    else:
        try:
            sc_value.set(sc_value.get() + text)
            screen.update()
        except Exception:
            print("something is wrong")


root = Tk()
root.geometry("284x362")
root.maxsize(284, 362)
root.minsize(284, 362)
root.title("CALCULATOR")
root.configure(background="spring green")

sc_value = StringVar()
sc_value.set('')
screen = Entry(root, textvar=sc_value, font="lucida 20 bold")
screen.place(x=10, y=15, width=261, height=51)
screen.bind("<Key>", lambda e: "break")

f1 = Frame(root, bg="grey").pack()

xpos = [10, 80, 150, 220, 10, 150, 220]
ypos = [130, 190, 250, 310, 80]
x_loop = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6]
y_loop = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4]
wpos = [51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 121, 51, 51, 51]
fix = ['9', '8', '7', '+', '6', '5', '4', '-', '3', '2', '1', '*', '%', '0', '.', '/', 'C', '<--', '=']
for y in range(0, 19):  # make All buttons in fix tuple
    b = Button(f1, text=fix[y], font="lucida 15 bold")
    b.place(x=xpos[x_loop[y]], y=ypos[y_loop[y]], width=wpos[y], height=41)
    b.bind("<Button-1>", click)

root.mainloop()