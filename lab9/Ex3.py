import pygame 
pygame.init()
W, H = 690, 690
sc = pygame.display.set_mode((W, H))
ball = pygame.Surface((50, 50))
ball.fill('white')
speed = 20
ball_x = 0
ball_y = 0
while True:
    sc.fill('white')
    sc.blit(ball, (ball_x, ball_y))
    pygame.draw.circle(ball, "Red", (25, 25), 25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if ball_x < W-60:
                    ball_x += speed
            if event.key == pygame.K_LEFT:
                if ball_x > 0:
                    ball_x -= speed
            if event.key == pygame.K_DOWN:
                if ball_y < H-60:
                    ball_y += speed
            if event.key == pygame.K_UP:
                if ball_y > 0:
                    ball_y -= speed
    pygame.display.update()