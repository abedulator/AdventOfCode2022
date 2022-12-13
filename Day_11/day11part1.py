class Monkey:
    def calculate(arch):
        archive = arch.readlines()
        index = 0
        zoo =  []
        num_monkey = 0
        inspect = []
        for i in archive:
            j = i.split()
            
            if j != []:
                if j[0] == "Monkey":
                    zoo.append([])
                    inspect.append([0])
                    zoo[num_monkey].append(archive[index+1].split(":")[1].split(",")) #starting items
                    zoo[num_monkey].append(archive[index+2].split("=")[1].split()[1:]) #* or + and by what
                    zoo[num_monkey].append(archive[index+3].split()[-1]) # divisible by what
                    zoo[num_monkey].append(archive[index+4].split()[-1]) # if true to 
                    zoo[num_monkey].append(archive[index+5].split()[-1]) # if false to
                    zoo[num_monkey].append(num_monkey)
                    num_monkey += 1
            index += 1
        val = 0
        round = 0
        while round < 21:
            print("--------------")
            print("ronda numero: " + str(round))
            for monkey in zoo:
                print("Mono numero: " + str(monkey[5]))
                print(monkey[0])
                for item in monkey[0]:
                    inspect[monkey[5]][0] += 1
                    if monkey[1][1] == "old":
                        val= (int(item)*int(item))//3 
                    elif monkey[1][0] == "+":
                        val = (int(item) + int(monkey[1][1]))//3
                    else:
                        val = (int(item) * int(monkey[1][1]))//3
                    
                    if val % int(monkey[2]) == 0:
                        
                        zoo[int(monkey[3][0])][0].append(val)
                      
                    else:
                        
                        zoo[int(monkey[4][0])][0].append(val)
                        
                    del monkey[0][0]
            print("------------")
            for monkeys in zoo:
                print(monkeys[0])
            round += 1


        print(inspect)


        
        
if __name__ == "__main__":
    
    Monkey.calculate(open("testinput.txt","r"))