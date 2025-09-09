import pygame
from constants import *
from player import Player

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

game_clock = pygame.time.Clock()
dt = 0

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        dt = (game_clock.tick(60) / 1000)


if __name__ == "__main__":
    main()
