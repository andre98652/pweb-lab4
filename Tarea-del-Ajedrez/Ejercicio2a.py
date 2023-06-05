from pieces import *
from picture import *
from interpreter import draw
from colors import *

# Crear una instancia de la clase Picture con el caballo blanco
horse_white = Picture(KNIGHT)


horse_black = horse_white.changeColor('.', '@')
horse_combined = horse_black.join(horse_white)

horse_white2 = Picture(KNIGHT)
horse_black2 = horse_white.changeColor('.', '@')
horse_combined2 = horse_white2.join(horse_black2)

horse_block=horse_combined.under(horse_combined2)

draw(horse_block)