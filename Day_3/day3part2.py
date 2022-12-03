class Rucksack:
    def calculate(arch):
        list = arch.readlines()
        res = []
        for sub in list:
            res.append(sub.replace("\n", ""))
     
        values = []
        target = ""
        
        for j in range(0,len(res),3):
            print(res[j],res[j+1],res[j+2])
            for x in res[j]:
                if x in res[j+1]:
                    if x in res[j+2]: 
                        target = x
            bol = target.isupper()
            print(target)
            priority = ord(target) - 96 + (58*bol) 

            
            values.append(priority)
                        
                
            
        
          
        
        return sum(values)

if __name__ == "__main__":
    
    Rucksack.calculate(open("testinput.txt","r"))