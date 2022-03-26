Al comienzo del código se define una lista (HANGMAN_PICS) con las distintas imágenes del ahorcado, formadas con código ascii. En la posición 0 se encuentra la imagen cuando se erró 0 veces a la letra, en la posición 1 cuando se erró 1 vez. Así sucesivamente hasta la posición 6.

La segunda variable es una lista de las palabras posibles para adivinar en el juego. Esta lista se formó a partir de un string de las palabras separadas por un espacio y utilizando la función split().

La primera función que se define es getRandom(wordList), que devuelve de forma aleatoria una palabra de una lista de palabras (wordList). Esta lista estará formada por las palabras posibles a adivinar en el juego.

La segunda función displayBoard(missedLetters, correctLetters, secretWord), en primer lugar, muestra en pantalla la imagen del ahorcado correspondiente, la cual depende de las veces que se erró (missedLetters). Debajo muestra las letras erradas. Luego define una variable string formada por un número de guiones que se corresponde con el número de letras que contiene la palabra a adivinar (secretWord). Por último, remplaza los guiones por las letras correctamente adivinadas y ese string se muestra en pantalla.

La tercera función definida getGuess(alreadyGuessed) devuelve la letra que el jugador ingresó. Además, controla que no se ingrese más de una letra, que no sea una letra ya ingresada previamente y que sea efectivamente una letra. Si el jugador ingresa una mayúscula se convierte a minúscula (guess = guess.lower()).

La última función definida playAgain() muestra en pantalla la pregunta si se quiere volver a jugar. Devuelve true si se ingresa por teclado cualquier string que empieze con la letra 'y'. Caso contrario devuelve false.

Después de la definción de funciones se definen las suguientes variables:
+ missedLetters y correctsLetter son strings formados por las letras erradas y adivinadas respectivamente. Incialmente son strings vacíos.
+ secretWord es la palabra adivinar, obtenida aleatoriamente de la lista 'word'.
+ gameIsDone es un booleano que si el juego finalizó es igual a true, caso contrario igual a false. Se vuelve verdadero cuando se ingresaron 6 letras incorrectas o si se adivinaron todas las correctas. Se vuelve false cuando el jugador contesta que quiere seguir jugando. Si es false lo de adentro del while seguirá ejecutandose.
+ guess es la última letra ingresada.
+ foundAllLetters es un booleano que si se ingresaron todas las letras correctas es igual a true, caso contrario igual a false.


Los niveles se definen con la longitud de la lista HANGMAN_PICS. Esta longitud da el número de intentos en el juego.

En el código del hangman no se repeta la PEP 8 debido a que los nombres de las variables no están en minúsculas y las palabras no están separadas por '_'. Por ejemplo, 'wordIndex' debería ser 'word_index'.