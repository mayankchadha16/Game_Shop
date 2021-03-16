import pygame

pygame.init()
window = pygame.display.set_mode([720, 480])

image = pygame.image.load(r'C:\Users\Mayank\Documents\Pygame\hangaroo.jpg')
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

options = ['kumar', 'rahul', 'advait', 'prem', 'keshav', 'sujit', 'eshita']

root = Tk()
root.geometry('800x500+300+100')
root.configure(bg='cyan')
root.title('Hangman Game')

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
