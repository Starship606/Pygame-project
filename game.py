import pygame
import sys

pygame.init()

window_size = (1200, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Dragon eat F-22 Warplanes")
background = pygame.image.load(r"C:\Users\Acer\Downloads\sky.png")
quitt=False
blue = (0, 0, 255)
a=5000

class F_22(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Acer\Downloads\F22-removebg-preview.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Dragon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Acer\Downloads\dragon-removebg-preview.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

Soldier = F_22(800, 100)
Soldier1 = F_22(800, 300)
dragon = Dragon(100, 150)
human = pygame.sprite.Group()
human.add(Soldier, Soldier1)
Dragons = pygame.sprite.Group()
Dragons.add(dragon)
F_22_ate = 0
while True:
    current_time=pygame.time.get_ticks()
    window.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

   
    if keys[pygame.K_a]:
        dragon.rect.x -= 1 
    if keys[pygame.K_d]:
        dragon.rect.x += 1
    if keys[pygame.K_w]:
        dragon.rect.y -= 1
    if keys[pygame.K_s]:
        dragon.rect.y += 1

    if pygame.sprite.spritecollide(dragon, human,True):
        F_22_ate+=1
    if F_22_ate == 2:
        start_time=pygame.time.get_ticks()
        quitt=True
        F_22_ate=0
    if quitt:
        text = (pygame.font.Font(None, 50)).render("Dragon ate 2 Warplanes!,Dragon Win!",False,(255,0,0))
        window.blit(text,(300,50))
        result=current_time-start_time
   
        if current_time-start_time>=a:
            pygame.quit()
            sys.exit()
        
        

    human.update()
    Dragons.update()
    human.draw(window)
    Dragons.draw(window)

    pygame.display.flip()
