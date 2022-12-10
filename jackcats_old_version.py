#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))

rect(screen, (245, 245, 245), (0, 0, 800, 360))
rect(screen, (210, 210, 210), (0, 360, 800, 800-360))
rect(screen, (132, 112, 255), (500,50,270,270))
rect(screen, (190,190,190), (500,50,270,20))
rect(screen, (190,190,190), (500,50,20,270))
rect(screen, (190,190,190), (500,270+50,290,20))
rect(screen, (190,190,190), (500+270,50,20,270))
rect(screen, (190,190,190), (500+270/2,50,20,270))
rect(screen, (190,190,190), (500+270/2,50+270/2,270/2,20))

rect(screen, (132, 112, 255), (200,50,270,270))
rect(screen, (190,190,190), (200,50,270,20))
rect(screen, (190,190,190), (200,50,20,270))
rect(screen, (190,190,190), (200,270+50,290,20))
rect(screen, (190,190,190), (200+270,50,20,270))
rect(screen, (190,190,190), (200+270/2,50,20,270))
rect(screen, (190,190,190), (200+270/2,50+270/2,270/2,20))

rect(screen, (132, 112, 255), (-100,50,270,270))
rect(screen, (190,190,190), (-100,50,270,20))
rect(screen, (190,190,190), (-100,50,20,270))
rect(screen, (190,190,190), (-100,270+50,290,20))
rect(screen, (190,190,190), (-100+270,50,20,270))
rect(screen, (190,190,190), (-100+270/2,50,20,270))
rect(screen, (190,190,190), (-100+270/2,50+270/2,270/2,20))

# Рисуем жеккота!
def draw_ellipse_angle(surface, color, rect, angle, width=0):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size))
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.center))
def draw_ellipse_angle1(surface, color, rect, angle, width=0):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size),1)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.center))
pi = 3.14

def cat(color,color_eye,x,y,r):
    
    draw_ellipse_angle(screen, color, (x+4.5*r,y-1.7*r,1.2*r,3.5*r), 65, 2)
    draw_ellipse_angle1(screen, (0, 0, 0), (x+4.5*r,y-1.7*r,1.2*r,3.5*r), 65, 2)
    ellipse(screen,color,(x,y-1.2*1*r,5*r,1.2*2*r))
    ellipse(screen,(0,0,0),(x,y-1.2*1*r,5*r,1.2*2*r),1)
    ellipse(screen,color,(x-5*r/6,y+r/6,2.5*r/3,1.2*r))
    ellipse(screen,(0, 0, 0),(x-5*r/6,y+r/6,2.5*r/3,1.2*r),1)
    ellipse(screen,color,(x+2*r/6,y+0.8*r,1.5*r,2*r/3))
    ellipse(screen,(0, 0, 0),(x+2*r/6,y+0.8*r,1.5*r,2*r/3),1)
    circle(screen, color, (x+4*r,y+0.7*r), 0.65*r)
    circle(screen, (0, 0, 0), (x+4*r,y+0.7*r), 0.65*r,1)
    ellipse(screen,color,(x+4*r+0.45*r,y+0.7*r+0.1*r,0.4*r,1.1*r))
    ellipse(screen,(0, 0, 0),(x+4*r+0.45*r,y+0.7*r+0.1*r,0.4*r,1.1*r),1)

    ellipse(screen,color,(x-1.05*r,y-1.05*r,2*r*1.15,2*r))
    ellipse(screen,(0,0,0),(x-1.05*r,y-1.05*r,2*r*1.15,2*r),1)
    pygame.draw.polygon(screen,color,[[x+5*r*1.15/15, y-14*r/15],[x+12*r*1.15/15,y-8*r/15],[x+5.5*r*1.15/6,y-6.5*r/6]])
    pygame.draw.polygon(screen,color,[[x-5*r*1.15/15, y-14*r/15],[x-12*r*1.15/15,y-8*r/15],[x-5.5*r*1.15/6,y-6.5*r/6]])
    pygame.draw.polygon(screen,(0,0,0),[[x+5*r*1.15/15, y-14*r/15],[x+12*r*1.15/15,y-8*r/15],[x+5.5*r*1.15/6,y-6.5*r/6]],1)
    pygame.draw.polygon(screen,(0,0,0),[[x-5*r*1.15/15, y-14*r/15],[x-12*r*1.15/15,y-8*r/15],[x-5.5*r*1.15/6,y-6.5*r/6]],1)
    circle(screen, color_eye, (x+3*r/5,y), r/3)
    circle(screen, color_eye, (x-2.5*r/5,y), r/3)
    circle(screen, (0,0,0), (x+3*r/5,y), r/3,1)
    circle(screen, (0,0,0), (x-2.5*r/5,y), r/3,1)
    ellipse(screen,(0,0,0),(x+3.2*r/5,y-r/4,r/10,r/2))
    ellipse(screen,(0,0,0),(x-2.3*r/5,y-r/4,r/10,r/2))
    pygame.draw.polygon(screen,color,[[x+r*8/15, y-13.3*r/15],[x+13*r/15,y-10*r/15],[x+5.5*r*1/6,y-6*r/6]])
    pygame.draw.polygon(screen,color,[[x-r*8/15, y-13.3*r/15],[x-13*r/15,y-10*r/15],[x-5.5*r*1/6,y-6*r/6]])
    pygame.draw.polygon(screen,color,[[x-2*r/30, y+r*9/30],[x+4*r/30, y+r*9/30],[x+r/30,y+r*14/30]])
    pygame.draw.polygon(screen,(0,0, 0),[[x-2*r/30, y+r*9/30],[x+4*r/30, y+r*9/30],[x+r/30,y+r*14/30]],1)
    pygame.draw.polygon(screen,(0,0, 0),[[x+r/30, y+r*20/30],[x+r/30,y+r*14/30]],1)
    pygame.draw.arc(screen, (0,0,0),(x+r/30, y+r*20/30-r/10,2*r/10,2*r/10),2*pi/2, 2*pi-pi/4)
    pygame.draw.arc(screen, (0,0,0),(x+r/30-2*r/10, y+r*20/30-r/10,2*r/10,2*r/10),2*pi/2+pi/4, 2*pi)
    pygame.draw.arc(screen, (0,0,0),(x+r/30+r/4,y+r*16/30-r/8,r,r/4),pi/6, pi)
    pygame.draw.arc(screen, (0,0,0),(x+r/30+r/4,y+r*18/30-r/8,r,r/4),pi/6, pi)
    pygame.draw.arc(screen, (0,0,0),(x+r/30+r/4,y+r*20/30-r/8,r,r/4),pi/6, pi)
    pygame.draw.arc(screen, (0,0,0),(x+r/30-r/4-r,y+r*16/30-r/8,r,r/4),0,5*pi/6)
    pygame.draw.arc(screen, (0,0,0),(x+r/30-r/4-r,y+r*18/30-r/8,r,r/4),0,5*pi/6)
    pygame.draw.arc(screen, (0,0,0),(x+r/30-r/4-r,y+r*20/30-r/8,r,r/4), 0,5*pi/6)
    draw_ellipse_angle(screen, (255,255,255), (x+2.45*r/5,y-r/4,r/8,r/3), 30, 2)
    draw_ellipse_angle(screen, (255,255,255), (x-3.05*r/5,y-r/4,r/8,r/3), 30, 2)

# Рисуем жекклубок!

def clubok(x,y,r):
    

    circle(screen, (139,139, 122), (x,y), r)
    circle(screen, (0,0,0), (x,y), r,1)
    pygame.draw.arc(screen, (0,0,0),(x-r/2,y-r/4,r,r/2),pi/2,pi)
    pygame.draw.arc(screen, (0,0,0),(x-r/4,y-r/6,4*r,r/2),5*pi/6,pi)
    pygame.draw.arc(screen, (0,0,0),(x-r/1.4,y-r/2,6*r,r/2),4.5*pi/6,pi)
    pygame.draw.arc(screen, (0,0,0),(x+r/4,y-r/2,r/2,r),4.5*pi/6,4.8*pi/6)
    pygame.draw.arc(screen, (0,0,0),(x+r/6,y-r/4,r/2,4*r),4.5*pi/6,4.9*pi/6)
    pygame.draw.arc(screen, (0,0,0),(x+r/2,y-r/1.4,r/2,6*r),4.5*pi/6,4.9*pi/6)
    pygame.draw.arc(screen, (0,0,0),(x,y+r-r/4,8*r,r/2),pi,3*pi/2)

cat((240, 255, 255),(0, 154, 205),500,500,30)
cat((105, 105 ,105),(0, 0, 255),600,600,20)
cat((255, 255, 255),(49,255,1),300,600,30)
cat((255, 165, 0),(0, 250, 154),100,450,20)
cat((222, 184, 135),(255, 215, 0),600,700,25)
cat((139, 134, 130),(30, 144, 255),100,650,20)
cat((255, 215, 0),(173, 255, 47),700,400,20)
clubok(100,750,20)
clubok(350,720,20)
clubok(500,730,10)
clubok(100,500,25)
clubok(350,400,20)
clubok(500,400,28)
clubok(340,500,28)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

