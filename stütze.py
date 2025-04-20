import color
import random
import pygame

class player():
    width:int
    height:int
    def __init__(self,width,height):
        self.x= width//4
        self.y= height//2
        self.width=50
        self.height=50
        self.color=color.gelb
    def move(self):
        self.y+=15
    def gravity(self):
        self.y-=5
    def draw(self,surf):
        pygame.draw.rect(surf,self.color,(self.x,self.y,self.width,self.height))
class rohr():
    x:int
    y:int
    height:int
    def __init__(self,x,y,height):
        self.x=x
        self.y=y
        self.width=100
        self.height=height
        self.color=color.green
    def speed(self):
        self.x-=5
    def draw(self,surf):
        pygame.draw.rect(surf,self.color,(self.x,self.y,self.width,self.height))

def generator(width,height):
    yv=random.randint(-100,100)
    rohrr=rohr(width-1,height+yv,height*2)
    mirrohr=rohr(width-1,0,rohrr.y - 200)
    return mirrohr,rohrr

def mirror(ro):
    mir=[]
    for i in range(len(ro)):
        hight=ro[i].y - 200
        mir.append(rohr(ro[i].x,0,hight))
    return mir

def collision (px,bx,py,by,pwidth,pheight,bwith,bheight):
    if px <= bx + bwith and px + pwidth >= bx and py<= by + bheight and py + pheight>= by:
        return True
    else:
        return False

