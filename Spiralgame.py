import pygame
import math

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Prime Spiral")

clock = pygame.time.Clock()


# ფერები
BLACK = (0, 0, 0)
GREEN = (0, 255, 100)
YELLOW = (255, 220, 0)
RED = (255, 0, 0)


# მარტივი რიცხვი
def is_prime(n):

    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n))+1):

        if n % i == 0:
            return False

    return True



# მოძრაობის მიმართულებები
moves = [
    (0, -4),   # ზემოთ
    (4, 0),    # მარჯვნივ
    (0, 4),    # ქვემოთ
    (-4, 0)    # მარცხნივ
]
direction = 0
# საწყისი ადგილი

x = WIDTH // 2
y = HEIGHT // 2
number = 1
# გავლილი გზა
path = []
running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # მოძრაობა
    dx, dy = moves[direction]

    x += dx
    y += dy
    # შენახვა
    path.append(
        (x, y, number)
    )
    number += 1
    # თუ მარტივია -> მარჯვნივ

    if is_prime(number):
        direction += 1


        if direction == 4:
            direction = 0
    # გზის დახატვა
    for px, py, n in path:
        if is_prime(n):
            color = YELLOW
            size = 5
        else:
            color = GREEN
            size = 2
        pygame.draw.circle(
            screen,
            color,
            (px, py),
            size
        )
    # მოთამაშე
    pygame.draw.circle(
        screen,
        RED,
        (x,y),
        8
    )
    pygame.display.update()
    clock.tick(60)



pygame.quit()