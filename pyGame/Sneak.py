import random
import pygame
pygame.init()

# Colors Code

white = (255,255,255)
green =(0,255,0)
red = (255,0,0)
black =(0,0,0)

# Window Creation

pygame.display.set_caption("Nagin  Game")
gameWindow = pygame.display.set_mode((900,700))

# Game instructions After Ending

game_over = False
game_end = False
game_restart = False

# importent add ons

nagin_x = 45
nagin_y = 55
nagin_size = 10
fps = 45
velocity_x = 0
velocity_y= 0
score =0
food_x=random.randint(0,700)
food_y=random.randint(0,500)
clock=pygame.time.Clock()



font = pygame.font.SysFont(None,55)
def textscreen(text , color , x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

# Game loop Codes

while not game_end :
    for event in pygame.event.get() :
        if event.type==pygame.QUIT :
            game_end= True
        if event.type == pygame.KEYDOWN :
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                velocity_x = 4
                velocity_y=0
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a ):
                velocity_x = -4
                velocity_y=0
            if (event.key == pygame.K_UP or event.key == pygame.K_w):
                velocity_y = -4
                velocity_x=0
            if (event.key == pygame.K_DOWN or event.key == pygame.K_s) :
                velocity_y = 4
                velocity_x=0
    nagin_x =  nagin_x + velocity_x
    nagin_y = nagin_y + velocity_y
    if abs(nagin_x-food_x) < 6  and abs(nagin_y-food_y)< 6 :
        score += 1
        food_x = random.randint(20, 700 )
        food_y = random.randint(20, 500 )
    gameWindow.fill(black)
    textscreen("Score:-> " + str(score), green, 5, 5)
    pygame.draw.rect(gameWindow,red,[food_x ,food_y,nagin_size,nagin_size])
    pygame.draw.rect(gameWindow,white,[nagin_x ,nagin_y,nagin_size,nagin_size])
    pygame.display.update()
    clock.tick(fps)

# Quitting Programme
pygame.quit()
quit()