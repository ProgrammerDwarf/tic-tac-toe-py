# Proyecto: Tres en Raya (Tic-Tac-Toe) o 'La vieja'

Este proyecto fue desarrollado como parte del curso **Python Essentials 1** de la plataforma **Edube.org**. El objetivo era construir un juego de Tres en Raya, o como dice el título haciendo alusión a cómo se le llama a este juego en mi país "La vieja", funcional contra la computadora, aplicando los conceptos fundamentales de Python aprendidos durante el módulo.

## Descripción del Proyecto

El programa implementa un juego de Tres en Raya simplificado con las siguientes reglas:
* La computadora juega con el símbolo 'X'.
* El usuario juega con el símbolo 'O'.
* La computadora siempre realiza el primer movimiento, colocando su 'X' en el centro del tablero.
* El usuario ingresa sus movimientos seleccionando el número de la casilla (1-9).
* La computadora elige sus siguientes movimientos de forma aleatoria entre las casillas disponibles.
* El juego termina cuando un jugador gana o cuando el tablero se llena, resultando en un empate.

## Análisis y Abordaje del Problema

Mi proceso para abordar el problema fue realmente iterativo, trabajando un paso a la vez no solo sobre el programa que estaba construyendo sino con mi propio esquema de cómo tenía que construirse el juego.
En reiteradas ocasiones tuve que volver a iniciar desde 0, agarrar el lapiz y el papel y poner mis ideas en un esquema o mapa mental para abordar el problema en objetivos más pequeños y alcanzables.

### 1. Estructura Inicial y Planificación

Mi primer paso fue intentar entender los requisitos y desglosar el problema en partes más pequeñas y manejables. Utilicé la estructura de funciones provista por el enunciado como esqueleto para iniciar la construcción del programa:

- `display_board(board)`: Para mostrar el tablero. 
- `make_list_of_free_fields(board)`: Para saber qué casillas están disponibles. 
- `draw_move(board)`: Para gestionar la jugada de la computadora.
- `enter_move(board)`: Para gestionar la jugada del usuario.
- `victory_for(board, sign)`: Para verificar si alguien ha ganado.

### Detalles de mis acciones durante la creación del sistema

Inicialmente, llené las funciones en las que no estaba trabajando con la instrucción `pass` para poder enfocarme en una sola tarea a la vez sin generar errores. También definí constantes globales como `PLAYER_SYMBOL` y `COMPUTER_SYMBOL` para hacer el código más legible y fácil de mantener.

### 2. Representación del Tablero y Flujo Principal

Decidí representar el tablero como una lista de listas (`board[fila][columna]`), lo que me permitió un acceso a cada casilla.
Creé la función `board_creation()` para inicializar el tablero con los números del 1 al 9.

El flujo principal del juego lo encapsulé en un bucle `while True:`, el cual me pareció más limpio que un `while` con múltiples condiciones, como por ejemplo: Evaluar si el valor del llamado de la función `victory_for` para cualquiera de los jugadores daba true o si el máximo de turnos fue alcanzado. La salida del bucle la manejé explícitamente con `break`, es decir, cuando se cumple una condición de victoria o empate se interrumpirá el flujo del código y saldré del ciclo para culminar con el programa. La alternancia de turnos se maneja con una variable `turn_counter`, usando la paridad (par/impar) para decidir si mueve el jugador o la computadora.

### 3. Funciones Clave y Desafíos de Implementación

#### `make_list_of_free_fields()`
Al comienzo, intenté recorrer el tablero pero luego de varios intentos fallidos me di cuenta de que necesitaba los **índices** (coordenadas) de las casillas libres y yo estaba cometiendo el error de recorrerlos por valor. El punto clave aquí fue el uso de `range(len(board))` para iterar por índice, lo que me dio el control necesario para crear la lista de tuplas `(fila, columna)`. También modifiqué la función para que retornara la lista, en lugar de modificar una variable global, haciendo el código más predecible.

#### `enter_move()`
Esta función cambió un montón a lo largo del ejercicio y me dió más de un dolor de cabeza. Mi versión inicial era muy simple, y lo largo del ejercicio me di cuenta de que necesitaba un ciclo para que el flujo volviese al inicio en caso de que el usuario no ingresara la data correcta. Para eso implementé un bucle `while True:` que no termina hasta que el usuario introduce una jugada válida. Dentro de este, utilicé un bloque `try-except ValueError` para captar entradas no numéricas. Además, agregué validaciones para asegurar que el número estuviera en el rango (1-9) y, gracias a la reutilización de `make_list_of_free_fields()`, pude verificar de forma elegante si la casilla seleccionada ya estaba ocupada.

#### `victory_for()`
Esta función me generó una grata alegría ya que no tuve que equivocarme tanto para culminarla (-risa nerviosa-), lo cual fue un reto muy gratificante. La clave acá fue definir una lista con todas las 8 combinaciones de victoria. Luego, con un bucle anidado, la función itera sobre cada combinación y cuenta los símbolos del jugador actual. Si el contador llega a 3, la función retorna `True` inmediatamente. Durante las pruebas, llegué a pensar que había encontrado un bug, pero al analizar la secuencia de jugadas, me di cuenta de que el programa había detectado correctamente una victoria legítima de la computadora, lo que me sirvió para validar que mi lógica era sólida.

#### `display_board()`
Este fue el desafío final. Mi objetivo era replicar exactamente el formato visual del enunciado. Cabe destacar que al paralelo de este curso también estuve leyendo libros de Python como "Automate the Boring Stuff with Python, 2nd Edition: Practical Programming for Total Beginners" y "Python Crash Course, 2nd Edition: A Hands-On, Project-Based Introduction to Programming", allí noté que se usan herramientasm entiendo que yo que son más avanzadas, como los *f-strings* o el mini-lenguaje de formato del método `.format()`, estas opciones las descarté por considerar que estaban fuera del alcance de "Python Essentials 1". La solución más coherente y que, para mí, estaban en este nivel fue usar el método de string **`.center()`**. Esto me permitió calcular automáticamente los espacios necesarios para centrar cada símbolo o número en su celda, combinándolo con la concatenación (`+`) para construir cada línea del tablero.

```python
# Ejemplo de la línea clave en display_board
line_with_values = "|" + str(row_values[0]).center(7) + "|" + str(row_values[1]).center(7) + "|" + str(row_values[2]).center(7) + "|"
print(line_with_values)
```
Esta solución la percibí como sólida, legible y demuestra el uso de las herramientas fundamentales de Python para el formato de texto.

## Decisiones de Diseño Clave

* **Responsabilidad Única:** Cada función fue diseñada para hacer una sola cosa bien. Por ejemplo, `draw_move` solo se encarga de realizar el movimiento de la computadora. Pero para llegar a esta conclusión tuve que revisar varias veces el flujo del programa, debido a  que al comienzo había escrito condicionales dentro de esta función para manejar la diferencia del primer turno de la computadora de los subsecuentes, pero luego me dí cuenta que esta decisión pertenece al flujo general del programa y no de esta función.
* **Reutilización de Código:** `make_list_of_free_fields` es utilizada tanto por `enter_move` (para validar la jugada) como por `draw_move` (para elegir una casilla).
* **Gestión de Estado:** Mantuve el `board` y el `turn_counter` como el estado global del juego, mientras que otras variables (como la lista de casillas libres o la jugada del usuario) se mantuvieron locales a sus respectivas funciones.

## Cómo Ejecutar el Juego

Para jugar, simplemente ejecuta el script de Python desde una terminal:
```sh
python la_vieja.py
```
Sigue las instrucciones en pantalla para introducir el número de la casilla en la que deseas jugar.

## Conclusiones y Aprendizajes

Este proyecto fue fundamental para solidificar mi comprensión de la programación en Python. Más allá de la sintaxis, aprendí a pensar de forma algorítmica, a depurar mi propio código siguiendo la lógica paso a paso, y a considerar la importancia de escribir código modular y empezar a documentar el código que escribo para asentar las bases aprendidas. Los desafíos más fuertes, como el formato del tablero o la validación de la entrada, me obligaron a investigar e indagar por mi cuenta y a usar las herramientas del lenguaje de una manera más creativa y eficiente.

Espero que les haya gustado y cualquier crítica es bienvenida.
