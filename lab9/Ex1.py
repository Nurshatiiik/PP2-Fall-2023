import pygame
import datetime
pygame.init()
W, H = 800, 800
x = W//2
y = H//2
WHITE = (255, 255, 255)
sc = pygame.display.set_mode((W, H))
current_date = datetime.datetime.now()
minutes = current_date.strftime("%M")
seconds = current_date.strftime("%S")
start_point_min = (int(minutes)/60)*360
start_point_sec = (int(seconds)/60)*360

mickey = pygame.image.load("/Users/nurshatserik/pp22/images/main-clock.png")
leftHand = pygame.image.load("/Users/nurshatserik/pp22/images/left-hand.png")
rightHand = pygame.image.load("/Users/nurshatserik/pp22/images/right-hand.png")
mickeyRect = mickey.get_rect()
def blitRotateCenter(surf, image, center, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = center).center)
    surf.blit(rotated_image, new_rect)
langle = -start_point_sec+90
rangle = -start_point_min+90
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    langle -= 60/360
    rangle -= 1/360
    
    sc.fill(WHITE)
    sc.blit(mickey, (x, y))
    sc.blit(mickey, mickeyRect)
    
    blitRotateCenter(sc, leftHand, (x,y), langle) 
    blitRotateCenter(sc, rightHand, (x,y), rangle)
    pygame.display.update()