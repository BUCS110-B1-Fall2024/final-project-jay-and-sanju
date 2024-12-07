import pygame
import random
from christmas import Santa, Grinch, Present

class Controller:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Santa's Christmas Adventure")

        self.running = False  # Main game loop state
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)
        self.score = 0

        self.initialize_game_objects()

    def initialize_game_objects(self):
        self.santa = Santa("assets/santa.png", 100, 100, 5)

        self.grinches = [
            Grinch("assets/grinch.png", 200, 200, 2, 2),
            Grinch("assets/grinch.png", 300, 300, -3, 1),
            Grinch("assets/grinch.png", 500, 200, 2, -1),
            Grinch("assets/grinch.png", 600, 400, -2, 3)
        ]
        
        self.presents = [
            Present("assets/present.png", random.randint(50, 750), random.randint(50, 550)),
            Present("assets/present.png", random.randint(50, 750), random.randint(50, 550)),
            Present("assets/present.png", random.randint(50, 750), random.randint(50, 550)),
            Present("assets/present.png", random.randint(50, 750), random.randint(50, 550)),
            Present("assets/present.png", random.randint(50, 750), random.randint(50, 550)),
        ]
        
        self.score = 0

    def handle_events(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.santa.move("UP")
        if keys[pygame.K_DOWN]:
            self.santa.move("DOWN")
        if keys[pygame.K_LEFT]:
            self.santa.move("LEFT")
        if keys[pygame.K_RIGHT]:
            self.santa.move("RIGHT")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def detect_collisions(self):
        for present in self.presents:
            if self.santa.rect.colliderect(present.rect):
                self.score += 1
                present.update_position(random.randint(50, 750), random.randint(50, 550))

        for grinch in self.grinches:
            if self.santa.rect.colliderect(grinch.rect):
                self.running = False

    def update(self):
        for grinch in self.grinches:
            grinch.update_position(grinch.x + grinch.dx, grinch.y + grinch.dy)
            if grinch.x <= 0 or grinch.x + grinch.rect.width >= 800:
                grinch.dx = -grinch.dx
            if grinch.y <= 0 or grinch.y + grinch.rect.height >= 600:
                grinch.dy = -grinch.dy

    def redraw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.santa.image, (self.santa.x, self.santa.y))
        for grinch in self.grinches:
            self.screen.blit(grinch.image, (grinch.x, grinch.y))
        for present in self.presents:
            self.screen.blit(present.image, (present.x, present.y))

        score_text = self.font.render(f"Presents: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

    def display_message(self, message, sub_message=None):
        self.screen.fill((0, 0, 0))
        text = self.font.render(message, True, (255, 255, 255))
        text_rect = text.get_rect(center=(400, 250))
        self.screen.blit(text, text_rect)

        if sub_message:
            sub_text = self.font.render(sub_message, True, (200, 200, 200))
            sub_text_rect = sub_text.get_rect(center=(400, 300))
            self.screen.blit(sub_text, sub_text_rect)

        pygame.display.flip()

    def start_screen(self):
        self.display_message("Santa's Christmas Adventure", "Press SPACE to Start")
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    waiting = False

    def game_over_screen(self):
        self.display_message("Game Over", f"Score: {self.score}. Press R to Restart or Q to Quit.")
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.initialize_game_objects()  # Reset game state
                        waiting = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        exit()

    def mainloop(self):
        self.start_screen()

        self.running = True
        while self.running:
            self.handle_events()
            self.detect_collisions()
            self.update()
            self.redraw()
            pygame.display.flip()
            self.clock.tick(60)

        self.game_over_screen()
        self.mainloop()
