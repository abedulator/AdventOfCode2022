
        

            



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
        scenic_value = [0,0,0,0]
        values = []
        
        for x in range(1,height-1):
            for y in range(1,side-1):
                for up in range(x-1,-1,-1):
                    if trees[x][y] <= trees[up][y]:
                        scenic_value[0] += 1
                        break
                    else:
                        scenic_value[0] += 1

                for down in range(x+1,height):
                    if trees[x][y] <= trees[down][y]:
                        scenic_value[1] += 1
                        break
                    else:
                        scenic_value[1] += 1

                for left in range(y-1,-1,-1):
                    if trees[x][y] <= trees[x][left]:
                        scenic_value[2] += 1
                        break
                    else:
                        scenic_value[2] += 1

                for right in range(y+1,side):
                    if trees[x][y] <= trees[x][right]:
                        scenic_value[3] += 1
                        break
                    else:
                        scenic_value[3] += 1
                #print(scenic_value)
                mul = 1
                for j in scenic_value:
                    mul = j * mul
                scenic_value = [0,0,0,0]
                values.append(mul)

        return(max(values))

            


                
                
                
                
                

        
        
        
        
        
if __name__ == "__main__":
    
    Tree.calculate(open("testinput.txt","r"))

