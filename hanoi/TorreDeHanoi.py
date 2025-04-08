from nodo import Nodo

class TorresDeHanoi:
    def __init__(self, discos):
        self.discos = discos
        self.torres = [list(range(discos, 0, -1)), [], []]

    def mover(self, origen, destino):
        if self.torres[origen] and (not self.torres[destino] or self.torres[origen][-1] < self.torres[destino][-1]):
            disco = self.torres[origen].pop()
            self.torres[destino].append(disco)
        else:
            raise ValueError("Movimiento inválido")

    def resolver(self, n=None, origen=0, auxiliar=1, destino=2):
        if n is None:
            n = self.discos
        if n > 0:
            self.resolver(n - 1, origen, destino, auxiliar)
            self.mover(origen, destino)
            self.resolver(n - 1, auxiliar, origen, destino)

    def __str__(self):
        return "\n".join(f"Torre {i}: {self.torres[i]}" for i in range(3))