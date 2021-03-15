import random
import pygame

pygame.init()
window = pygame.display.set_mode([500, 500])

image = pygame.image.load(r'C:\Users\Mayank\Documents\Pygame\rps.jpg')

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
