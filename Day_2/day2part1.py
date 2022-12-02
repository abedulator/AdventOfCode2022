class PPT:
    def calculo(archivo):
        lista = archivo.readlines()
        other = [0,"A","B","C"]
        me = [0,"X","Y","Z"]
        puntuaciones = [0,[0,3,6,0],[0,0,3,6],[0,6,0,3]]
        puntuacion = 0
        for i in lista:
            jugada_other = other.index(i[0])
            jugada_me = me.index(i[2])
            puntuacion += puntuaciones[jugada_other][jugada_me] + jugada_me
           
        return puntuacion











if __name__ == "__main__":
    
    PPT.calculo(open("testinput.txt","r"))