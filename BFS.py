import math
import random
import time
import os

os.system('') #obsluga escape sekwencji do clearowania terminala

def generate_matrix(n: int):
    matrix = [[' ' for i in range(0,n)] for j in range(0,n)]

    return matrix

def view_matrix(matrix: list[list]):
    for i in matrix:
        print(i)


def generate_random_obstacles(matrix: list[list]):
    row_blocks = len(matrix[0])
    start = ()
    end = ()

    blocks_count = row_blocks * row_blocks
    obstacles = blocks_count * 0.4

    # zeby bylo najmniej 40% sprawdzam czy blocks_count to float
    # jezeli tak to += 1 i konwertuje na integer
    obstacles = int(math.ceil(obstacles))

    placed = 0
    while placed < obstacles:
        pos_x = random.randint(0, row_blocks-1)
        pos_y = random.randint(0, row_blocks-1)
        
        if can_place_obstacle(matrix, pos_y, pos_x):
            matrix[pos_y][pos_x] = "X"
            placed += 1

    placed = 0
    
    while placed < 2:
        pos_x = random.randint(0, row_blocks-1)
        pos_y = random.randint(0, row_blocks-1)


        if can_place_obstacle(matrix, pos_y, pos_x):
            if placed == 0:
                litera = "R"
                start = (pos_x, pos_y)
            else:
                litera = "Ż"
                end = (pos_x, pos_y)
            matrix[pos_y][pos_x] = litera
            placed += 1

    return [matrix, start, end]

def can_place_obstacle(matrix, row_idx, col_idx): # if true placed if false not placed
    if matrix[row_idx][col_idx] == " ":
        matrix[row_idx][col_idx] = "X"
        return True
    
    else:
        return False


def BFS(matrix: list[list], start: set, end: set):
    #wartosciami sa krotki wspolrzedych (i,j)
    visited = {start}
    parent = {start: None}
    kolejka = [start]

    while kolejka != []:
        node = kolejka[0]
        kolejka.pop(0)

        if node == end:
            # Odtwarzanie ścieżki
            path = []
            curr = end
            while curr is not None:
                path.append(curr)
                curr = parent[curr]
            return path[::-1]
        
        for i in get_neighbors(matrix, node):
            if i not in visited:
                visited.add(i)
                parent[i] = node
                kolejka.append(i)

    return None
        

        
    
def get_neighbors(matrix, node):          #(x,y)
    max_index = len(matrix)-1
    possible_moves = [(-1,0), (1,0), (0,1), (0,-1)]

    current_x, current_y = node
    all_moves = []
    for i in possible_moves:
        dx,dy = i
        all_moves.append((current_x+dx, current_y+dy))


    #sprawdzanie poprawnosci
    result = []
    for i in all_moves:
        x,y = i
        if (0 <= x <= max_index) and (0 <= y <= max_index):
            if matrix[y][x] != "X":
                result.append(i)

    return result

def visualize(matrix, solution_path):
    print("\033[H\033[J", end="")    #ekwiwalent cls

    for i in solution_path:
        x,y = i
        matrix[y][x] = "0"
        view_matrix(matrix)
        time.sleep(0.2)
        print("\033[H", end="")


    for i in solution_path:
        x,y = i
        matrix[y][x] = "1"
        view_matrix(matrix)
        time.sleep(0.2)
        print("\033[H", end="")

    

if __name__ == "__main__":
    matrix = generate_matrix(25)
    start = ()
    end = ()
    matrix, start, end = generate_random_obstacles(matrix)
    matrix 

    print("\033[H\033[J", end="")
    view_matrix(matrix)

    kolejka = BFS(matrix,start,end)

    if kolejka != None:
        kolejka = kolejka[1:-1]
        time.sleep(2)
        while True:
            visualize(matrix, kolejka)




