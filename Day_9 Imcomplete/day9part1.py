class Rope:
    def calculate(arch):
        archive = arch.readlines()
        H = Head([0,0],[0,0])
        T = Tail()
        pos = []
        index = 0
        for i in archive:
            dir , ammount = i.split()
            #print(dir,ammount)
            for j in range(int(ammount)):
                T.Hpos = H.pos 
                H.previousPos = H.move(dir)
                #print("se mueve")
                #print(H.pos,H.previousPos)
                if not T.isTouching():
                    #print("no se toca")
                    T.move(H.previousPos)
                    #print(T.pos,T.visited)
        
        print(T.visited)
        return len(T.visited) #6402 too high


                



class Head:
    def __init__(self,pos,previousPos): #pos = [x,y] x - hor / y - ver 
        self.pos = pos
        self.previousPos = previousPos
    
    def move(self,dir):
        
        if dir == "R":
            self.pos[0] += 1
            return [self.pos[0] - 1,self.pos[1]]
            
           
        elif dir == "L":
            
            self.pos[0] -= 1
            return [self.pos[0] + 1,self.pos[1]]
            
        elif dir == "U":
            self.pos[1] += 1
            return [self.pos[0],self.pos[1]-1]
            
        else:
            self.pos[1] -= 1
            return [self.pos[0],self.pos[1]+1]
           



class Tail:
    def __init__(self,pos = [0,0],visited = [[0,0]],Hpos = [0,0]): #pos = [x,y] x - hor / y - ver 
        self.pos = pos
        self.visited = visited
        self.Hpos = Hpos

    def isTouching(self):
        adyacent = []
        moves = [-1,0,1]

        for j in moves:
            for i in moves:
                adyacent.append([self.pos[0]+ i,self.pos[1]+ j]) #9 touching positions
        if self.Hpos in adyacent:
            return True
        else:
            return False
    
    def move(self,position):
        self.pos = position
        if position not in self.visited:
            self.visited.append(position)


        
        
if __name__ == "__main__":
    
    Rope.calculate(open("testinput.txt","r"))