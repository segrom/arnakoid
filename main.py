#-*-coding:utf8;-*-
#qpy:3
#qpy:console
import time, os
from downbar import *
screenWight=20
screenHeight=20
class Vector():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def Set(self, x,y):
        self.x = x
        self.y = y

class Screen():
    def __init__(self, w,h,pat, border):
        self.matx =[]
        self.pat = pat
        self.w = w
        self.h = h
        self.border=border
        self.Clear()
        
    def Clear(self):
        self.matx=[]
        border=self.border
        if border:
            borderLine=[]
            for y in range(self.h//2+2):borderLine.append("[]")
            self.matx.append(borderLine)
        for y in range(self.h):
            line=[]
            if border:line.append("[]")
            for x in range(self.w):
                line.append(self.pat)
            if border:line.append("[]")
            self.matx.append(line)
        self.matx.append(borderLine)
    def Print(self):
        #print(self.matx)
        for i in self.matx:
            print(*i,sep="")
    def Set(self,x,y,face):
        self.matx[x][y]= face
            
class Obj():
    def __init__(self, face, position):
        self.face = str(face)
        self.pos = position
    def Create(obj):
        objects.append(obj)
    def Delete(self):
        for ob in objects:
            if(ob is self):
                objects.remove(ob)
                del(ob)

class Ball(Obj):
    def __init__(self,face,position,velocity):
        self.face = str(face)
        self.pos = position
        self.vel = velocity
        objects.append(self)
    def Move(self):
        x=self.pos.x+self.vel.x
        y=self.pos.y+self.vel.y
        if x>=screenWight or x<=0:self.vel.x=-self.vel.x
        if y>=screenHeight+1 or y<=0:self.vel.y=-self.vel.y
        for ob in objects:
            if x==ob.pos.x and y==ob.pos.y and ob!=self: 
                self.vel.x=-self.vel.x
                self.vel.y=-self.vel.y     
                if isinstance(ob,Wall): ob.Collision()
                break 
            if x==ob.pos.x and self.pos.y==ob.pos.y:
                self.vel.x=-self.vel.x
                if isinstance(ob,Wall): ob.Collision()
                break
            if y==ob.pos.y and self.pos.x==ob.pos.x:
                self.vel.y=-self.vel.y
                if isinstance(ob,Wall): ob.Collision()
                break
            
        self.pos = Vector(self.pos.x+self.vel.x,self.pos.y+self.vel.y)

class Wall(Obj):
    def __init__(self, face1, face2,position,maxhp):
        self.pos=position
        self.face1=face1
        self.face2=face2
        self.face=face1
        self.hp=maxhp
        objects.append(self)
    def Collision(self):
        self.hp-=1
        hp=self.hp
        if(hp<=0): 
            self.face="X"
            self.Delete()
            return
        if(hp==1): self.face =self.face2
        else:self.face=self.face1
        

objects = []
screen = Screen(screenWight,screenHeight," ",True)
ball = Ball("o", Vector(1,1), Vector(1,2))
ball2=Ball("0", Vector(8,9), Vector(-1,1))
Obj.Create(Obj("@",Vector(5,7)))
wall = Wall("S","B",Vector(5,9),2)
bar=Downbar(screenWight)
for i in range(500):
    screen.Print()
    screen.Clear()
    bar.Print(i)
    for ob in objects:
        screen.Set(ob.pos.x,ob.pos.y,ob.face)
        if  isinstance(ob, Ball):
            ob.Move()
    time.sleep(0.1)
    os.system("clear")
        
                
        
