import pygame
import math
import pygame.gfxdraw

class Entity(pygame.sprite.Sprite):
    def __init__(self, Ox, Oy, Vx, Vy, Ax, Ay, mass, fixed):
        super().__init__()
        self.mass = mass
        self.image = 0
        self.rect = 0
        self.draw(Ox,Oy)

        #données rélles pour calculs car on donne que des donnés en pixels, on converti en m selon l'echelle
        self.x = Ox * 400000
        self.y = Oy * 400000
        self.Vx = Vx * 400000
        self.Vy = Vy * 400000
        self.Ax = Ax * 400000
        self.Ay = Ay * 400000
        #varibles locales de calucls
        self.d = 0
        self.Ax = 0
        self.angleC = 0
        self.angleS = 0

        #pour fixer la planete

        self.fixed = fixed

        self.w = 0
    
    def attract(self, EntToAttract): #entité qui influe sur l'accélération

        #calculs avec les données réelles
        self.d = math.sqrt( (EntToAttract.x-self.x)**2 + (EntToAttract.y-self.y)**2 )

        if not self.d == 0:
            
            self.A = (EntToAttract.mass * (6.67*(10**(-11))))/ self.d**2
            
            self.angleC = math.acos((EntToAttract.x-self.x)/self.d)
            self.angleS = math.asin((EntToAttract.y-self.y)/self.d)
            self.Ax = self.A * math.cos(self.angleC)
            self.Ay = self.A * math.sin(self.angleS)
    
    def move(self):

        if not self.fixed:
            self.Vx += self.Ax * 0.04
            self.Vy += self.Ay * 0.04

            self.x += self.Vx * 0.04
            self.y += self.Vy * 0.04

            self.rect.x = self.x / 400000 - self.w #le - self.w sert a recentrer l'entité apres les calculs
            self.rect.y = self.y / 400000 - self.w

            #on remet les accelérations a 0, elle reprendrons une certaines valeur si on doit en appliquer, sinon elles restent a 0 et la planetes continue sa route

            self.Ax = 0
            self.Ay = 0

    def draw(self, x, y):
        temp_mass = math.log(self.mass / 10000000)
        self.w = int(temp_mass/2)

        ENT_IMG = pygame.Surface((temp_mass, temp_mass ), pygame.SRCALPHA)
        pygame.gfxdraw.aacircle(ENT_IMG, self.w, self.w, self.w, (80, 80, 80))
        pygame.gfxdraw.filled_circle(ENT_IMG, self.w, self.w, self.w, (80, 80, 80))

        self.image = ENT_IMG

        self.rect = self.image.get_rect()

        self.rect.x = x - self.w  #le - self.w sert a recentrer l'entité apres les calculs
        self.rect.y = y - self.w