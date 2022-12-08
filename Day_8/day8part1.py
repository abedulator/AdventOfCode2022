class Tree:
    def calculate(arch):
        archive = arch.readlines()
        trees = []
        index = 0

        for i in archive: #make grid
            trees.append([])
            for j in i:
                if j == "\n":
                    pass
                else:
                    trees[index].append(int(j))
            index += 1
        
        height = len(trees)
        side = len(trees[0])
        #print(height,side)
        edge = (height * 2 + side* 2) -4 #corners
        
        interior = 0
        
        for x in range(1,height-1):
            for y in range(1,side-1):
                visible = [True,True,True,True]
                #print("---------------")
                #print(trees[x][y], "coor: ",x,y )
                #print("---------------")
                
                for up in range(x-1,-1,-1):
                    #print(trees[up][y])
                    if trees[x][y] <= trees[up][y]:
                        visible[0] = False
                        break

                for down in range(x+1,height):
                    #print(trees[down][y])
                    if trees[x][y] <= trees[down][y]:
                        visible[1] = False
                        break

                for left in range(y-1,-1,-1):
                    #print(trees[x][left])
                    if trees[x][y] <= trees[x][left]:
                        visible[2] = False
                        break

                for right in range(y+1,side):
                    #print(trees[x][right])
                    if trees[x][y] <= trees[x][right]:
                        visible[3] = False
                        break


                #print(visible)
                
                if sum(visible) > 0:
                    interior += 1
                
                

        #print(interior)
        return edge + interior
        
        
        
if __name__ == "__main__":
    
    Tree.calculate(open("testinput.txt","r"))