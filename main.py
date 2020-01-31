import pygame
from pygame.locals import *
import sys, os

GRIS = (159, 163, 173)
FPS = 60

class Game:
    clock = pygame.time.Clock()
    
    def __init__(self):
        # Inicialización de la superficie de dibujo (display surface)
        self.display = pygame.display
        # Establecemos el largo y ancho de la pantalla.
        self.dimensiones = [800, 600]
        self.pantalla = pygame.display.set_mode(self.dimensiones)
        
         # Titulo de la barra de la aplicacion
        pygame.display.set_caption('walkJumpPygame')
        
    
    def game_over(self):
        pygame.quit()
        # No Olvidar pasar 0 en sys.exit(0), sin el parametro -> "Exception has occurred: SystemExit"
        sys.exit(0)
        
    def render(self, dt):
        self.pantalla.fill(GRIS)
        
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
    