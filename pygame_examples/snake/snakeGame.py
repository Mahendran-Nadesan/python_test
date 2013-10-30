import pygame,sys
import random
from snake import Snake
from pygame.locals import *
from settings import *

pygame.init()
fpsClock=pygame.time.Clock()
surf=pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
gameSnake=Snake(3,3)
apples=[]
lost=False

def cordToPixels(cord):
    return (cord[0]*RECTWIDTH,cord[1]*RECTHEIGHT)

def update():
    global lost
    for x in gameSnake.body:
        if x==gameSnake.nextMove():
            lost=True
    next_m=gameSnake.nextMove()
    if next_m[0]==0 or next_m[0]==WINDOWWIDTH//RECTWIDTH:
        lost=True
    if next_m[1]==0 or next_m[1]==WINDOWHEIGHT//RECTHEIGHT:
        lost=True
    gameSnake.move()
    for x in apples:
        if x==gameSnake.head:
            apples.remove(x)
            gameSnake.eat=True
            addRandomApple()
            
    
def background_draw():
    surf.fill(BLACK)
    pygame.draw.rect(surf,WHITE,(0,0,WINDOWWIDTH,WINDOWHEIGHT),RECTWIDTH*2)

def draw_rect_on_cord(cord,color):
    pygame.draw.rect(surf,color,(cordToPixels(cord)[0],cordToPixels(cord)[1],RECTWIDTH,RECTHEIGHT),0)
    
def draw_snake():
    for x in gameSnake.body:
        draw_rect_on_cord(x,WHITE)
    for x in apples:
        draw_rect_on_cord(x,WHITE)
        

def handle_input():
    for event in pygame.event.get():
        if event.type== QUIT :
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if (event.key == K_LEFT or event.key == K_a) and gameSnake.direction!= (1,0):
                gameSnake.setDirection('left')
            elif (event.key == K_RIGHT or event.key == K_d) and gameSnake.direction!= (-1,0):
                gameSnake.setDirection('right')
            elif (event.key == K_UP or event.key == K_w) and gameSnake.direction!= (0,1):
                gameSnake.setDirection('up')
            elif (event.key == K_DOWN or event.key == K_s) and gameSnake.direction!= (0,-1):
                gameSnake.setDirection('down')

def addRandomApple():
    randomX=random.randrange(1,WINDOWWIDTH//RECTWIDTH)
    randomY=random.randrange(1,WINDOWHEIGHT//RECTHEIGHT)
    apples.append((randomX,randomY))
def main():    
    addRandomApple()
    addRandomApple()
    addRandomApple()
    while True :
        if lost:
            pygame.quit()
            sys.exit()
        background_draw()
        handle_input()
        update()
        draw_snake()
        pygame.display.update()
        fpsClock.tick(FPS)               
    
if __name__ == '__main__':
    main()

