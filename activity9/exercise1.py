"""
1. Usa programación dinámica para resolver el problema de encontrar el máximo conjunto independiente con mayor peso.
Usa el archivo MWIS.txt para obtener los datos, cada dato es el peso de un vértice en un grafo camino.
Contesta los siguiente:
¿Cuáles de los vértices 1, 2, 3, 4, 17, 117, 517, y 997 forman parte de la solución óptima?
"""

def mwis(w):
    # Obtiene el valor optimo
    n = len(w)
    a = [0, w[0]]
    for i in range(2, n+1):
        a.append(max(
            a[i-1],
            a[i-2] + w[i-1]
        ))

    # Reconstruir la solucion
    i = n
    s = set()
    while i >= 1:
        if a[i] == a[i-1]:
            i -= 1
        else:
            s.add(i-1)
            i -= 2
    print(s)


w = []

with open("MWIS.txt", "r") as f:
    for line in f:
        line = line.strip()
        w.append(int(line))

mwis(w)
