class Directories:
    def calculate(arch):
        archive = arch.readlines()
        all = [[]] #all data will be here
        arch_dict = { #stores where in all is stored
            "/" : all[0]
        }
        tree_dict = {} #stores relationships
        actual_dir = ""
        previous_dir = ""
        count = 0
        for i in archive:
            vals = i.split()
            
            if vals[0] == "$":

                if vals[1] == "cd": #change directories

                    if vals[2] == "/":
                        actual_dir = "/" #base case

                    elif vals[2] == "..":
                        actual_dir = tree_dict.get(actual_dir) #go to parent saved in dict

                    else:
                        previous_dir = actual_dir #save previous
                        actual_dir += vals[2] + "/" #save new
                        tree_dict[actual_dir] = previous_dir #notify the relationship parent-son


                else: #list elements
                    for j in archive[count+1:]:
                        poo = j.split()
                        bol = poo[0] == "dir"

                        if poo[0] == "$": #EOF
                            break

                        elif bol: #if a dir
                            name = actual_dir + poo[1] + "/" #save new dir
                            all.append([]) #create space for new dir
                            arch_dict[name] = all[len(all)-1] #save the space in the dict
                            arch_dict.get(actual_dir).append(name) #we add reference value to parent dir list

                        else: #if a file
                            arch_dict.get(actual_dir).append(int(poo[0])) #we only care about the size not name
                           
                        
            else: #if is not cd or ls ignore because they will only be taken care of in ls
                pass

            count +=1 #line we are on
            
        list_values = []
        for x in all:
            list_values.append(Directories.getSizes(x,arch_dict))

        deleteable = []

        for j in list_values:
            if j <= 100000:
                deleteable.append(j)

        return sum(deleteable)

        


    def getSizes(values,arch_dict):
        size = 0
        for i in values:
            if isinstance(i,int):
                size += i
            else:
                size += Directories.getSizes(arch_dict.get(i),arch_dict)


        return size

    

        
        


        
        
if __name__ == "__main__":
    
    Directories.calculate(open("testinput.txt","r"))