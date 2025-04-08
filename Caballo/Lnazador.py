from Caballos import Caballos
import random
import time
import sys
import pygame

class Lanzador:
    """Clase que representa el lanzador del caballo."""
    def __init__(self):
        # Movimientos posibles del caballo
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

    def main():
        """Función principal para ejecutar el lanzador del caballo."""
        lanzador = Lanzador()
        num_movimientos = int(input("Introduce el número de movimientos: "))
        total_movimientos = lanzador.calcular_movimientos_iniciales(num_movimientos)
        print(f"Total de movimientos válidos: {total_movimientos}")

    @staticmethod
    def inicializar_pygame():
        """Inicializa Pygame y configura la ventana."""
        pygame.init()
        WIDTH, HEIGHT = 800, 600
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Movimientos del Caballo en el Teclado")
        return screen

    def obtener_colores():
        """Define los colores utilizados en la aplicación."""
        return {
            "WHITE": (255, 255, 255),
            "BLUE": (0, 0, 255),
            "GREEN": (0, 255, 0),
            "RED": (255, 0, 0),
            "BLACK": (0, 0, 0)
        }

    def obtener_teclas_posiciones():
        """Define las posiciones de las teclas en la pantalla."""
        return {
            1: (200, 100), 2: (300, 100), 3: (400, 100),
            4: (200, 200), 5: (300, 200), 6: (400, 200),
            7: (200, 300), 8: (300, 300), 9: (400, 300),
            0: (300, 400)
        }

    def dibujar_teclas(screen, teclas_posiciones, colores):
        """Dibuja las teclas en la pantalla."""
        for tecla, (x, y) in teclas_posiciones.items():
            pygame.draw.circle(screen, colores["BLUE"], (x, y), 30)
            font = pygame.font.SysFont(None, 24)
            texto = font.render(str(tecla), True, colores["WHITE"])
            screen.blit(texto, (x - 10, y - 10))

    def dibujar_conexiones(screen, teclas_posiciones, movimientos, colores):
        """Dibuja las conexiones entre las teclas según los movimientos del caballo."""
        for tecla, destinos in movimientos.items():
            x1, y1 = teclas_posiciones[tecla]
            for destino in destinos:
                x2, y2 = teclas_posiciones[destino]
                pygame.draw.line(screen, colores["GREEN"], (x1, y1), (x2, y2), 2)

    def mostrar_resultados(screen, num_movimientos, total, colores):
        """Muestra los resultados en la pantalla."""
        font = pygame.font.SysFont(None, 36)
        texto = font.render(f"Movimientos válidos con {num_movimientos} movimiento(s): {total}", True, colores["BLACK"])
        screen.blit(texto, (50, 500))

    def ejecutar_simulacion():
        screen = Lanzador.inicializar_pygame()
        screen = Lanzador.inicializar_pygame()
        colores = Lanzador.obtener_colores()
        teclas_posiciones = Lanzador.obtener_teclas_posiciones()
        caballos = Caballos()  # Instancia de la clase Caballos para obtener movimientos
        movimientos = caballos.movimientos  # Movimientos posibles del caballo

        clock = pygame.time.Clock()
        running = True

        while running:
            screen.fill(colores["WHITE"])
            
            # Dibujar teclas y conexiones
            dibujar_teclas(screen, teclas_posiciones, colores)
            dibujar_conexiones(screen, teclas_posiciones, movimientos, colores)
            
            # Calcular los movimientos válidos para un número de pasos
            num_movimientos = 2  # Cambiar este número para probar diferentes cantidades de movimientos
            total_movimientos = caballos.calcular_movimientos_iniciales(num_movimientos)

            # Mostrar resultados
            mostrar_resultados(screen, num_movimientos, total_movimientos, colores)

            # Detectar eventos de cierre de ventana
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Actualizar la pantalla
            pygame.display.flip()

            # Controlar la tasa de refresco
            clock.tick(60)

        pygame.quit()
        sys.exit()

       

    