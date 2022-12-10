
class Tube:
    def calculate(arch):
        archive = arch.readlines()
        X = 1
        X_range = [X-1,X,X+1]
        cycle = 1
        signals = []
        extracycle = False
        index = 0
        CRT = 0 
        screen = ""
        while cycle < 241:
            #print(cycle)
            val_crt = CRT % 40
            
            if val_crt in X_range:
                screen += "#"
            else:
                screen += " "
            CRT += 1
            if not extracycle:
                i = archive[index]
                ign = i.split()
                
                if ign[0] == "addx":
                    val = ign[1]
                    extracycle = True
                index += 1
                cycle += 1
            else:
                cycle += 1
                X += int(val)
                extracycle = False
            X_range = [X-1,X,X+1]
        print(screen[:40])
        print(screen[40:80])
        print(screen[80:120])
        print(screen[120:160])
        print(screen[160:200])
        print(screen[200:])

        
    


        
if __name__ == "__main__":
    
    Tube.calculate(open("puzzleinput.txt","r"))

