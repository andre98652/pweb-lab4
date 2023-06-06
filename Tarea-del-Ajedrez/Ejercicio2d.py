from interpreter import draw
from chessPictures import *

square_white = Picture(SQUARE)
square_black = square_white.changeColor('_', '#')

square_block = square_white.join(square_black)

for i in range(6):
    square_block = square_block.join(square_white if i % 2 == 0 else square_black)

draw(square_block)
