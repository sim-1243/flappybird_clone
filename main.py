import stütze
import pygame
import random

pygame.init()
pygame.font.init()
score=0
screen_width = 1920
screen_height = 1080
l=screen_width//4
player=stütze.player(screen_width,screen_height)
rohre=[stütze.rohr(player.x+l +l*i,screen_height//2 +100,screen_height//2) for i in range(4)]
mirrohr=stütze.mirror(rohre)
screen = pygame.display.set_mode((screen_width, screen_height))
Font='Ubuntu-Title.ttf'
my_font=pygame.font.Font(Font,30)
müll=0
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    
    #screen prep

    screen.fill((0,0,0))
    #screen preped

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running=False
    if keys[pygame.K_SPACE]:
        player.move()
    player.gravity()
    player.draw(screen)

    for j in range(len(rohre)):
        rohre[j].speed()
        rohre[j].draw(screen)
        mirrohr[j].speed()
        mirrohr[j].draw(screen)
    
    if rohre[0].x <= 50:
        rohre.pop(0)
        mirrohr.pop(0)
        mirro,rohrrr=stütze.generator(screen_width,screen_height//2)
        mirrohr.append(mirro)
        rohre.append(rohrrr)
    if stütze.collision(player.x,rohre[0].x,player.y,rohre[0].y,player.width,player.height,rohre[0].width,rohre[0].height) or stütze.collision(player.x,mirrohr[0].x,player.y,mirrohr[0].y,player.width,player.height,mirrohr[0].width,mirrohr[0].height):
        running= False

    #screen time




    text_surf=my_font.render(str(score),False,(255,255,255))

    screen.blit(text_surf,(screen_width//2 - 40, 80))
    if müll == ((screen_width//4) // 5):
        score+=1
        müll=0
    müll+=1

    clock = pygame.time.Clock()
    clock.tick(60)
    pygame.display.flip()

pygame.quit
