import pygame
import math
import pygame.gfxdraw

class Entity(pygame.sprite.Sprite):
    def __init__(self, Ox, Oy, Vx, Vy, Ax, Ay, mass):
        super().__init__()
        self.mass = mass
        self.image = 0
        self.draw()
        self.rect = self.image.get_rect()

        #données affichage
        self.rect.x = Ox
        self.rect.y = Oy

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
    
    def attract(self, EntToAttract): #entité qui influe sur l'accélération

        #calculs avec les données réelles
        self.d = math.sqrt( (EntToAttract.x-self.x)**2 + (EntToAttract.y-self.y)**2 )
        
        self.A = (EntToAttract.mass * (6.67*(10**(-11))))/ self.d**2
        
        self.angleC = math.acos((EntToAttract.x-self.x)/self.d)
        self.angleS = math.asin((EntToAttract.y-self.y)/self.d)
        self.Ax = self.A * math.cos(self.angleC)
        self.Ay = self.A * math.sin(self.angleS)

        #on adapte les vraies données

        self.rect.x = self.x / 400000
        self.rect.y = (self.y) / 400000
    
    def move(self):
        self.Vx += self.Ax * 0.4
        self.Vy += self.Ay * 0.4

        self.x += self.Vx * 0.4
        self.y += self.Vy * 0.4

        self.rect.x = self.x / 400000
        self.rect.y = (self.y) / 400000

        #on remet les accelérations a 0, elle reprendrons une certaines valeur si on doit en appliquer, sinon elles restent a 0 et la planetes continue sa route

        self.Ax = 0
        self.Ay = 0

    def draw(self):
        temp_mass = math.log(self.mass / 1000000)
        w = int(temp_mass/2)

        ENT_IMG = pygame.Surface((temp_mass, temp_mass), pygame.SRCALPHA)
        pygame.gfxdraw.aacircle(ENT_IMG, w, w, w, (80, 80, 80))
        pygame.gfxdraw.filled_circle(ENT_IMG, w, w, w, (80, 80, 80))

        self.image = ENT_IMG