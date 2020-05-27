from logica.Instrumento import Instrumento as i


class Marimba(i):
	
    NAME = "Marimba"

    def afinar(self):
        super().afinar()
        return "Afinando " + self.NAME + " con Resonador"

    def tocar(self):
        super().tocar()
        return "Tocando " + self.NAME  
