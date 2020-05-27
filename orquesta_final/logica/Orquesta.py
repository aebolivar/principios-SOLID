from logica.Instrumento import *
from logica.Clarinete import *
from logica.Guitarra import *
from logica.Marimba import *
from logica.Oboe import *
from logica.Saxofon import *
from logica.Teclado import *
from logica.Trompeta import *
from logica.Violin import *
from logica.Violonchelo import *


class Orquesta:

    instrumento1 = Instrumento()
    listInstrumento = [
        Clarinete(),
        Guitarra(),
        Marimba(),
        Oboe(),
        Saxofon(),
        Teclado(),
        Trompeta(),
        Violin(),
        Violonchelo()

    ]

    def asignarInstrumento(self, numInstrumento):
        self.instrumento1 = self.listInstrumento[numInstrumento]
        return self.instrumento1.NAME

    def afinarInstrumento(self):
        return self.instrumento1.afinar()

    def tocarInstrumento(self):
        return self.instrumento1.tocar()
