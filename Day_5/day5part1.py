class Crane:
    def calculate(arch):
        archive = arch.readlines()
        separator = 0
        for i in archive: #separate between crane and movements by the position of \n
            if i == "\n":
                break
            separator += 1

        

        numbers = archive[separator-1] #number of pilars
        
        how_many = int(len(numbers)/4)
        item_list = []
        

        for j in archive[0:separator-1]: #crane set up
            for x in range(1,how_many*4,4):
                item_list.append(j[x])

        tmp_list = []
        final_list = []
        shift = 0
        for i in range(how_many):
            for j in range(0+shift,len(item_list),how_many):
                tmp_list.append(item_list[j])
            final_list.append(tmp_list)
            tmp_list = []
            shift += 1
       
        index = 0
        for j in final_list:
            j.reverse()
            final_list[index] = ' '.join(final_list[index]).split()
            index += 1
        
        form = []
        for y in archive[separator+1:]: #movements
            form = y.split(" ")
            count = int(form[1])
            from_column = int(form[3]) -1
            to_column = int(form[5]) -1
            for i in range(count):
                final_list[to_column].append(final_list[from_column][-1])
                final_list[from_column].pop(-1)
                i += 1
        result = ""
        for j in range(len(final_list)):
            result += final_list[j][-1]

        return result
if __name__ == "__main__":
    
    Crane.calculate(open("testinput.txt","r"))