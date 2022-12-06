class Signal:
    def calculate(line):
        
        tmp = []
        for i in range(13,len(line)):
            tmp = [line[i-13],line[i-12],line[i-11],line[i-10],line[i-9],line[i-8],line[i-7],line[i-6],line[i-5],line[i-4],line[i-3],line[i-2],line[i-1],line[i]]

            
            if len(set(tmp)) == len(tmp):
                return i+1
                
        
        
if __name__ == "__main__":
    
    Signal.calculate(open("testinput.txt","r"))