import pygame
pygame.init()

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
screenWidth = 1200
screenHeight = 600
half_sc = 300
vel = 9
x = 20
y = 236
a = 64
b = 64
obsticle_a = 64
run = True
isJump = False
jumpCount = 10

win = pygame.display.set_mode((screenWidth, screenHeight))

#main loop
while run:
    pygame.time.delay(40)
    good = pygame.Rect(x, y, a, b)
    bad = pygame.Rect(600, half_sc - obsticle_a, obsticle_a, obsticle_a)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screenWidth - a - vel:
        x += vel
    if keys[pygame.K_SPACE]:
        isJump = True
    if isJump:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    if good.colliderect(bad):
        pygame.quit()


    win.fill(WHITE)
    pygame.draw.rect(win, (GREEN), (0, screenHeight/2, screenWidth, screenHeight/2))
    pygame.draw.rect(win, BLACK, good)
    pygame.draw.rect(win, RED, bad)
    pygame.display.update()

pygame.quit()