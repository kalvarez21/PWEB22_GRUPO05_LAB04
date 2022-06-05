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
    return Picture(reflejoVertical)#Se retorna un objeto picture que contiene a la imagen invertida verticalmente


  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    imagenActual = self.img
    reflejoHorizontal = [] #Array auxiliar que contendra la imagen invertida horizontalmente (en cadenas)
    str = "" # variable String auxiliar
    for x in self.img:# Recorrera cada elemento String de imagenActual
      str = x[::-1] #Invierte la cadena x y lo almacena en str
      reflejoHorizontal.append(str)# Almacena la cadena str en el arrat reflejoHorizontal
    return Picture(reflejoHorizontal)#Se retorna un objeto picture que contiene a la imagen invertida horizontalmente


  def negative(self):
    """ Devuelve un negativo de la imagen """
    imagenNegativa = []#Array auxiliar que contendra la imagen negativa
    for x in range(len(self.img)):# Recorrera cada cadena de la imagen Actual
      str = "" #String auxiliar
      for y in self.img[x]: # Recorrera cada carater de la cadena
        str += self._invColor(y) #Convierte cada caracter a su inverso y lo concatena a str
      imagenNegativa.append(str) # cada cadena invertida lo añade en imagenNegativa
    return Picture(imagenNegativa)#Se retorna un objeto picture que contiene a la imagen negativa


  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento
        al lado derecho de la figura actual """
    imagenActual = self.img
    segundaImagen = p.img
    imagenesUnidas = [] #Array auxiliar que contendra la imagenes unidas (actual - secundaria)
    for x in range(len(self.img)):
      imagenesUnidas.append(imagenActual[x] + segundaImagen[x])#Concatena las cadenas x de los arrays imagenActual e segundaImagen
    return Picture(imagenesUnidas)#Se retorna un objeto picture que contiene a las imagenes unidas


  def up(self, p):
    """Devuelve una nueva figura poniendo la figura recibida
       como argumento, encima de la figura actual"""
    imagenActual = self.img
    imagenArriba = p.img
    imagenMontada = []
    imagenMontada.extend(imagenArriba) #Añade todas las cadenas de imagenArriba a la variable imagenMontada
    imagenMontada.extend(imagenActual) #Añade todas las cadenas de imagenActual a la variable imagenMontada
    return Picture(imagenMontada)#Se retorna un objeto picture que contiene a imagenArriba arriba de imagenActual 

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
