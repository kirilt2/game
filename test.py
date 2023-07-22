import pygame
import sys
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
FPS = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Snake directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Create the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Duck Snake")
clock = pygame.time.Clock()

# Load resources
duck_image = pygame.image.load("duck.png").convert_alpha()
apple_image = pygame.image.load("apple.png").convert_alpha()
duck_image = pygame.transform.scale(duck_image, (GRID_SIZE, GRID_SIZE))
apple_image = pygame.transform.scale(apple_image, (GRID_SIZE, GRID_SIZE))

# Load sounds
quack_sound = pygame.mixer.Sound("duckeat.mp3")
quack_sound.set_volume(0.5)

# Global variables
money = 0
skin_unlocked = [True, False]  # List to keep track of which skins are unlocked

def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(window, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(window, WHITE, (0, y), (WIDTH, y))

class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.grow = False

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = ((head_x + dx) % GRID_WIDTH, (head_y + dy) % GRID_HEIGHT)
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def change_direction(self, new_direction):
        if new_direction[0] != -self.direction[0] or new_direction[1] != -self.direction[1]:
            self.direction = new_direction

    def check_collision(self):
        return len(set(self.body)) < len(self.body)

    def check_apple_collision(self, apple_pos):
        return self.body[0] == apple_pos

    def grow_snake(self):
        self.grow = True

    def draw(self):
        for segment in self.body:
            x, y = segment
            window.blit(duck_image, (x * GRID_SIZE, y * GRID_SIZE))

class Apple:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        return (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def draw(self):
        x, y = self.position
        window.blit(apple_image, (x * GRID_SIZE, y * GRID_SIZE))

def draw_main_menu():
    window.fill(BLACK)
    font = pygame.font.Font(None, 36)
    title_text = font.render("Duck Snake", True, WHITE)
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    window.blit(title_text, title_rect)

    play_text = font.render("Play", True, WHITE)
    play_rect = play_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(play_text, play_rect)

    shop_text = font.render("Shop", True, WHITE)
    shop_rect = shop_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    window.blit(shop_text, shop_rect)

    pygame.display.flip()

def draw_shop_menu():
    window.fill(BLACK)
    font = pygame.font.Font(None, 36)
    title_text = font.render("Shop", True, WHITE)
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    window.blit(title_text, title_rect)

    skin1_text = font.render("Skin 1 (100 Money)", True, WHITE)
    skin1_rect = skin1_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    window.blit(skin1_text, skin1_rect)

    skin2_text = font.render("Skin 2 (500 Money)", True, WHITE)
    skin2_rect = skin2_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    window.blit(skin2_text, skin2_rect)

    back_text = font.render("Back", True, WHITE)
    back_rect = back_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    window.blit(back_text, back_rect)

    pygame.display.flip()

def buy_skin(skin_number):
    global money, skin_unlocked
    if skin_number == 1 and money >= 100:
        money -= 100
        skin_unlocked[1] = True
    elif skin_number == 2 and money >= 500:
        money -= 500
        skin_unlocked[2] = True

def game_loop():
    snake = Snake()
    apple = Apple()
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(RIGHT)

        snake.move()

        if snake.check_collision():
            # Game over
            font = pygame.font.Font(None, 36)
            game_over_text = font.render("Game Over", True, WHITE)
            game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            window.fill(BLACK)
            window.blit(game_over_text, game_over_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            return

        if snake.check_apple_collision(apple.position):
            apple.position = apple.random_position()
            snake.grow_snake()
            score += 1

        window.fill(BLACK)
        draw_grid()
        snake.draw()
        apple.draw()

        font = pygame.font.Font(None, 24)
        score_text = font.render("Score: " + str(score), True, WHITE)
        window.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

def main():
    global money, skin_unlocked
    draw_main_menu()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:  # Press 'p' to play the game
            draw_grid()
            game_loop()
            draw_main_menu()
        elif keys[pygame.K_s]:  # Press 's' to access the shop
            draw_shop_menu()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit()
                            sys.exit()
                        elif event.key == pygame.K_b:  # Press 'b' to go back to main menu
                            draw_main_menu()
                            break
                        elif event.key == pygame.K_1:  # Press '1' to buy skin 1
                            buy_skin(1)
                            draw_shop_menu()
                        elif event.key == pygame.K_2:  # Press '2' to buy skin 2
                            buy_skin(2)
                            draw_shop_menu()

        pygame.display.flip()
        clock.tick(FPS)

# Start the game
if __name__ == "__main__":
    main()



