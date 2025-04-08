from caballo.lanzador import Lanzador as CaballoLanzador
from reinas.lanzador import Lanzador as ReinasLanzador
from reinas.reinas import NReinas

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Ejecutar simulación del caballo")
    print("2. Ejecutar simulación de las reinas")
    print("3. Salir")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Ingrese su elección: ")
        
        if opcion == "1":
            CaballoLanzador.ejecutar_simulacion()
        elif opcion == "2":
                n = int(input("Introduce el tamaño del tablero (N): "))
                n_reinas = NReinas(n)
                n_reinas.ejecutar_simulacion()
                ReinasLanzador.ejecutar_simulacion()
        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")