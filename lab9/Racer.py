import pygame, sys, random, time
from pygame.locals import *

class Game:
    def __init__(self):
        pygame.init()
        self.FPS = pygame.time.Clock()
        
        # Colors
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        
        # Screen
        self.WIDTH, self.HEIGHT = 400, 600
        self.DISPLAYSURF = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Racing Game")
        
        # Game state
        self.SPEED = 5
        self.SCORE = 0
        self.COINS_COLLECTED = 0
        self.N = 5  # Speed increase threshold
        
        # Fonts
        self.font = pygame.font.SysFont("Verdana", 60)
        self.font_small = pygame.font.SysFont("Verdana", 20)
        
        # Load assets
        self.background = pygame.image.load("C:/Users/Nurzhan/Laboratory-Works/imagesPygame/AnimatedStreet.png")
        self.crash_sound = pygame.mixer.Sound('C:/Users/Nurzhan/Laboratory-Works/audioPygame/crash.wav')
        
        # Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        
        # Create initial sprites
        self.P1 = Player(self)
        self.E1 = Enemy(self)
        self.C1 = Coin(self)
        
        self.all_sprites.add(self.P1, self.E1, self.C1)
        self.enemies.add(self.E1)
        self.coins.add(self.C1)
    
    def reset(self):
        """Reset game state"""
        self.SPEED = 5
        self.SCORE = 0
        self.COINS_COLLECTED = 0
        
        # Clear all sprites
        for sprite in self.all_sprites:
            sprite.kill()
        
        # Create new sprites
        self.P1 = Player(self)
        self.E1 = Enemy(self)
        self.C1 = Coin(self)
        
        self.all_sprites.add(self.P1, self.E1, self.C1)
        self.enemies.add(self.E1)
        self.coins.add(self.C1)
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Game logic
            self.DISPLAYSURF.blit(self.background, (0, 0))
            
            # Update and draw all sprites
            for entity in self.all_sprites:
                entity.move()
                self.DISPLAYSURF.blit(entity.image, entity.rect)
            
            # Display scores
            scores = self.font_small.render(str(self.SCORE), True, self.BLACK)
            coins_display = self.font_small.render(f"Coins: {self.COINS_COLLECTED}", True, self.BLACK)
            self.DISPLAYSURF.blit(scores, (10, 10))
            self.DISPLAYSURF.blit(coins_display, (self.WIDTH - 100, 10))
            
            # Check collisions
            if pygame.sprite.spritecollideany(self.P1, self.enemies):
                self.game_over()
            
            collected_coin = pygame.sprite.spritecollideany(self.P1, self.coins)
            if collected_coin:
                self.COINS_COLLECTED += collected_coin.value
                collected_coin.respawn()
                
                # Increase speed every N coins (without infinite loop)
                if (self.COINS_COLLECTED - collected_coin.value) // self.N < self.COINS_COLLECTED // self.N:
                    self.SPEED += 0.5
            
            pygame.display.update()
            self.FPS.tick(60)
    
    def game_over(self):
        self.crash_sound.play()
        self.DISPLAYSURF.fill(self.RED)
        game_over_text = self.font.render("Game Over", True, self.BLACK)
        restart_text = self.font_small.render("Press R to restart", True, self.WHITE)
        
        self.DISPLAYSURF.blit(game_over_text, (30, 250))
        self.DISPLAYSURF.blit(restart_text, (120, 350))
        pygame.display.update()
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        waiting = False
                        self.reset()
                    elif event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            self.FPS.tick(60)

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load("C:/Users/Nurzhan/Laboratory-Works/imagesPygame/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < self.game.WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load("C:/Users/Nurzhan/Laboratory-Works/imagesPygame/Enemy.png")
        self.rect = self.image.get_rect()
        self.respawn()
    
    def move(self):
        self.rect.move_ip(0, self.game.SPEED)
        if self.rect.bottom > self.game.HEIGHT:
            self.game.SCORE += 1
            self.respawn()
    
    def respawn(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40, self.game.WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.respawn()
    
    def respawn(self):
        if random.random() < 0.4:
            self.image = pygame.image.load("C:/Users/Nurzhan/Laboratory-Works/imagesPygame/Emerald.png")
            self.value = 3
        else:
            self.image = pygame.image.load("C:/Users/Nurzhan/Laboratory-Works/imagesPygame/Coin.png")
            self.value = 1
        
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, self.game.WIDTH - 40), random.randint(50, self.game.HEIGHT // 2))
    
    def move(self):
        self.rect.move_ip(0, self.game.SPEED)
        if self.rect.top > self.game.HEIGHT:
            self.respawn()

if __name__ == "__main__":
    game = Game()
    game.run()