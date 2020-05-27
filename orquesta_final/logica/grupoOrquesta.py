import random
from logica.Orquesta import Orquesta


class grupoOrquesta:

    listOrquesta = []
    listInstrumento = []
    listInstrumentoAfinar=[]
    listInstrumentoTocar=[]
    instrument = None

    def asignargrupoOrquesta(self):
        self.listInstrumento.clear()
        numRandom = random.randint(9, 14)
        for i in range(0, numRandom):
            self.listOrquesta.append(Orquesta())
            self.listInstrumento.append(self.listOrquesta[i].asignarInstrumento(
                random.randint(0, 4)))
        return self.listInstrumento

    def afinargrupoOrquesta(self):
        self.listInstrumentoAfinar.clear()
        for i in range(0, len(self.listOrquesta)):
            self.listInstrumentoAfinar.append(self.listOrquesta[i].afinarInstrumento())
        return self.listInstrumentoAfinar

    def tocargrupoOrquesta(self):
        self.listInstrumentoTocar.clear()
        for i in range(0, len(self.listOrquesta)):
            self.listInstrumentoTocar.append(self.listOrquesta[i].tocarInstrumento())
        return self.listInstrumentoTocar


