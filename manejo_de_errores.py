"""Errores comunes en Python
 while (no while True)
Error de condición infinita: usar while continuar == "si" pero nunca cambiar el valor de continuar.

Error de comparación: escribir = en vez de == → while continuar = "si" da SyntaxError.

Error de mayúsculas/minúsculas: while continuar == "si" pero el usuario escribe "Si" → no entra al bucle.

 if / elif / else
Indentación incorrecta: olvidar sangría → IndentationError.

Orden de condiciones: poner primero elif edad < 18 y luego if edad < 12 → nunca se ejecuta el segundo.

Uso incorrecto de elif: escribir else if en vez de elif → SyntaxError.
Diccionarios
Clave inexistente: acceder con diccionario["clave"] que no existe → KeyError.

Confusión entre métodos: usar .append() en un diccionario → AttributeError.

Sobrescribir valores: asignar dos veces la misma clave → se pierde el valor anterior.

 Listas
Índice fuera de rango: lista[10] cuando la lista tiene menos elementos → IndexError.

Tipo incorrecto: intentar sumar lista con número → TypeError.

Método mal escrito: usar .add() en vez de .append() → AttributeError.

 for
Iterar sobre tipo incorrecto: for x in 10: → TypeError porque 10 no es iterable.

Modificar lista mientras se recorre: puede dar resultados inesperados.

Olvidar : → SyntaxError.

.append()
Usar en tipos incorrectos: .append() solo funciona en listas, no en strings ni diccionarios.

Olvidar paréntesis: lista.append en vez de lista.append("dato") → no agrega nada.

 Variables
No definir antes de usar: print(x) sin haber definido x → NameError.

Confusión de tipos: sumar string con número → TypeError.

Sobrescribir variables: usar el mismo nombre para cosas distintas → resultados inesperados.

 Funciones
No usar def: escribir funcion() sin definirla → NameError.

Olvidar return: la función devuelve None aunque esperabas un valor.

Número incorrecto de argumentos: llamar con más o menos parámetros → TypeError.

 Operaciones básicas
División por cero: 10 / 0 → ZeroDivisionError.

Tipos incompatibles: "texto" - 5 → TypeError.

Confusión entre = y ==: usar = en comparaciones → SyntaxError."""