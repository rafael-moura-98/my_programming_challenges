"""
Estou seguindo esta ideia: Para cada posição, checar a linha, 
coluna e quadrado onde se encontra. adicionar todos os valores
em uma lista, e adicionar o primeiro valor não presente na
lista na posição.
"""

sudoku = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0], 
         [0, 9, 8, 0, 0, 0, 0, 6, 0], 
         [8, 0, 0, 0, 6, 0, 0, 0, 3], 
         [4, 0, 0, 8, 0, 3, 0, 0, 1], 
         [7, 0, 0, 0, 2, 0, 0, 0, 6], 
         [0, 6, 0, 0, 0, 0, 2, 8, 0], 
         [0, 0, 0, 4, 1, 9, 0, 0, 5], 
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]

def solve_sudoku(sudoku: list) -> list:
    line = list()
    col = list()
    square = list()

    for i, i_value in enumerate(sudoku):
        for j, j_value in enumerate(sudoku[i]):
            if j_value == 0:
                line = sudoku[i]
                for count in range(9):
                    if sudoku[count][j] != 0:
                        col.append(sudoku[count][j])
            
    print(line)
    print("aqui acaba a linha")
    print(col)

solve_sudoku(sudoku)

