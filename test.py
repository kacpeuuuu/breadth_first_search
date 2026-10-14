matrix = [
[' ', 'X', ' ', ' ', ' ', 'X', 'X', 'X'],
['X', 'X', ' ', 'X', ' ', 'X', 'X', 'X'],
['Ż', ' ', ' ', ' ', ' ', 'X', 'X', ' '],
[' ', 'X', 'X', ' ', 'X', ' ', 'X', 'X'],
[' ', ' ', ' ', 'X', ' ', ' ', ' ', ' '],
['X', 'X', ' ', ' ', ' ', 'X', ' ', 'X'],
[' ', ' ', ' ', ' ', 'X', 'R', ' ', ' '],
[' ', ' ', 'X', ' ', ' ', 'X', ' ', 'X']
]

def get_neighbors(matrix, node):          #(x,y)
    max_index = len(matrix[0])-1
    possible_moves = [(-1,0), (1,0), (0,1), (0,-1)]

    all_moves = []
    for i in possible_moves:
        x,y = i
        current_x, current_y = node

        all_moves.append((current_x+x, current_y+y))

    result = []
    for i in all_moves:
        x,y = i
        if (0 <= x <= max_index) and (0 <= y <= max_index):
            result.append(i)

    return result


print(get_neighbors(matrix, (7,5)))
print(matrix[7][5])