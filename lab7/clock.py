import pygame
import time

pygame.init()

background = pygame.image.load("images/MickeyClock.png")
right_hand = pygame.image.load("images/righthand.png")
left_hand = pygame.image.load("images/lefthand.png")

WIDTH, HEIGHT = background.get_size()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

center_x, center_y = WIDTH // 2, HEIGHT // 2

def rotate_hand(image, angle, offset_x, offset_y):
  rotated_image = pygame.transform.rotate(image, angle)
  new_rect = rotated_image.get_rect(center=(center_x + offset_x, center_y + offset_y))
  
  return rotated_image, new_rect.topleft

clock = pygame.time.Clock()
run = True
while run:
  screen.blit(background, (0, 0))

  current_time = time.localtime()
  minutes = current_time.tm_min
  seconds = current_time.tm_sec

  min_angle = -minutes * 6
  sec_angle = -seconds * 6

  rotated_min_hand, min_pos = rotate_hand(right_hand, min_angle, 0, 0)
  rotated_sec_hand, sec_pos = rotate_hand(left_hand, sec_angle, 0, 0)

  screen.blit(rotated_min_hand, min_pos)
  screen.blit(rotated_sec_hand, sec_pos)

  pygame.display.update()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  clock.tick(1)
pygame.quit()
