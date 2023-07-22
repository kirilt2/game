import pygame
import random

# Initialize Pygame
pygame.init()

# Constants for the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(SCREEN_HEIGHT - self.rect.height)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Kill the Ballsgffgfgfg")

# Create a sprite group for the balls
all_sprites = pygame.sprite.Group()

# Create balls and add them to the sprite group
for _ in range(10):
    ball = Ball()
    all_sprites.add(ball)

# Main menu loop
def main_menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False

        screen.fill(WHITE)
        font = pygame.font.Font(None, 36)
        text = font.render("Press SPACE to start", True, RED)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()

# Main game loop
def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(WHITE)

        # Update and draw the balls
        all_sprites.update()
        all_sprites.draw(screen)

        # Check for collisions with the mouse click
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            clicked_sprites = [s for s in all_sprites if s.rect.collidepoint(pos)]
            for sprite in clicked_sprites:
                sprite.kill()

        # Update the display
        pygame.display.flip()

# Run the main menu and game loop
main_menu()
game_loop()

# Quit the game
pygame.quit()
