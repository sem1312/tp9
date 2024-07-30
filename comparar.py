import time
import matplotlib.pyplot as plt
import random

def generar_lista(tamano):
    return sorted(random.sample(range(1, 1000000), tamano))

def comparar_tiempos():
    tamaños = [100, 1000, 5000, 10000, 20000, 50000]
    tiempos_lineal = []
    tiempos_binaria = []

    for tamaño in tamaños:
        lista = generar_lista(tamaño)
        elemento = random.choice(lista)


        inicio = time.time()
        busqueda_lineal(lista, elemento)
        tiempos_lineal.append(time.time() - inicio)


        inicio = time.time()
        busqueda_binaria(lista, elemento)
        tiempos_binaria.append(time.time() - inicio)

    return tamaños, tiempos_lineal, tiempos_binaria

def main():
    tamaños, tiempos_lineal, tiempos_binaria = comparar_tiempos()

    plt.plot(tamaños, tiempos_lineal, label='Búsqueda Lineal')
    plt.plot(tamaños, tiempos_binaria, label='Búsqueda Binaria')
    plt.xlabel('Tamaño de la Lista')
    plt.ylabel('Tiempo de Ejecución (s)')
    plt.title('Comparación de Tiempos de Búsqueda')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
