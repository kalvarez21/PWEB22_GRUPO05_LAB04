<table>
  <tbody>
   <tr>
   <td><img src="./imagenes/epis.png" alt="EPIS"></td>
   <th>
   <p>UNIVERSIDAD NACIONAL DE SAN AGUSTIN</p>
   <p>FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</p>
   <p>ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</p>
   </th>
   <td><img src="./imagenes/abet.png" alt="ABET"></td>
   </tr>
  </tbody>
</table>
<div align="center" dir="auto"><table>    
   <tbody>
   <tr><td colspan="3">Formato: Guía de Práctica de Laboratorio / Talleres / Centros de Simulación</td></tr>
   <tr><td>Aprobación:  2022/03/01</td><td>Código: GUIA-PRLD-001</td><td>Página: 1</td></tr>
   </tbody>
</table></div>
<div align="center" dir="auto">
   <span>INFORME DE LABORATORIO</span><br>
   <span>(formato estudiante)</span>
</div>
<div align="center" dir="auto"><table>
   <tbody><tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
   </tbody><tbody>
   <tr><td>ASIGNATURA:</td><td colspan="5">Programación Web 2</td></tr>
   <tr><td>TÍTULO DE LA PRÁCTICA: </td><td colspan="5">Python</td></tr>
   <tr>
   <td>NÚMERO DE PRÁCTICA:</td><td>04</td><td>AÑO LECTIVO:</td><td>2022 A</td><td>NRO. SEMESTRE:</td><td>III</td>
   </tr>
   <tr>
   <td>FECHA Presentacion:</td><td>05-Jun-2022</td><td>Hora de Presentacion:</td><td colspan="3">23:55</td>
   </tr>
   <tr><td colspan="3">Integrantes:
   <ul dir="auto">
   <li>Kevin Jheeremy Alvarez Astete</li>
   </ul>
   </td>
   <td> NOTA: </td>
   <td colspan="2"> </td>
   </tr><tr><td colspan="6">DOCENTES:
   <ul dir="auto">
   <li>Richart Smith Escobedo Quispe (rescobedoq@unsa.edu.pe)</li>
   </ul>
   </td>
</tr></tbody></table></div>
   <h1>SOLUCION Y RESULTADOS</h1>
   <h2>I. SOLUCION DE EJERCICIOS/PROBLEMAS</h2>
   <h3>EJERCICIO 01 : DESARROLLO DE FUNCIONES</h3> 
   
   - NOTA: En el archivo TestingFunciones.py podra probar el funcionamiento de cada una de las siguientes funciones
   - Funcion verticalMirror: Se basa en ir almacenando los Strings del array que contiene la imagen actual en otro, solo que se empieza desde el ultimo y se va retrocediendo.
  ```sh
    draw(knight.verticalMirror())
  ```
  <img src="https://i.ibb.co/5R8B2ft/caballo-Reflejo-Vertical.png">
  
  - Funcion HorizontallMirror: Se basa en invertir cada String del array que contiene la imagen actual e ir almacenandolos en otro. Ya que en python los Strings se comportan con arrays es posible usar el artilugio de la linea 32 para reducir el codigo [4]
  ```sh
    str = x[::-1]
  ```
  - Probando la funcion:
  ```sh
    draw(knight.horizontalMirror())
  ```
  <img src="https://i.ibb.co/KrS8vCn/caballo-Reflejo-Horizontal.png">
  	
  - Funcion negative: Se basa en evaluar cada uno de los caracteres y convertirlo en su inverso definido en el array inverter del archivo color.py. En caso de no encontrarse tal caracter en este array no se generara la conversion
  ```sh
    draw(knight.negative())
  ```
  <img src="https://i.ibb.co/xmyz8V0/caballo-Invertido.png">
  
  - Funcion join: Se basa en concatenar el String x de la imagen Actual con la segunda imagen.
  ```sh
    draw(knight.join(rock))
  ```
  <img src="https://i.ibb.co/jrN51py/caballo-Torre-Unidos.png">
  
  - Funcion up: Se basa en almacenar en un array auxiliar primero todos los elementos del array de la segunda imagen y luego los de la imagen actual
  ```sh
    draw(knight.up(rock))
  ```
  <img src="https://i.ibb.co/QfqkTZ9/torre-Arriba-Caballo.png">
  
  - Funcion under: Se basa en evaluar cada caracter de la segunda imagen, en caso de que sea un espacio vacio se reemplaza con el caracter en la misma posicion de la  imagen actual, caso contrario se mantiene el caracter de la segunda imagen intacta.
  ```sh
    draw(square.under(knight)) #caballo sobre la casilla
  ```
  <img src="https://i.ibb.co/G0N3Yw2/caballo-Sobre-Casilla.png">
  
  - Funcion horizontalRepeat: En python el operador * tambien trabaja con strings, haciendo que se repita las veces que uno desea. Para esta funcion se uso este operador en cada cadena de la imagen actual para luego almacenarlas  
  ```sh
    draw(knight.horizontalRepeat(5))
  ```
  <img src="https://i.ibb.co/bB1typ6/caballo-Repetido-H.png">
  
  - Funcion verticalRepeat: Se basa en almacenar n veces el conjunto de arrays de la imagen actual en un array auxiliar
  ```sh
    draw(knight.verticalRepeat(5))
  ```
  <img src="https://i.ibb.co/TmwnzBw/caballo-Repetido-V.png">
  
  - Funcion rotateAntihorario: Se basa en concatenar todos los caracteres de la columna x (iniciando en la primera fila)y almacenarlos en un array auxliar. El recorrido de las columnas se hara desde el ultimo al primero.
  - Funcion rotateHorario: Se basa en concatenar todos los caracteres de la columna x (iniciando desde la ultima fila)y almacenarlos en un array auxliar. El recorrido de las columnas se hara desde el primero al ultimo.
  ```sh
      draw(knight.rotateAntihorario().join(knight.rotateHorario()))
  ```
  <img src="https://i.ibb.co/FqfPLbN/caballos-Rotados.png">
  
  <h3>EJERCICIO 02: RESOLUCION</h3> 
  - FIGURA a: figura1 contendra el caballo blanco unido al caballo negro. figura2 contendra el caballo negro unido al caballo blanco. Se finalizara dibujando figura1 sobre figura2.
  
  ```sh
  figura1 = knight.join(knight.negative())
  figura2 = knight.negative().join(knight)
  draw(figura2.up(figura1))
  ```
  <img src="https://i.ibb.co/kBRzGjS/figura2a.png">
  
  - FIGURA b: figura1 contendra el caballo blanco unido al caballo negro. figura2 contendra el reflejo horizontal de figura1 . Se finalizara dibujando figura1 sobre figura2.
  
  ```sh
  figura1 = knight.join(knight.negative())
  figura2 = figura1.horizontalMirror()
  draw(figura2.up(figura1))
  ```
  <img src="https://i.ibb.co/RBZ1JP3/figura2b.png">
  
  - FIGURA c: Reinas contendra las 4 reinas. Se finaliza dibujando reinas.
  
  ```sh
  reinas = queen.horizontalRepeat(4)
  draw(reinas)
  ```
  <img src="https://i.ibb.co/LrWrnzB/figura2c.png">
  
  - FIGURA d: fila contendra la union de una casilla blanca y una negra repetida 4 veces
  
  ```sh
  fila = square.join(square.negative()).horizontalRepeat(4)
  draw(fila)
  ```
  <img src="https://i.ibb.co/Wsss6N0/figura2d.png">
  
  - FIGURA e: fila2 contendra la union de una casilla negra y una blanca repetida 4 veces
  
  ```sh
  fila2 = square.negative().join(square).horizontalRepeat(4)
  draw(fila2)
  ```
  <img src="https://i.ibb.co/n6gzKv8/figura2e.png">
  
  - FIGURA f: fila contendra la figurad y fila2 contendra la figurae. unirFilas contendra fila arriba de fila2. Se finaliza dibujando unirFilas repetida verticalmente 2 veces 
  
  ```sh
  fila = square.join(square.negative()).horizontalRepeat(4)
  fila2 = square.negative().join(square).horizontalRepeat(4)
  unirFilas = fila2.up(fila)
  draw(unirFilas.verticalRepeat(2))
  ```
  <img src="https://i.ibb.co/WKhPJyv/figura2f.png">
  
  - FIGURA g: El ejercicio se dividio en pasos:
    - Fichas blancas: Se prepara la imagen que contendra todas las fichas blancas. Para ello en fichasEspecialesBlancas se almacena las fichas que no sean peones segun el orden establecido uniendoles con la funcion join. En peones se almaacenara la figura pawn(peon) repetida 8 veces. Por ultimo en fichasBlancas se juntaran todas las fichas colocando peones arriba de fichasEspecialesBlancas.
    - Fichas Negras: Se prepara la imagen que contendra todas las fichas negras. Para ello en fichasEspecialesNegras se almacena fichasEspecialesBlancas pero con el color invertido. En peonesNgros se almacena peones pero con el color invertido. Por ultimo en fichasNegras se juntaran todas las fichas colocando fichasEspecialesNegras arriba de peonesNegros.
    - Par de fila: Se repite el paso hecho para obtener unirFilas en el ejercicioF. 
    - Tablero: Se divide en tres zonas necesarias para su formacion: zonaFichasNegras, zonaFichasBlancas y zonaMedia.
      - ZonaFichasNegras: Se coloca fichasNegras encima de unirFilas.
      - ZonaFichasBlancas: Se coloca fichasBlancas encima de unirFilas
      - ZonaMedia : Se repite verticalmente unirFilas 2 veces.
    - Se finaliza juntando ZonaFichasNegras arriba de zonaMedia, y esta nueva imagen formada arriba de ZonaFichasBlancas. Luego se procede a dibujar.
  
  ```sh
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
  ```
  <img src="https://i.ibb.co/74HH6JT/figura2g.png">
  
  
  
   <h2>II. SOLUCION DE CUESTIONARIO</h2>
   
   - ¿Qué son los archivos .pyc?
     - A pesar de que Python es un lenguaje interpretado puede compilar ciertos paquetes incluidos en un programa de Python cuando se ejecuta el programa, lo que aumenta la velocidad de ejecución y la eficiencia. Esto demuestra muchas ventajas siempre que el código fuente del módulo no cambie, por lo que el intérprete de Python no interpretara el módulo cada vez que un programa se ejecuta. Más bien, se utilizará la versión "listo" del código. Esto disminuye la sobrecarga utilizado por interpretación continua de los mismos archivos de origen.
   - ¿Para qué sirve el directorio pycache?
     - Cuando se compila un archivo de python, el producto lo guarda en esta carpeta en formato de codigo de bytes. Por ejemplo, durante la resolucion de este laboratorio, los distintos archivos que se utlizaron (tales como picture.py) tienen su archivo compilado almacenado en esta carpeta con la terminacion *.cpython-39.pyc. Ejemplo: picture.cpython-39.pyc 
   - ¿Cuáles son los usos y lo que representa el subguión en Python?
     - El intérprete python almacena el valor de la última expresión usada en una variable especial llamada _. Por ejemplo, utilizando el interpretante en modo interactivo: 
     ```sh
      Python 2.7.13 (default, Jan 19 2017, 14:48:08)
      [GCC 6.3.0 20170118] on linux2
      Type "help", "copyright", "credits" or "license" for more information.
      >>> 5
      5
      >>> _
      5
      >>> _ * 3
      15
      >>> _
      15
      >>> _ + 7
      22
      >>> _
      22
     ```
     - Se puede utilizar el guión bajo para separar los dígitos de los números para lograr una mayor legibilidad.
     ```sh
      x_dec = 6_543_210
      y_hex = 0x_1234_abcd # 0x es el prefijo para indicar que es un numero hexadecimal

      print(x_dec) # 6543210
      print(y_hex) # 305441741
     ```
     
     - El _ se puede utilizar como un nombre desechable. Si no necesitas algunos valores específicos o si los valores no se utilizan, sólo hay que asignar los valores al guión bajo y estos valores serán ignorados. Por ejemplo:
     ```sh
      # Ignorar un valor al desempaquetar
      x, _, y = (1, 2, 3)
      print(x) # x = 1
      print(y) # y = 3

      # Desempaque extendido: ignora varios valores. Disponible solo en Python 3.x
      x, *_, y = (1, 2, 3, 4, 5)
      print(x) # x = 1
      print(y) # y = 5
     ```
     
     - El _ se puede utilizar como un nombre desechable. Si no necesitas algunos valores específicos o si los valores no se utilizan, sólo hay que asignar los valores al guión bajo y estos valores serán ignorados. Por ejemplo:
     ```sh
      # Ignorar un valor al desempaquetar
      x, _, y = (1, 2, 3)
      print(x) # x = 1
      print(y) # y = 3

      # Desempaque extendido: ignora varios valores. Disponible solo en Python 3.x
      x, *_, y = (1, 2, 3, 4, 5)
      print(x) # x = 1
      print(y) # y = 5
     ```
     
     - El guión bajo es más utilizado en "nombrar" variables o funciones. Por el PEP8, que es la guía de convenciones recomendadas para Python, se indican los siguientes 3 casos de nomenclatura:
       - Un solo guión bajo Después de un nombre (por ejemplo spam_) : Evita conflictos con keywords de Python
       - Un solo guión bajo Antes de un nombre (por ejemplo _spam) : Un convencion utilizada para indicar que la variable es privada o interna
       - Un doble guión bajo Antes y Después de un nombre (por ejemplo __spam__) : Indican que un metodo es especial, por ejemplo, el metodo __init__ usado en este laboratorio

   <h2>III. CONCLUSIONES</h2>
   <ul>
      <li>Python es un lenguaje facil de aprender e ideal para aquellos programadores que se estan iniciando. Este lenguaje de programación permite una diversidad de desarrollo de una manera fácil, ágil y rápida.</li>
      <li>Python presenta funciones que facilitan mucho el manejo de Strings y Arrays</li>
  
   </ul>
   <h1>RETROALIMENTACION GENERAL</h1>
   <h1>REFERENCIA Y BIBLIOGRAFIA</h1>
   <b><i>[1] https://www.w3schools.com/python/python_reference.asp</i></b><br>
   <b><i>[2] https://docs.python.org/3/tutorial/</i></b><br>   
   <b><i>[3] https://es.stackoverflow.com/questions/225847/como-instalar-pygame-en-python3-con-pip</i></b><br>  
   <b><i>[4] https://stackoverflow.com/questions/3940128/how-to-reverse-a-list</i></b>
   <b><i>[5] https://www.pythonmania.net/es/2017/03/05/guion-bajo-en-python/</i></b>
   
#

[downloads]: https://img.shields.io/github/downloads/rescobedoq/pw2/total?label=Downloads
[releases]: https://github.com/rescobedoq/pw2/releases/

[last-commit]: https://img.shields.io/github/last-commit/rescobedoq/pw2?label=Last%20Commit

[Debian]: https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white
[debian-site]: https://www.debian.org/index.es.html

[Git]: https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[git-site]: https://git-scm.com/

[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
[github-site]: https://github.com/

[Vim]: https://img.shields.io/badge/VIM-%2311AB00.svg?style=for-the-badge&logo=vim&logoColor=white
[vim-site]: https://www.vim.org/

[Java]: https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white
[java-site]: https://docs.oracle.com/javase/tutorial/


[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Java][Java]][java-site]


[![License][license]][license-file]
[![Downloads][downloads]][releases]
[![Last Commit][last-commit]][releases]
