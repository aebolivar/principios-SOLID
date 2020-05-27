from logica.Instrumento import Instrumento as i


class Violin(i):
	
    NAME = "Violin"

    def afinar(self):
        super().afinar()
        return "Afinando " + self.NAME + " (Cuerdas)"

    def tocar(self):
        super().tocar()
        return "Tocando " + self.NAME  
