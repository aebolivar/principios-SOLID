from logica.Instrumento import Instrumento as i


class Trompeta(i):
	
    NAME = "Trompeta"

    def afinar(self):
        super().afinar()
        return "Afinando " + self.NAME + " (Limpiando boquilla)"

    def tocar(self):
        super().tocar()
        return "Tocando " + self.NAME  
