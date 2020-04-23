import pygame
from simulation import *
from entity import *

pygame.display.set_caption("Test Physique")
screen = pygame.display.set_mode((1280,720)) #renvoie une surface, on la recupere dans screen

background = pygame.image.load("ressources/bg.png")

simu = Simulation()
originX, originY = screen.get_width()/2,screen.get_height()/2

#définission des différentes planètes
sun = Entity(originX, originY, 0, -1, 0, 0, 2*10**30)
earth = Entity(originX + 149597870/400000, originY + 125,1,-1,0,0, 2*10**29)

simu.all_ent.add(sun)
simu.all_ent.add(earth)

clock = pygame.time.Clock()
FPS = 120

running = True

while running:
    clock.tick(FPS)
    screen.blit(background, (0,0))

    simu.all_ent.draw(screen)

    pygame.display.flip()

    for ent in simu.all_ent:
        for EntAttract in simu.all_ent:
            if EntAttract != ent:
                ent.move(EntAttract)

    for event in pygame.event.get():
        #si on quite
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("au revoir !")