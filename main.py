import pygame
from simulation import *
from entity import *
from control import *

pygame.display.set_caption("Test Physique")
screen = pygame.display.set_mode((1280,720)) #renvoie une surface, on la recupere dans screen

background = pygame.image.load("ressources/bg.png")

simu = Simulation()
originX, originY = screen.get_width()/2,screen.get_height()/2

#définission des différentes planètes
sun = Entity(originX, originY, 0, 0, 0, 0, 2*10**30)
earth = Entity(originX + 149597870/400000, originY + 125,1,-1,0,0, 2*10**20)

simu.all_ent.add(sun)
simu.all_ent.add(earth)

clock = pygame.time.Clock()
FPS = 60

running = True

while running:
    clock.tick(FPS)
    screen.blit(background, (0,0))

    simu.all_ent.draw(screen)

    pygame.display.flip()

    for ent in simu.all_ent:
        ent.move()

        #appliquer l'attraction
        for ent2 in simu.all_ent:
            if not ent2 is ent:
                ent.attract(ent2)
                
            #si il ya des collisions, on fusionne
            if collidable(ent, ent2):
                ent.mass += ent2.mass
                ent.draw()
                simu.all_ent.remove(ent2)
                continue

    for event in pygame.event.get():
        #si on quite
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("au revoir !")