from logica.Instrumento import Instrumento as i


class Violonchelo(i):
	
    NAME = "Violonchelo"

    def afinar(self):
        super().afinar()
        return "Afinando " + self.NAME + " (Cuerdas)"

    def tocar(self):
        super().tocar()
        return "Tocando " + self.NAME  
