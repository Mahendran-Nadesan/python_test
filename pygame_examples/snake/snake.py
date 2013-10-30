class Snake:
    def __init__(self,x,y):
        self.body=[(x,y)]
        self.head=(x,y)
        self.direction=(1,0)
        self.eat=False
    def setDirection(self,str_dir):
        if str_dir ==  'right':
            self.direction=(1,0)
        elif str_dir ==  'left':
            self.direction=(-1,0)
        elif str_dir ==  'up':
            self.direction=(0,-1)
        elif str_dir ==  'down':
            self.direction=(0,1)
    def nextMove(self):
        return (self.head[0]+self.direction[0],self.head[1]+self.direction[1])
    def move(self):
        self.body.append(self.nextMove())
        self.head=self.nextMove()
        if not self.eat:
            self.body.pop(0)
        else:
            self.eat=False
    
        
    
