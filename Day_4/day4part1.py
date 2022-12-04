class Camp:
    def calculate(arch):
        list = arch.readlines()
        count = 0
        for i in list:
            first , second = i.split(",")
            min1 , max1 = first.split("-")
            min2 , max2 = second.split("-")
            if (int(min1) <= int(min2) and int(max1) >= int(max2)) or (int(min2) <= int(min1) and int(max2) >= int(max1)):
                count += 1
        
        return count

        

            





if __name__ == "__main__":
    
    Camp.calculate()