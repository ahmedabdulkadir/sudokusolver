"""
Ahmed Abdulkadir, 26 August 2017
Sudoku Solver
"""

def initializeGrid():
    """
    initalizes the 9x9 playing grid with zeros
    """
    grid = []
    for row in range(9):
        grid.append([])
        for column in range(9):
            grid[row].append(0)
    return grid
