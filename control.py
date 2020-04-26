import pygame
from simulation import *

class Control(object):
    def __init__(self):
        pygame.init()
        self.background = pygame.image.load("ressources/bg.png")
        self.screen = pygame.display.set_mode((1280,720))
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = 60.0
        self.simu = Simulation()

        self.originX, self.originY = self.screen.get_width()/2,self.screen.get_height()/2

        self.make_planets()
 
    def make_planets(self):
        #sun = Entity(self.originX, self.originY, 0, 0, 0, 0, 2*10**30)
        earth = Entity(self.originX + 149597870/400000, self.originY + 125,0,-5,0,0, 6*10**26,False)

        #self.simu.all_ent.add(sun)
        self.simu.all_ent.add(earth)

        print(self.simu.all_ent)
 
    def event_loop(self):
        for event in pygame.event.get():
            #si on quite
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                print("au revoir !")

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                self.simu.all_ent.add(Entity(x,y,0,0,0,0,2*10**31,False))
 
    def main_loop(self):

        while self.running:

            for ent in self.simu.all_ent:

                for ent2 in self.simu.all_ent:
                    ent.attract(ent2)
                    ent.move()

            self.event_loop()
            self.clock.tick(self.fps)
            self.screen.blit(self.background, (0,0))

            self.simu.all_ent.draw(self.screen)

            pygame.display.update()