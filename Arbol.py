class Nodo:
    """
    Clase que representa un nodo en un árbol de peso.

    Atributos:
      valor: El valor del nodo.
      peso: El peso del nodo.
      hijos: Una lista que contiene los hijos del nodo.
    """

    def __init__(self, valor, peso):
        self.valor = valor
        self.peso = peso
        self.hijos = []

    def __str__(self):
        return f"Nodo(valor={self.valor}, peso={self.peso}, hijos={self.hijos})"


def calcular_peso_total(arbol):
    """
    Calcula el peso total de un árbol de peso.

    Parámetros:
      arbol: El nodo raíz del árbol.

    Retorno:
      El peso total del árbol.
    """

    return arbol.peso + sum(map(calcular_peso_total, arbol.hijos))


def imprimir_arbol(arbol, nivel=0):
    """
    Imprime un árbol de peso en forma de árbol.

    Parámetros:
      arbol: El nodo raíz del árbol.
      nivel: El nivel actual del árbol (0 para la raíz).
    """

    if not arbol:
        return

    print(f"{' ' * nivel}{arbol.valor} ({arbol.peso})")
    [imprimir_arbol(hijo, nivel + 1) for hijo in arbol.hijos]


# Ejemplo de uso
arbol = Nodo(10, 10)
arbol.hijos.extend([Nodo(5, 5), Nodo(7, 7)])
arbol.hijos[0].hijos.extend([Nodo(2, 2), Nodo(3, 3)])

print("Peso total:", calcular_peso_total(arbol))
print()
imprimir_arbol(arbol)
