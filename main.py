import pygame
from pygame.locals import *
import sys, os

GRIS = (159, 163, 173)
FPS = 60

class WalkJump(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.w = 160
        self.h = 256
        
        # Inicializamos el Sprite, (ver pygame.doc)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.w,self.h), pygame.SRCALPHA, 32)
        # Convertimos la imagen en un rectangulo con x,y,w,h, -> devuelve (0,0,68,40)
        self.rect = self.image.get_rect()
        # Coordenadas de entrada para posicionamiento -> Pos(x,y)
        self.rect.x = x
        self.rect.y = y
        
        # Preparacion de los frames
        # Alamacenamos los frames en una lista
        self.frames = []
        self.index = 0
        self.num_imagenes = 0
        self.tiempo_animacion = FPS // 2 
        
        # Cargamos la imagen
        self.load_frames()
        
    def load_frames(self):
        sprite_sheet = pygame.image.load('resources/walkJump.png').convert_alpha()
        
        for fila in range(3):
            y = fila * self.h
            for columna in range(6):
                x = columna * self.w
                
                image = pygame.Surface((self.w, self.h), pygame.SRCALPHA).convert_alpha()
                image.blit(sprite_sheet, (0,0), (x, y, self.w, self.h))
                self.frames.append(image)
                
        self.num_imagenes = len(self.frames) 
        self.image = self.frames[self.index]
            

class Game():
    clock = pygame.time.Clock()
    
    def __init__(self):
        # Inicialización de la superficie de dibujo (display surface)
        self.display = pygame.display
        # Establecemos el largo y ancho de la pantalla.
        self.dimensiones = [800, 600]
        self.pantalla = pygame.display.set_mode(self.dimensiones)
        # Titulo de la barra de la aplicacion
        pygame.display.set_caption('walkJumpPygame')
        
        # Instanciamos un WalkJump (personaje)
        personaje = WalkJump(340,300)
        # Creamos un grupo de Sprites
        self.allSprites = pygame.sprite.Group()
        self.allSprites.add(personaje)
        
    
    def game_over(self):
        pygame.quit()
        # No Olvidar pasar 0 en sys.exit(0), sin el parametro -> "Exception has occurred: SystemExit"
        sys.exit(0)
        
    def render(self, dt):
        self.pantalla.fill(GRIS)
        
        # Actualizamos todos los sprite del grupo
        # Hacemos la llamada del metodo update de Sprite
        self.allSprites.update(dt)
        # Pintamos los Sprite del grupo actualizados
        self.allSprites.draw(self.pantalla)
        
        
        # Actualizamos la pantalla con lo dibujado.
        self.display.flip()
            
    def manejador_eventos(self):
        # Manejador de eventos, un daemon o broker a la espera llamado desde bucle principal
        for evento in pygame.event.get():
            # Sí, pulsa Salir
            if evento.type == pygame.QUIT or evento.type == KEYDOWN and evento.key == K_ESCAPE:
                self.game_over()
            
    def main_loop(self):
        while True:
            # tiempo_transcurrido
            dt = self.clock.tick(FPS)
            self.manejador_eventos()
            self.render(dt)
            
if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.main_loop()
    