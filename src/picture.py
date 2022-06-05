from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    imagenActual = self.img #Se almacena el array de cadenas en imagenActual
    reflejoVertical = [] #Array auxiliar que contendra la imagen invertida verticalmente (en cadenas)
    max = len(self.img) - 1 #Contador auxiliar
    while max >= 0:
      reflejoVertical.append(imagenActual[max])#Almacena en reflejoVertical las cadenas de imagenActual empezando desde la ultima
      max -= 1
    return Picture(reflejoVertical)#Se retorna un objeto picture que contiene a la imagen invertida verticalmente (en cadenas)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    imagenActual = self.img
    reflejoHorizontal = [] #Array auxiliar que contendra la imagen invertida horizontalmente (en cadenas)
    str = "" # variable String auxiliar
    for x in self.img:# Recorrera cada elemento String de imagenActual
      str = x[::-1] #Invierte la cadena x y lo almacena en str
      reflejoHorizontal.append(str)# Almacena la cadena str en el arrat reflejoHorizontal
    return Picture(reflejoHorizontal)#Se retorna un objeto picture que contiene a la imagen invertida horizontalmente (en cadenas)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    return Picture(None)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento
        al lado derecho de la figura actual """
    return Picture(None)

  def up(self, p):
    return Picture(None)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    return Picture(None)

  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    return Picture(None)

  def verticalRepeat(self, n):
    return Picture(None)

  #Extra: Sólo para realmente viciosos
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)
