class PPT:
    def calculo(archivo):
        lista = archivo.readlines()
        other = [0,"A","B","C"]
        me = [0,"X","Y","Z"]
        perder = [0,3,1,2]
        ganar = [0,2,3,1]
        puntuacion = 0
        for i in lista:
            jugada_other = other.index(i[0])
            jugada_por_hacer = me.index(i[2])
            if jugada_por_hacer == 2: # empate
                puntuacion += jugada_other + 3
            elif jugada_por_hacer == 1: #perder
                puntuacion += perder[jugada_other]
            else: #ganar
                puntuacion += ganar[jugada_other] + 6

        return puntuacion











if __name__ == "__main__":
    
    PPT.calculo(open("testinput.txt","r"))