from interpreter import draw
from chessPictures import *

square_white = Picture(SQUARE)
square_black = square_white.changeColor('_', '#')

square_block = square_black.join(square_white)

for i in range(6):
    square_block = square_block.join(square_black if i % 2 == 0 else square_white)

draw(square_block)
