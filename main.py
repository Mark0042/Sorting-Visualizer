import pygame
import math
import random
import time
from pygame import mixer

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

a=[5,3,7,9,8,4,14,7,12,20,24,21,6,19,8,23,22,12,11,10]
mx=0
for i in a:
    if i>mx:
        mx=i
n=len(a)
wid=800/n
ht=600/mx-1
pygame.display.set_caption("Bubble Sort")

running= True
def checkquit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def draw(x):
    screen.fill((0, 0, 0))
    for k in range(n):
        if k>x:
            pygame.draw.rect (screen, (0,255,0),[k*wid,(600-(a[k]*ht)),wid-1,a[k]*ht])
        else:
            pygame.draw.rect (screen, (255,255,255),[k*wid,(600-(a[k]*ht)),wid-1,a[k]*ht])

    pygame.display.update()
while running:

    for i in range(n):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
#                 beepsound=mixer.Sound("beep-07.wav")
#                 beepsound.play()
            draw(n-i-1)

            time.sleep(0.01)
    draw(0)
    draw(-1)
    running=False
    time.sleep(0.1)


