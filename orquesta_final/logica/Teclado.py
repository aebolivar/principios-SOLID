from logica.Instrumento import Instrumento as i


class Teclado(i):
	
    NAME = "Teclado"

    def afinar(self):
        super().afinar()
        return "Afinando " + self.NAME + " con Afinador digital"

    def tocar(self):
        super().tocar()
        return "Tocando " + self.NAME  
