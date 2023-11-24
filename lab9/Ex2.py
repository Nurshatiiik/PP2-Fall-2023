import pygame
pygame.init()
W, H = 332, 541
sc = pygame.display.set_mode((W, H))
bg = pygame.image.load("/Users/nurshatserik/pp22/images/player.jpg")
base_img = pygame.image.load("/Users/nurshatserik/pp22/images/TameImpala.png")
white_surf = pygame.Surface((230, 60))
white_surf.fill("white")
myfont = pygame.font.Font("/Users/nurshatserik/pp22/fonts/Lato-Black.ttf", 15)
music_name = myfont.render('house with normal phenomena', False, 'black')
myfont = pygame.font.Font("/Users/nurshatserik/pp22/fonts/Lato-Black.ttf", 15)
skrippi = myfont.render('TameImpala', False, 'black')
sound1 = pygame.mixer.Sound('/Users/nurshatserik/pp22/music/Eventually.mp3')
sound2 = pygame.mixer.Sound('/Users/nurshatserik/pp22/music/TheLessIKnowtheBetter.mp3')
sound3 = pygame.mixer.Sound('/Users/nurshatserik/pp22/music/NewPerson,SameOldMistakes.mp3')
music = [sound1, sound2, sound3]
music[0].play()
i = 0
while True:
    sc.fill("white")
    sc.blit(bg, (0, 0))
    sc.blit(base_img, (29, 22))
    sc.blit(white_surf, (17, 390))
    white_surf.blit(music_name, (0, 0))
    white_surf.blit(skrippi, (0, 30))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                music[i].stop()
                if i==5:
                    i = 0
                else:
                    i += 1
                music[i].play()
            elif event.key == pygame.K_LEFT:
                music[i].stop()
                if i==0:
                    i = 5
                else:
                    i -= 1
                music[i].play()
            elif event.key == pygame.K_SPACE:
                music[i].stop()
            elif event.key == pygame.K_TAB:
                music[i].play()
        elif event.type == pygame.QUIT:
            exit()
    pygame.display.update()