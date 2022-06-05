from interpreter import draw
from chessPictures import *
figura1 = knight.join(knight.negative())
figura2 = knight.negative().join(knight)
draw(figura2.up(figura1))
