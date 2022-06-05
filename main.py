import pygame
from hero import Hero


#variaveis pra aparecer o background
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#variavel da framerate do jogo
clock = pygame.time.Clock()
FPS = 60
#variavel e funcao pra desenhar o background
bg_image = pygame.image.load("bg.png").convert_alpha()
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(bg_image, (0, 0))

#-------instancia de personagens
hero = Hero(200, 475)

#------------------------------------------LOOP-PRINCIPAL-------------------------------------------------------------------------------------------------
run = True
while run:
    #framerate do jogo
    clock.tick(FPS)
    #executar funcao do background
    draw_bg()
    #mover personagens
    hero.move(SCREEN_WIDTH, SCREEN_HEIGHT)
    #desenhar personagens na tela
    hero.draw(screen)

    #loop para poder fechar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #update 
    pygame.display.update()