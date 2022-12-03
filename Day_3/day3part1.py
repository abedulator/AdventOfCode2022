class Rucksack:
    def calculate(arch):
        list = arch.readlines()
        values = []
        
        for i in list:
            target = ""
            val = len(i)
            halfval = int(val/2)

            fhalf = i[0:halfval]
            shalf = i[halfval:val]
            for j in fhalf:
                if j in shalf:
                    target = j
            
            bol = target.isupper()
            priority = ord(target) - 96 + (58*bol) 

            
            values.append(priority)
        
        return sum(values)


            





if __name__ == "__main__":
    
    Rucksack.calculate()