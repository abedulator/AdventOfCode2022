class Crane:
    def calculate(arch):
        archive = arch.readlines()
        separator = 0
        for i in archive: #separate between crane and movements by the position of \n
            if i == "\n":
                break
            separator += 1

        print(separator)

        numbers = archive[separator-1] #number of pilars
        
        how_many = int(len(numbers)/4)
        print(how_many)
        print("-------------------")
        item_list = []
        

        for j in archive[0:separator-1]: #crane set up
            for x in range(1,how_many*4,4):
                item_list.append(j[x])
        print("lista de items")
        print(item_list)
        print("-----------------------")
        tmp_list = []
        final_list = []
        shift = 0
        for i in range(how_many):
            for j in range(0+shift,len(item_list),how_many):
                tmp_list.append(item_list[j])
            final_list.append(tmp_list)
            tmp_list = []
            shift += 1
        print("lista separada")
        print(final_list)
        print("-----------------------")
        index = 0
        for j in final_list:
            j.reverse()
            final_list[index] = ' '.join(final_list[index]).split()
            index += 1
        print("lista al reves y sin espacios")

        print(final_list)
        
        #one_list.reverse()
        #one_list = ' '.join(one_list).split()
        
        #print(one_list)
       




        #print("--------------------")
        for y in archive[separator+1:]: #movements
            pass
            #print(y)

           
            
       

if __name__ == "__main__":
    
    Crane.calculate(open("puzzleinput.txt","r"))