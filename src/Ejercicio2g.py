from interpreter import draw
from chessPictures import *
# Fichas blancas
fichasEspecialesBlancas = rock.join(knight).join(bishop)
fichasEspecialesBlancas = fichasEspecialesBlancas.join(queen).join(king)
fichasEspecialesBlancas = fichasEspecialesBlancas.join(bishop).join(knight).join(rock)
peones = pawn.horizontalRepeat(8)
fichasBlancas = fichasEspecialesBlancas.up(peones)
#draw(fichasBlancas)

# Fichas Negras
fichasEspecialesNegras = fichasEspecialesBlancas.negative()
peonesNegros = peones.negative()
fichasNegras = peonesNegros.up(fichasEspecialesNegras)
#draw(fichasNegras)

# Par de Filas
fila = square.join(square.negative()).horizontalRepeat(4)
fila2 = square.negative().join(square).horizontalRepeat(4)
unirFilas = fila2.up(fila)
# draw(unirFilas)

# tablero
zonaFichasNegras = unirFilas.under(fichasNegras)
zonaFichasBlancas = unirFilas.under(fichasBlancas)
zonaMedia = unirFilas.verticalRepeat(2)
tablero = zonaFichasBlancas.up(zonaMedia).up(zonaFichasNegras)
draw(tablero)
