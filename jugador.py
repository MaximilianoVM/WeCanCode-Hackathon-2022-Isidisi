import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self, x, y, dalt, religion):
        super().__init__()

        self.x = x
        self.y = y

        self.frames = []
        self.frame_index = 0

        self.image = pygame.image.load('assets/Sprite-0006.png').convert_alpha() # Cambiar Sprite
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))

        #=================== CRISTIANO ===================#
        if religion == 'cristiano' :
            #=================== SIN DALTONISMO
            if dalt == False:
                jugador1 = pygame.transform.scale2x(pygame.image.load('assets/Caleb/Caleb1.png').convert_alpha())
                jugador2 = pygame.transform.scale2x(pygame.image.load('assets/Caleb/Caleb2.png').convert_alpha())
                jugador3 = pygame.transform.scale2x(pygame.image.load('assets/Caleb/Caleb3.png').convert_alpha())
                jugador4 = pygame.transform.scale2x(pygame.image.load('assets/Caleb/Caleb4.png').convert_alpha())
                jugador5 = pygame.transform.scale2x(pygame.image.load('assets/Caleb/Caleb5.png').convert_alpha())
                jugador6 = pygame.transform.scale2x(pygame.image.load('assets/Caleb/Caleb6.png').convert_alpha())
                jugador7 = pygame.transform.scale2x(pygame.image.load('assets/Caleb/Caleb7.png').convert_alpha())
                jugador8 = pygame.transform.scale2x(pygame.image.load('assets/Caleb/Caleb8.png').convert_alpha())

                self.jugadorWalk = [jugador1, jugador2, jugador3, jugador4, jugador5, jugador6, jugador7, jugador8]
            #=================== DALTONISMO
            else:
                print("dalt")
        
        #==================== MEXICA ====================#
        elif religion == 'mexica':
            #=================== SIN DALTONISMO
            if dalt == False:
                jugador1 = pygame.transform.scale2x(pygame.image.load('assets/Mexica/Mexica1.png').convert_alpha())
                jugador2 = pygame.transform.scale2x(pygame.image.load('assets/Mexica/Mexica2.png').convert_alpha())
                jugador3 = pygame.transform.scale2x(pygame.image.load('assets/Mexica/Mexica3.png').convert_alpha())
                jugador4 = pygame.transform.scale2x(pygame.image.load('assets/Mexica/Mexica4.png').convert_alpha())
                jugador5 = pygame.transform.scale2x(pygame.image.load('assets/Mexica/Mexica5.png').convert_alpha())
                jugador6 = pygame.transform.scale2x(pygame.image.load('assets/Mexica/Mexica6.png').convert_alpha())
                jugador7 = pygame.transform.scale2x(pygame.image.load('assets/Mexica/Mexica7.png').convert_alpha())
                jugador8 = pygame.transform.scale2x(pygame.image.load('assets/Mexica/Mexica8.png').convert_alpha())

                self.jugadorWalk = [jugador1, jugador2, jugador3, jugador4, jugador5, jugador6, jugador7, jugador8]
            #=================== DALTONISMO
            else:
                print("dalt")
        
        self.jugador_index = 0
        self.image = self.jugadorWalk[self.jugador_index]
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))

    def playerInput(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= 5
            self.jugador_index += 1
            if self.jugador_index >= len(self.jugadorWalk):
                self.jugador_index = 0
            self.image = self.jugadorWalk[self.jugador_index]

        if keys[pygame.K_RIGHT] and self.rect.x < 1212:
            self.rect.x += 5
            self.jugador_index += 1
            if self.jugador_index >= len(self.jugadorWalk):
                self.jugador_index = 0
            self.image = self.jugadorWalk[self.jugador_index]

        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= 5
            self.jugador_index += 1
            if self.jugador_index >= len(self.jugadorWalk):
                self.jugador_index = 0
            self.image = self.jugadorWalk[self.jugador_index]

        if keys[pygame.K_DOWN] and self.rect.y < 656:
            self.rect.y += 5
            self.jugador_index += 1
            if self.jugador_index >= len(self.jugadorWalk):
                self.jugador_index = 0
            self.image = self.jugadorWalk[self.jugador_index]

    def animationState(self):
        self.jugador_index += 0.5
        if self.jugador_index >= len(self.jugadorWalk):
            self.jugador_index = 0
        self.image = self.jugadorWalk[int(self.jugador_index)]

    def update(self):
        self.playerInput()
        self.animationState()
    

