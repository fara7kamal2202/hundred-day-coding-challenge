import os
import pygame
pygame.font.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Invaders')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH = 40
SPACESHIP_HEIGHT = 55

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(YELLOW_SPACESHIP_IMAGE, 90)
YELLOW_SPACESHIP_IMAGE = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP_IMAGE = pygame.transform.rotate(RED_SPACESHIP_IMAGE, 270)
RED_SPACESHIP_IMAGE = pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

HEALTH_FONT = pygame.font.SysFont('comicsans', 30)

SPACE = pygame.image.load(os.path.join("Assets", "space.png"))
SPACE = pygame.transform.scale(SPACE, (WIDTH, HEIGHT))

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    red_health_text = HEALTH_FONT.render(f"Health: {red_health}", 1, WHITE)
    yellow_health_text = HEALTH_FONT.render(f"Health: {yellow_health}", 1, WHITE)

    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))

    WIN.blit(YELLOW_SPACESHIP_IMAGE, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP_IMAGE, (red.x, red.y))
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    pygame.display.update()

def move_left(item):
    if item.x - VEL > 0:
        item.x -= VEL

def move_right(item):
    if item.x + VEL + SPACESHIP_WIDTH < WIDTH:
        item.x += VEL


def move_up(item):
    if item.y - VEL > 0:
        item.y -= VEL


def move_down(item):
    if item.y + VEL + SPACESHIP_HEIGHT < HEIGHT:
        item.y += VEL

def handle_yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a]:
        move_left(yellow)
    if keys_pressed[pygame.K_d]:
        if yellow.x + VEL + SPACESHIP_WIDTH < BORDER.x:
            move_right(yellow)
    if keys_pressed[pygame.K_w]:
        move_up(yellow)
    if keys_pressed[pygame.K_s]:
        move_down(yellow)

def handle_red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]:
        if red.x - VEL > BORDER.x:
            move_left(red)
    if keys_pressed[pygame.K_RIGHT]:
        move_right(red)
    if keys_pressed[pygame.K_UP]:
        move_up(red)
    if keys_pressed[pygame.K_DOWN]:
        move_down(red)

def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x >= WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x <= 0:
            red_bullets.remove(bullet)

def draw_winner(text):
    draw_text = HEALTH_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, ((WIDTH - draw_text.get_width())/2, (HEIGHT - draw_text.get_height())/2))
    pygame.display.update()
    pygame.time.wait(5000)

def  main():
    yellow_bullets = []
    red_bullets = []
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    yellow_health = 10
    red_health = 10

    winner_text = ""
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)


            if event.type == RED_HIT:
                red_health -= 1
                if red_health == 0:
                    winner_text = "YELLOW WINS"

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                if yellow_health == 0:
                    winner_text = "RED WINS"

        keys_pressed = pygame.key.get_pressed()
        handle_yellow_movement(keys_pressed, yellow)
        handle_red_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
        if winner_text != "":
            draw_winner(winner_text)
            break


    pygame.quit()



if __name__ == "__main__":
    main()
