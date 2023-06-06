from interpreter import draw
from chessPictures import *
from picture import *

# Definir las imágenes de las piezas y los cuadros
pieces = [rock, knight, bishop, king, queen, bishop, knight, rock]
pawn = Picture(PAWN)
square = Picture(SQUARE)

# Construir la primera fila del tablero con una roca y cuadros intercalados
row = rock.up(square)

for i in range(1, 8):
    sq = square
    if i % 2 != 0:
        sq = square.negative()

    img = pieces[i].up(sq)
    row = row.join(img)

row_negative = row.negative()

# Construir la fila de peones negros
row_P = pawn.up(square.negative())

for i in range(1, 8):
    sq = square
    if i % 2 == 0:
        sq = square.negative()

    img = pawn.up(sq)
    row_P = row_P.join(img)

row_P_negative = row_P.negative()

# Construir una fila vacía de cuadros
row_Empty = square

for i in range(1, 8):
    sq = square
    if i % 2 != 0:
        sq = square.negative()

    row_Empty = row_Empty.join(sq)

row_Empty_negative = row_Empty.negative()

# Construir una fila con bloques alternados de cuadros vacíos y negativos
row_Block = row_Empty

for i in range(1, 4):
    if i % 2 != 0:
        row_Block = row_Block.under(row_Empty_negative)
    else:
        row_Block = row_Block.under(row_Empty)

# Construir el tablero completo
board = row
board = board.under(row_P)
board = board.under(row_Block)
board = board.under(row_P_negative)
board = board.under(row_negative)

# Mostrar el tablero
draw(board)
