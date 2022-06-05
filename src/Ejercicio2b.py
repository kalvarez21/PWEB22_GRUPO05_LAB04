from interpreter import draw
from chessPictures import *
figura1 = knight.join(knight.negative())
figura2 = figura1.horizontalMirror()
draw(figura2.up(figura1))
