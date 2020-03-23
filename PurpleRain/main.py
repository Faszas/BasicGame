import pygame
import random

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
time = pygame.time.Clock()
pygame.display.set_caption("Purple Rain")



randomColors = [(230,230,250), (216,191,216), (221,160,221), (238,130,238), (218,112,214), (255,0,255), (255,0,255), (138,43,226)]

class RAIN:

    
    def __init__(self, x, y, speedx, speedy):
        self.x = x
        self.y = y
        self.speedx = speedx
        self.speedy = speedy
        self.width = 10
        self.height = 2
        self.color = (129, 0, 128)
        
    def display(self):
        global randomColors
        self.color = random.choice(randomColors)
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        self.x += self.speedx
        self.y += self.speedy
        
        if self.x > width or self.y > height:
            self.x = random.randrange(0, width - 10)
            self.y = random.randrange(0, height - 10)
        
      
    

rains = [RAIN(random.randrange(0, width - 10), random.randrange(0, height - 10), 20, 10) for i in range(500)]


def display():
    for i in rains:
        i.display()
    pygame.display.update()
    
def main():
    
    while True:
        time.tick(30)
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        display()
main()
