from logica.Instrumento import Instrumento as i


class Guitarra(i):
	
    NAME = "Guitarra"

    def afinar(self):
        super().afinar()
        return "Afinando " + self.NAME + " (Cuerdas)"

    def tocar(self):
        super().tocar()
        return "Tocando " + self.NAME  