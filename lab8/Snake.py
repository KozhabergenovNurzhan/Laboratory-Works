import pygame, sys, random
from pygame.math import Vector2

# Snake class to handle movement, drawing, and updates
class SNAKE:
  def __init__(self):
    self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]  # Initial snake position
    self.direction = Vector2(0,0)  # No movement at start
    self.new_block = False  # Flag for growing the snake

    # Load snake images
    self.head_up = pygame.image.load('images_lab8/head_up.png').convert_alpha()
    self.head_down = pygame.image.load('images_lab8/head_down.png').convert_alpha()
    self.head_right = pygame.image.load('images_lab8/head_right.png').convert_alpha()
    self.head_left = pygame.image.load('images_lab8/head_left.png').convert_alpha()
    
    self.tail_up = pygame.image.load('images_lab8/tail_up.png').convert_alpha()
    self.tail_down = pygame.image.load('images_lab8/tail_down.png').convert_alpha()
    self.tail_right = pygame.image.load('images_lab8/tail_right.png').convert_alpha()
    self.tail_left = pygame.image.load('images_lab8/tail_left.png').convert_alpha()

    self.body_vertical = pygame.image.load('images_lab8/body_vertical.png').convert_alpha()
    self.body_horizontal = pygame.image.load('images_lab8/body_horizontal.png').convert_alpha()

    self.body_tr = pygame.image.load('images_lab8/body_tr.png').convert_alpha()
    self.body_tl = pygame.image.load('images_lab8/body_tl.png').convert_alpha()
    self.body_br = pygame.image.load('images_lab8/body_br.png').convert_alpha()
    self.body_bl = pygame.image.load('images_lab8/body_bl.png').convert_alpha()
    self.crunch_sound = pygame.mixer.Sound('audio_lab8/crunch.wav')

  def draw_snake(self):
    self.update_head_images()
    self.update_tail_images()

    for index, block in enumerate(self.body):
      x_pos = int(block.x * cell_size)
      y_pos = int(block.y * cell_size)
      block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

      if index == 0:
        screen.blit(self.head, block_rect)  # Draw head
      elif index == len(self.body) - 1:
        screen.blit(self.tail, block_rect)  # Draw tail
      else:
        previous_block = self.body[index + 1] - block
        next_block = self.body[index - 1] - block
        
        if previous_block.x == next_block.x:
          screen.blit(self.body_vertical, block_rect)
        elif previous_block.y == next_block.y:
          screen.blit(self.body_horizontal, block_rect)
        else:
          if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
            screen.blit(self.body_tl, block_rect)
          elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
            screen.blit(self.body_bl, block_rect)
          elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
            screen.blit(self.body_tr, block_rect)
          elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
            screen.blit(self.body_br, block_rect)

  def update_head_images(self):
    head_relation = self.body[1] - self.body[0]
    if head_relation == Vector2(1,0): self.head = self.head_left
    elif head_relation == Vector2(-1,0): self.head = self.head_right
    elif head_relation == Vector2(0,1): self.head = self.head_up
    elif head_relation == Vector2(0,-1): self.head = self.head_down

  def update_tail_images(self):
    tail_relation = self.body[-2] - self.body[-1]
    if tail_relation == Vector2(1,0): self.tail = self.tail_left
    elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
    elif tail_relation == Vector2(0,1): self.tail = self.tail_up
    elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

  def move_snake(self):
    if self.new_block:
      self.body.insert(0, self.body[0] + self.direction)
      self.new_block = False
    else:
      self.body.pop()
      self.body.insert(0, self.body[0] + self.direction)

  def add_block(self):
    self.new_block = True  # Enable snake growth

  def play_crunch_sound(self):
    self.crunch_sound.play()

  def reset(self):
    self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
    self.direction = Vector2(0,0)

# Fruit class to manage food placement
class FRUIT:
  def __init__(self):
    self.randomize()

  def draw_fruit(self):
    fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
    screen.blit(apple, fruit_rect)

  def randomize(self):
    self.pos = Vector2(random.randint(0, cell_number - 1), random.randint(0, cell_number - 1))

# Main game logic
class MAIN:
  def __init__(self):
    self.snake = SNAKE()
    self.fruit = FRUIT()
    self.score = 0
    self.level = 1
    self.move_delay = 280
    self.last_move_time = pygame.time.get_ticks()
    self.font = pygame.font.Font("font/PoetsenOne-Regular.ttf", 40)

  def update(self):
    if pygame.time.get_ticks() - self.last_move_time > self.move_delay:
      self.snake.move_snake()
      self.check_collision()
      self.check_fail()
      self.last_move_time = pygame.time.get_ticks()
  
  def draw_stats(self):
    self.snake = SNAKE()
    self.fruit = FRUIT()
    self.score = 0
    self.level = 1
    self.move_delay = 280
    self.last_move_time = pygame.time.get_ticks()
    self.font = pygame.font.Font("your_font.ttf", 40)  # Load custom font

  def draw_stats(self):
    apple_size = 40  # Resize if necessary
    apple_icon = pygame.transform.scale(apple, (apple_size, apple_size))  # Scale apple image

    # Positions
    apple_x = 10
    apple_y = screen.get_height() - apple_size - 10  # Bottom-left corner
    text_x = apple_x + apple_size + 10  # Place counter next to apple
    level_x = text_x + 100  # Position level further to the right

    # Render texts
    score_text = self.font.render(f"{self.score}", True, (0, 0, 0))
    level_text = self.font.render(f"Level: {self.level}", True, (0, 0, 0))

    # Draw on screen
    screen.blit(apple_icon, (apple_x, apple_y))  # Draw apple icon
    screen.blit(score_text, (text_x, apple_y))  # Draw apple counter
    screen.blit(level_text, (level_x, apple_y))  # Draw level info

  def check_collision(self):
    if self.fruit.pos == self.snake.body[0]:
      self.fruit.randomize()
      self.snake.add_block()
      self.snake.play_crunch_sound()
      self.score += 1
      if self.score % 3 == 0 and self.level < 6:
        self.level += 1
        self.move_delay = max(100, self.move_delay - 30)

  def check_fail(self):
    if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
      self.game_over()
    if self.snake.body[0] in self.snake.body[1:]:
      self.game_over()

  def game_over(self):
    self.snake.reset()
    self.score = 0
    self.level = 1
    self.move_delay = 160

# Initialize pygame
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
apple = pygame.image.load('images_lab8/apple.png').convert_alpha()
clock = pygame.time.Clock()

main_game = MAIN()
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP and main_game.snake.direction.y == 0:
        main_game.snake.direction = Vector2(0, -1)
      elif event.key == pygame.K_DOWN and main_game.snake.direction.y == 0:
          main_game.snake.direction = Vector2(0, 1)
      elif event.key == pygame.K_LEFT and main_game.snake.direction.x == 0:
        main_game.snake.direction = Vector2(-1, 0)
      elif event.key == pygame.K_RIGHT and main_game.snake.direction.x == 0:
        main_game.snake.direction = Vector2(1, 0)

  main_game.update()
  screen.fill((175,215,70))
  main_game.snake.draw_snake()
  main_game.fruit.draw_fruit()
  main_game.draw_stats()
  
  pygame.display.update()
  clock.tick(60)
