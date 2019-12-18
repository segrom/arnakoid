#-*-coding:utf8;-*-
#qpy:3
#qpy:console

class Downbar():
    def __init__(self,wigth):
        self.w=wigth
    def Print(self,frame):
        line=["="*self.w]
        inf="frime:"+str(frame)
        empty=" "*(self.w-len(inf)-1)
        print()
        print (*line)
        print("|"+inf+empty+"|")
        print(*line)
