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
            #print("loop")
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
                        #print(poo)
                        bol = poo[0] == "dir"
                        if poo[0] == "$": #EOF
                            #print("break")
                            break
                        elif bol: #if a dir
                            name = actual_dir + poo[1] + "/" #save new dir
                            #print("llego a dir")
                            all.append([]) #create space for new dir
                            arch_dict[name] = all[1-len(all)] #save the space in the dict
                            arch_dict.get(actual_dir).append(name) #we add reference value to parent dir list

                        else: #if a file
                            arch_dict.get(actual_dir).append(poo[0]) #we only care about the size not name
                            #print(actual_dir)
                            #print("llego a file")
                            #print(arch_dict.get(actual_dir))
                        
            else: #if is not cd or ls ignore because they will only be taken care of in ls
                pass
            count +=1 #line we are on
            #print(vals)
            #print(all)

        #print(tree_dict)
        return arch_dict

        
        


        
        
if __name__ == "__main__":
    
    Directories.calculate(open("testinput.txt","r"))