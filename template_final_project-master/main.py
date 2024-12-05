import pygame
import sys
import os

from controller import Controller

def main():
    pygame.init()
    # Create an instance of your controller object
    game_controller = Controller()
    # Call your mainloop
    game_controller.mainloop()

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
