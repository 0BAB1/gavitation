import pygame
from entity import *

def collidable(one, two):
    if one is two:
        return False
    else:
        return one.rect.colliderect(two.rect)

class Simulation():
    def __init__(self):
        self.all_ent = pygame.sprite.Group()