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
   <h3>DESARROLLO DE FUNCIONES</h3> 
   
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
  
   <h2>II. SOLUCION DE CUESTIONARIO</h2>
   <ul>
      <li>¿Qué son los archivos *.pyc?</li>
      <li>¿Para qué sirve el directorio pycache?</li>
      <li>¿Cuáles son los usos y lo que representa el subguión en Python?</li>
   </ul>
   <h2>III. CONCLUSIONES</h2>
   <ul>
      <li></li>
      <li></li>
   </ul>
   <h1>RETROALIMENTACION GENERAL</h1>
   <h1>REFERENCIA Y BIBLIOGRAFIA</h1>
   <b><i>[1] https://www.w3schools.com/python/python_reference.asp</i></b><br>
   <b><i>[2] https://docs.python.org/3/tutorial/</i></b><br>   
   <b><i>[3] https://es.stackoverflow.com/questions/225847/como-instalar-pygame-en-python3-con-pip</i></b><br>  
   <b><i>[4] https://stackoverflow.com/questions/3940128/how-to-reverse-a-list</i></b>

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
