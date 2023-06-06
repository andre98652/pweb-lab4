from pieces import *
from picture import *
from interpreter import draw
from colors import *

# Crear una instancia de la clase Picture con el caballo blanco
queen_white = Picture(QUEEN)
queen_block = Picture(QUEEN)

for i in range(3):
    queen_block=queen_block.join(queen_white)

draw(queen_block)
