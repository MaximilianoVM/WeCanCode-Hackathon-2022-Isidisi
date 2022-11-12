import pygame

class Jugador(pygame.sprite.Sprite):
    def __init__(self, x, y, dalt, religion):
        super().__init__()

        self.x = x
        self.y = y

        self.frames = []
        self.frame_index = 0

        #=================== CRISTIANO ===================#
        if religion == 'cristiano' :
            #=================== SIN DALTONISMO
            if dalt == False:
                jugador1 = pygame.transform.scale2x(pygame.image.load('assets/TupacCristiano/Caleb1.png').convert_alpha())
                jugador2 = pygame.transform.scale2x(pygame.image.load('assets/TupacCristiano/Caleb2.png').convert_alpha())
                jugador3 = pygame.transform.scale2x(pygame.image.load('assets/TupacCristiano/Caleb3.png').convert_alpha())
                jugador4 = pygame.transform.scale2x(pygame.image.load('assets/TupacCristiano/Caleb4.png').convert_alpha())
                jugador5 = pygame.transform.scale2x(pygame.image.load('assets/TupacCristiano/Caleb5.png').convert_alpha())
                jugador6 = pygame.transform.scale2x(pygame.image.load('assets/TupacCristiano/Caleb6.png').convert_alpha())
                jugador7 = pygame.transform.scale2x(pygame.image.load('assets/TupacCristiano/Caleb7.png').convert_alpha())
                jugador8 = pygame.transform.scale2x(pygame.image.load('assets/TupacCristiano/Caleb8.png').convert_alpha())

                self.jugadorWalk = [jugador1, jugador2, jugador3, jugador4, jugador5, jugador6, jugador7, jugador8]
            #=================== DALTONISMO
            else:
                print("dalt")
        
        #==================== MEXICA ====================#
        elif religion == 'mexica':
            #=================== SIN DALTONISMO
            if dalt == False:
                jugador1 = pygame.transform.scale2x(pygame.image.load('assets/TupacMexica/Canek1.png').convert_alpha())
                jugador2 = pygame.transform.scale2x(pygame.image.load('assets/TupacMexica/Canek2.png').convert_alpha())
                jugador3 = pygame.transform.scale2x(pygame.image.load('assets/TupacMexica/Canek3.png').convert_alpha())
                jugador4 = pygame.transform.scale2x(pygame.image.load('assets/TupacMexica/Canek4.png').convert_alpha())
                jugador5 = pygame.transform.scale2x(pygame.image.load('assets/TupacMexica/Canek5.png').convert_alpha())
                jugador6 = pygame.transform.scale2x(pygame.image.load('assets/TupacMexica/Canek6.png').convert_alpha())
                jugador7 = pygame.transform.scale2x(pygame.image.load('assets/TupacMexica/Canek7.png').convert_alpha())
                jugador8 = pygame.transform.scale2x(pygame.image.load('assets/TupacMexica/Canek8.png').convert_alpha())

                self.jugadorWalk = [jugador1, jugador2, jugador3, jugador4, jugador5, jugador6, jugador7, jugador8]
            #=================== DALTONISMO
            else:
                print("dalt")
        
        self.jugador_index = 0
        self.image = self.jugadorWalk[self.jugador_index]
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))

    def animationState(self):
        self.jugador_index += 0.3
        if self.jugador_index >= len(self.jugadorWalk):
            self.jugador_index = 0
        self.image = self.jugadorWalk[int(self.jugador_index)]
    
    @staticmethod
    def playerInput(self, event, player1, player2):
        if event.key == pygame.K_DOWN:
            print('down')
            player1.sprite.rect.y += 64
            player2.sprite.rect.y += 64

        if event.key == pygame.K_UP:
            print('up')
            player1.sprite.rect.y -= 64
            player2.sprite.rect.y -= 64

        if event.key == pygame.K_LEFT:
            print('left')
            player1.sprite.rect.x -= 64
            player2.sprite.rect.x -= 64

        if event.key == pygame.K_RIGHT:
            print('right')
            player1.sprite.rect.x += 64
            player2.sprite.rect.x += 64

    def update(self):
        self.animationState()
    
    def collision_meta(self, meta):
        if self.rect.colliderect(meta.rect):
            return True
        else:
            return False
