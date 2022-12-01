

class Calorias:
    def calculo(archivo):
        lista = archivo.readlines()
        
        list = []
        val = 0
        for i in lista:
            if i == "\n":
                list.append(val)
                
                val = 0
            else:
                num = i.strip("\n")
                val = int(num) + val
                
                
        list.append(val)
        mx = []
        for j in range(3):
            mx.append(max(list))
            list.remove(max(list))

        value = sum(mx)

            
        return value



if __name__ == "__main__":
    
    Calorias.calculo()