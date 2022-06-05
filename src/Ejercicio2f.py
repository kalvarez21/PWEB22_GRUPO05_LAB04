from interpreter import draw
from chessPictures import *
fila = square.join(square.negative()).horizontalRepeat(4)
fila2 = square.negative().join(square).horizontalRepeat(4)
unirFilas = fila2.up(fila)
draw(unirFilas.verticalRepeat(2))
