import pygame
from entity import *

class Simulation():
    def __init__(self):
        self.all_ent = pygame.sprite.Group()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, True, pygame.sprite.collide_mask)