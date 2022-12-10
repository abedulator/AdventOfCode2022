
class Tube:
    def calculate(arch):
        archive = arch.readlines()
        X = 1
        cycle = 1
        signals = []
        extracycle = False
        index = 0
        while cycle < 221:
            #print(cycle)
            if not extracycle:
                i = archive[index]
                ign = i.split()
                
                if ign[0] == "addx":
                    val = ign[1]
                    extracycle = True
                
                index += 1
                if cycle in range(20,240,40):
                    signals.append(X*cycle)
                cycle += 1
            else:
                
                if cycle in range(20,240,40):
                    signals.append(X*cycle)
                cycle += 1
                X += int(val)
                extracycle = False
        #print(signals)
        return sum(signals)
    


        
if __name__ == "__main__":
    
    Tube.calculate(open("testinput.txt","r"))

