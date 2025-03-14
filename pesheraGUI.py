import pygame
import tkinter as tk
from tkinter import messagebox

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Пещера')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
background = pygame.image.load('')
character_image = pygame.image.load('')
character_rect = character_image.get_rect(center = WIDTH//2, HEIGHT//2)

class Game:
    def __init__(self):
        self.running = True
        self.score = 0
        self.level = 1
        self.health = 100

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            #screen.fill((0, 0, 0))
            #pygame.display.flip()
            self.update_game_state()
            self.draw()
            pygame.time.delay(100)
        pygame.quit()

    def update_game_state(self):
        self.score += 1
        if self.score % 100 == 0:
            self.level += 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LIFT]:
            character_rect.x -= 5
        if keys[pygame.K_RIGHT]:
            character_rect.x += 5
        if keys[pygame.K_UP]:
            character_rect.y -= 5
        if keys[pygame.K_DOWN]:
            character_rect.y += 5

    def draw(self):
        screen.fill(background, (0,0))
        screen.blit(character_image, character_rect())
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'очки: {self.score}, True, WHITE')
        level_text = font.render(f'уровень: {self.level}, True, WHITE')
        health_text = font.render(f'здоровье: {self.health}, True, WHITE')
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 50))
        screen.blit(health_text, (10, 90))
        pygame.display.flip()

def start_game():
    root.windraw()
    game = Game()
    game.run()
    root.quit()

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Пещера')
    start_button = tk.Button(root, text = 'начать исследование', command = start_game)
    start_button.pack(pady = 20)