import pygame
from simulation import *

class Control(object):
    def __init__(self):
        pygame.init()
        self.background = pygame.image.load("ressources/bg.png")
        self.screen = pygame.display.set_mode((1280,720))
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.running = False
        self.fps = 60.0
        self.simu = Simulation()

        self.originX, self.originY = self.screen.get_width()/2,self.screen.get_height()/2

        self.make_planets()
 
    def make_planets(self):
        sun = Entity(self.originX, self.originY, 0, 0, 0, 0, 2*10**30)
        earth = Entity(self.originX + 149597870/400000, self.originY + 125,1,-1,0,0, 2*10**20)

        self.simu.all_ent.add(sun)
        self.simu.all_ent.add(earth)

        print(self.simu.all_ent)
 
    def event_loop(self):
        for event in pygame.event.get():
            #si on quite
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                print("au revoir !")
 
    def main_loop(self):

        while not self.running:
            self.event_loop()
            self.clock.tick(self.fps)
            self.screen.blit(self.background, (0,0))

            self.simu.all_ent.draw(self.screen)

            for ent in self.simu.all_ent:
                ent.move()

                #appliquer l'attraction
                for ent2 in self.simu.all_ent:
                    if not ent2 is ent:
                        ent.attract(ent2)
                        
                    #si il ya des collisions, on fusionne
                    if collidable(ent, ent2):
                        ent.mass += ent2.mass
                        ent.draw()
                        self.simu.all_ent.remove(ent2)
                        continue

            pygame.display.update()