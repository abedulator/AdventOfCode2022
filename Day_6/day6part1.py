class Signal:
    def calculate(line):
        
        tmp = []
        for i in range(3,len(line)):
            tmp = [line[i-3],line[i-2],line[i-1],line[i]] 
            if len(set(tmp)) == len(tmp):
                return i+1
                break
        
        
if __name__ == "__main__":
    
    Signal.calculate(open("testinput.txt","r"))