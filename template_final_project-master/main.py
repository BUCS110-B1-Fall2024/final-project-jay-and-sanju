import pygame
import sys
import os

from controller import Controller

def main():
    pygame.init()
    game_controller = Controller()
    game_controller.mainloop()

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
