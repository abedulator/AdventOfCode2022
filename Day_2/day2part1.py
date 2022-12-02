class PPT:
    def calculo(archivo):
        lista = archivo.readlines()
        other = [0,"A","B","C"]
        me = [0,"X","Y","Z"]
        puntuacion = 0
        for i in lista:
            jugada_other = other.index(i[0])
            jugada_me = me.index(i[2])
            if jugada_other == jugada_me:
                puntuacion += 3 + jugada_me
            elif jugada_other == 1: #roca
                if jugada_me == 2: #papel
                    puntuacion += 6 + jugada_me
                else:
                    puntuacion += jugada_me
            elif jugada_other == 2: # papel
                if jugada_me == 3: #tijera
                   puntuacion += 6 + jugada_me
                else:
                    puntuacion += jugada_me
            else: #tijera
                if jugada_me == 1: #roca
                   puntuacion += 6 + jugada_me
                else:
                    puntuacion += jugada_me  
        return puntuacion











if __name__ == "__main__":
    
    PPT.calculo(open("testinput.txt","r"))