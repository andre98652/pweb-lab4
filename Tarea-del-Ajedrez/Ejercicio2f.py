from interpreter import draw
from chessPictures import *


square_white = Picture(SQUARE)
square_black = square_white.changeColor('_', '#')

# Crea una fila con colores alternados, comenzando con un cuadro blanco
row_pattern_white = square_white.join(square_black)
row_pattern_black = square_black.join(square_white)
row_white = row_pattern_white
row_black = row_pattern_black
for _ in range(1, 4):  # Repite el patrón de la fila tres veces más
    row_white = row_white.join(row_pattern_white)
    row_black = row_black.join(row_pattern_black)

# Alterna las filas para crear el patrón del tablero
board_pattern = row_white
for i in range(3):  # Repite el patrón de filas tres veces más
    board_pattern = board_pattern.under(row_black if i % 2 == 0 else row_white)
    

# Crea el tablero completo repitiendo el patrón de filas
board = board_pattern

draw(board)
