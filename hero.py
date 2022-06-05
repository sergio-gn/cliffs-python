import pygame

class Hero():
    #------------variaveis
    jump_force = 15
    jump_count = 0
    jump_enabled = True
    floor = 155


    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 42, 90))
        self.vel_y = 0

    def draw(self, surface):
        pygame.draw.rect(surface, (255,0, 0), self.rect)


    def move(self, screen_width, screen_height):
        #-----------------------------INPUT COM TECLAS-----------
        #variaveis para acontecer isso
        SPEED = 10
        GRAVITY = 1
        dx = 0
        dy = 0
        comando = pygame.key.get_pressed()
        #condicao pra acontecer isso
        if comando [pygame.K_LEFT]:
            dx = -SPEED
        if comando [pygame.K_RIGHT]:
            dx = SPEED

        if self.jump_enabled == True: 
            if comando [pygame.K_UP]:
                self.vel_y = - self.jump_force
        else:
            if comando [pygame.K_UP]:
                self.vel_y = 0

        

        self.vel_y += GRAVITY
        dy += self.vel_y

        #manter o personagem sempre dentro da tela
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
         #lutador fica dentro da tela verticalmente
        if self.rect.bottom + dy > screen_height - self.floor:
            self.vel_y = 0
            dy = screen_height - self.floor - self.rect.bottom
            self.jump_count = 0
        #update da tela pra acontecer isso
        self.rect.x += dx
        self.rect.y += dy