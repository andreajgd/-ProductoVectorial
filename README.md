# Producto Vectorial y Fuerza Magnética sobre un Conductor

Este repositorio contiene la implementación de una función para calcular el producto vectorial entre dos vectores y su aplicación en el cálculo de la fuerza magnética que actúa sobre un conductor con corriente eléctrica dentro de un campo magnético.

## Descripción del proyecto

El proyecto tiene como objetivo resolver ejercicios relacionados con el producto vectorial y la fuerza magnética sobre un conductor.  
Para ello, se utiliza la fórmula:

F = I(L × B)

Donde:

- F es la fuerza magnética.
- I es la corriente eléctrica.
- L es el vector longitud del conductor.
- B es el campo magnético.
- × representa el producto vectorial.

## Objetivo

Implementar una función que permita calcular el producto vectorial de dos vectores y utilizar ese resultado para determinar la fuerza magnética causada por un campo magnético en diferentes escenarios.

## Fórmula del producto vectorial

Dados dos vectores:

A = (Ax, Ay, Az)  
B = (Bx, By, Bz)

El producto vectorial se calcula como:

A × B = (
AyBz - AzBy,
AzBx - AxBz,
AxBy - AyBx
)

## Fuerza magnética sobre un conductor

La fuerza magnética sobre un conductor se calcula mediante:

F = I(L × B)

Donde el vector L representa la dirección y longitud del conductor, y se obtiene a partir de dos puntos:

L = Q - P

Si el conductor une los puntos P y Q, entonces:

L = (Qx - Px, Qy - Py, Qz - Pz)

## Escenario de ejemplo

Para un conductor que une los puntos:

P = (-7, 4, 5)  
Q = (8, 0, -4)

y una corriente eléctrica:

I = 20 A

Primero se calcula el vector longitud:

L = Q - P

L = (8 - (-7), 0 - 4, -4 - 5)

L = (15, -4, -9)

Luego se utiliza la fórmula de la fuerza magnética:

F = I(L × B)

## Tecnologías utilizadas

- Lenguaje de programación utilizado en el proyecto
- Editor o IDE de desarrollo
- Conceptos de álgebra vectorial
- Conceptos básicos de electricidad y magnetismo

## Funcionalidades

- Cálculo del producto vectorial entre dos vectores.
- Obtención del vector longitud de un conductor.
- Aplicación de la fórmula de fuerza magnética.
- Resolución de escenarios físicos usando vectores.

## Estructura del proyecto

El repositorio puede organizarse de la siguiente manera:

producto-vectorial/
│
├── src/
│   └── main
│
├── README.md
└── ejercicios

## Cómo ejecutar el proyecto

1. Clonar el repositorio.
2. Abrir el proyecto en el editor o IDE correspondiente.
3. Ejecutar el archivo principal.
4. Ingresar o modificar los valores de los vectores según el escenario.
5. Obtener como resultado el producto vectorial y la fuerza magnética.

## Aprendizaje obtenido

Con este proyecto se refuerzan los conceptos de producto vectorial, vectores en tres dimensiones y fuerza magnética sobre un conductor. Además, permite relacionar la programación con la resolución de problemas de física aplicada.

## Autor

Proyecto académico desarrollado para practicar el cálculo del producto vectorial y su aplicación en la fuerza magnética sobre un conductor.

## Estado del proyecto

Proyecto en desarrollo con fines académicos.
