from pprint import pprint

#  Laberinto (9x9) 

maze = [
    [1, 1, 1, 1, 99, 1, 1, 1, 1],   
    [1, 99, 99, 1, 99, 1, 99, 1, 99],
    [1, 1, 99, 1, 1, 1, 99, 1, 99],
    [99, 1, 99, 1, 99, 99, 99, 1, 99],
    [1, 1, 99, -1, 1, 1, 1, 3, 99],
    [-2, 99, 99, 1, 99, 99, 99, 1, 1],
    [1, 99, 1, -1, 1, 1, 1, 1, 99],
    [1, 99, 99, 99, 99, 2, 99, 1, 99],
    [0, 1, 3, 1, 1, 1, 99, 1, 1],  
]

rows = len(maze)
cols = len(maze[0])

# Coordenadas (fila, columna)
start = (0, 8)
goal = (8, 0)   
initial_energy = 18

# Movimientos 
moves = [(0, -1), (1, 0), (-1, 0), (0, 1)]

solution_path = None

best_energy_at = {}

def step_cost(r, c):
    """Devuelve el coste energético de la celda (r,c) al entrar.
       Si es start o goal => 0 (según enunciado).
       Si es otro valor: coste = valor; si es negativo repone energía.
    """
    if (r, c) == start or (r, c) == goal:
        return 0
    return maze[r][c]

def dfs(r, c, energy, path):
    """
    DFS con backtracking que mantiene la energía actual.
    'energy' es la energía que queda **antes** de entrar en (r,c).
    Cuando se entra, se aplica el coste (positivo resta, negativo suma).
    """
    global solution_path


    if solution_path is not None:
        return

    # Límites
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return

    cell = maze[r][c]
    # Muro
    if cell == 99:
        return




    cost = step_cost(r, c)
    new_energy = energy - cost  


    if new_energy < 0:
        return


    prev_best = best_energy_at.get((r, c), -1)
    if new_energy <= prev_best:
        return
    best_energy_at[(r, c)] = new_energy

    
    path.append((r, c))

    
    if (r, c) == goal:
        solution_path = path.copy()
        return

    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        dfs(nr, nc, new_energy, path)
        if solution_path is not None:
            return


    path.pop()

def mostrar_matriz_con_camino(path):
    """Imprime la matriz con el camino marcado con 'P'"""
    display = [[("{:>3}".format(v)) for v in row] for row in maze]
    if path:
        for (r, c) in path:
            display[r][c] = " P "
    for fila in display:
        print(" ".join(fila))

def main():
    print("\n--- LABERINTO ORIGINAL (99 = muro, valores negativos repone energía) ---")
    pprint(maze)

    dfs(start[0], start[1], initial_energy, [])

    if solution_path is None:
        print("\nNo se encontró un camino válido desde la casilla verde hasta la roja con la energía disponible (iniciando con {} unidades).".format(initial_energy))
    else:
        print("\n¡Se encontró un camino!")
        print("Ruta (lista de coordenadas (fila, columna) en orden):")
        print(solution_path)

        print("\nMatriz con el camino marcado (P):")
        mostrar_matriz_con_camino(solution_path)

if __name__ == "__main__":
    main()