from logica.Instrumento import Instrumento as i


class Clarinete(i):
	
    NAME = "Clarinete"

    def afinar(self):
        super().afinar()
        return "Afinando " + self.NAME + " (Limpiando boquilla)"

    def tocar(self):
        super().tocar()
        return "Tocando " + self.NAME  