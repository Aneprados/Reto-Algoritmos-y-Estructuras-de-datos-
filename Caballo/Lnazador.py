import pygame
import sys

class Tablero:
    """Clase que representa el tablero y las posiciones de las teclas."""
    def __init__(self):
        self.teclas_posiciones = {
            1: (200, 100), 2: (300, 100), 3: (400, 100),
            4: (200, 200), 5: (300, 200), 6: (400, 200),
            7: (200, 300), 8: (300, 300), 9: (400, 300),
            0: (300, 400)
        }
        self.colores = {
            "WHITE": (255, 255, 255),
            "BLUE": (0, 0, 255),
            "GREEN": (0, 255, 0),
            "RED": (255, 0, 0),
            "BLACK": (0, 0, 0)
        }

    def dibujar_teclas(self, screen):
        """Dibuja las teclas en el tablero."""
        for tecla, (x, y) in self.teclas_posiciones.items():
            pygame.draw.circle(screen, self.colores["BLUE"], (x, y), 30)
            font = pygame.font.SysFont(None, 24)
            texto = font.render(str(tecla), True, self.colores["WHITE"])
            screen.blit(texto, (x - 10, y - 10))

    def dibujar_conexiones(self, screen, movimientos):
        """Dibuja las conexiones entre las teclas según los movimientos del caballo."""
        for tecla, destinos in movimientos.items():
            x1, y1 = self.teclas_posiciones[tecla]
            for destino in destinos:
                x2, y2 = self.teclas_posiciones[destino]
                pygame.draw.line(screen, self.colores["GREEN"], (x1, y1), (x2, y2), 2)


class Caballo:
    """Clase que representa los movimientos del caballo."""
    def __init__(self):
        self.movimientos = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }

    def contar_movimientos(self, pos, movimientos_restantes):
        """Cuenta los movimientos válidos desde una posición inicial."""
        if movimientos_restantes == 0:
            return 1
        total_movimientos = 0
        for siguiente_pos in self.movimientos[pos]:
            total_movimientos += self.contar_movimientos(siguiente_pos, movimientos_restantes - 1)
        return total_movimientos

    def calcular_movimientos_iniciales(self, num_movimientos):
        """Calcula los movimientos válidos desde todas las posiciones iniciales."""
        total_movimientos = 0
        for inicio in range(10):
            total_movimientos += self.contar_movimientos(inicio, num_movimientos - 1)
        return total_movimientos


class Simulador:
    """Clase que gestiona la simulación."""
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Movimientos del Caballo en el Teclado")
        self.clock = pygame.time.Clock()
        self.tablero = Tablero()
        self.caballo = Caballo()

    def mostrar_resultados(self, num_movimientos, total):
        """Muestra los resultados en la pantalla."""
        font = pygame.font.SysFont(None, 36)
        texto = font.render(f"Movimientos válidos con {num_movimientos} movimiento(s): {total}", True, self.tablero.colores["BLACK"])
        self.screen.blit(texto, (50, 500))

    def ejecutar(self):
        """Ejecuta la simulación."""
        running = True
        while running:
            self.screen.fill(self.tablero.colores["WHITE"])

            # Dibujar teclas y conexiones
            self.tablero.dibujar_teclas(self.screen)
            self.tablero.dibujar_conexiones(self.screen, self.caballo.movimientos)

            # Calcular los movimientos válidos para un número de pasos
            num_movimientos = 2  # Cambiar este número para probar diferentes cantidades de movimientos
            total_movimientos = self.caballo.calcular_movimientos_iniciales(num_movimientos)

            # Mostrar resultados
            self.mostrar_resultados(num_movimientos, total_movimientos)

            # Detectar eventos de cierre de ventana
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Actualizar la pantalla
            pygame.display.flip()

            # Controlar la tasa de refresco
            self.clock.tick(60)

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    simulador = Simulador()
    simulador.ejecutar()
