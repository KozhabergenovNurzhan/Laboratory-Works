import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Color palette
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), BLACK]
selected_color = BLACK

# Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Paint Program")
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

# Brush settings
drawing = False
mode = "pencil"  # Modes: 'pencil', 'rectangle', 'circle', 'eraser'
eraser_size = 20
brush_size = 5
rect_border = 3
circle_radius = 10
start_pos = None

# Main loop
while True:
  screen.fill(WHITE)
  screen.blit(canvas, (0, 0))
  
  # Draw color palette
  for i, color in enumerate(colors):
    pygame.draw.rect(screen, color, (10 + i * 40, 10, 30, 30))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:  # Left mouse button
        x, y = event.pos
        
        # Check if user clicked on color palette
        for i, color in enumerate(colors):
          if 10 + i * 40 <= x <= 40 + i * 40 and 10 <= y <= 40:
            selected_color = color
            break
        else:
          drawing = True
          start_pos = event.pos

    if event.type == pygame.MOUSEBUTTONUP:
      if event.button == 1:
        drawing = False
        start_pos = None
    
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_p:
        mode = "pencil"
      elif event.key == pygame.K_r:
        mode = "rectangle"
      elif event.key == pygame.K_c:
        mode = "circle"
      elif event.key == pygame.K_e:
        mode = "eraser"
      elif event.key == pygame.K_EQUALS or event.key == pygame.K_PLUS:
        if mode == "pencil":
          brush_size = min(50, brush_size + 2)
        elif mode == "rectangle":
          rect_border = min(20, rect_border + 1)
        elif mode == "circle":
          circle_radius = min(100, circle_radius + 5)
        elif mode == "eraser":
          eraser_size = min(100, eraser_size + 5)
      elif event.key == pygame.K_MINUS:
        if mode == "pencil":
          brush_size = max(1, brush_size - 2)
        elif mode == "rectangle":
          rect_border = max(1, rect_border - 1)
        elif mode == "circle":
          circle_radius = max(5, circle_radius - 5)
        elif mode == "eraser":
          eraser_size = max(5, eraser_size - 5)

  if drawing and pygame.mouse.get_pressed()[0]:
    x, y = pygame.mouse.get_pos() 
    
    if mode == "pencil":
      pygame.draw.circle(canvas, selected_color, (x, y), brush_size)
    
    elif mode == "rectangle" and start_pos:
      pygame.draw.rect(canvas, selected_color, (*start_pos, x - start_pos[0], y - start_pos[1]), rect_border)
    
    elif mode == "circle" and start_pos:
      radius = int(((x - start_pos[0]) ** 2 + (y - start_pos[1]) ** 2) ** 0.5)
      pygame.draw.circle(canvas, selected_color, start_pos, radius, 2)
    
    elif mode == "eraser":
      pygame.draw.circle(canvas, WHITE, (x, y), eraser_size)
      
  if mode == "eraser" and pygame.mouse.get_focused():
    pygame.draw.circle(screen, (200, 200, 200), pygame.mouse.get_pos(), eraser_size, 1)
  
  pygame.display.flip()