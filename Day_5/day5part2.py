class Camp:
    def calculate(arch):
        archive = arch.readlines()
        count = 0
        for i in archive:
            first , second = i.split(",")
            min1 , max1 = first.split("-")
            min2 , max2 = second.split("-")
            listfirst = list(range(int(min1),int(max1)+1))
            listsecond = list(range(int(min2),int(max2)+1))
            inter = list(set(listfirst) & set(listsecond))
            if inter:
                count += 1
        
        return count

        

            





if __name__ == "__main__":
    
    Camp.calculate()