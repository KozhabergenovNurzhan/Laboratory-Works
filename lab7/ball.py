import pygame

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BALL_RADIUS = 25
STEP = 5  

x, y = WIDTH // 2, HEIGHT // 2  

clock = pygame.time.Clock()
run = True
while run:
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), BALL_RADIUS)
    pygame.display.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y - BALL_RADIUS - STEP >= 0:
        y -= STEP
    if keys[pygame.K_DOWN] and y + BALL_RADIUS + STEP <= HEIGHT:
        y += STEP
    if keys[pygame.K_LEFT] and x - BALL_RADIUS - STEP >= 0:
        x -= STEP
    if keys[pygame.K_RIGHT] and x + BALL_RADIUS + STEP <= WIDTH:
        x += STEP

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(60)  

pygame.quit()
