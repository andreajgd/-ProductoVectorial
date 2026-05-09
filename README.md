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

-Escenario 1
<img width="907" height="165" alt="image" src="https://github.com/user-attachments/assets/09284a4d-d0a7-45f8-95c0-84f36161ef7f" />

-Escenario 2

<img width="898" height="186" alt="image" src="https://github.com/user-attachments/assets/04c394f0-1c39-42d4-a43b-75f897ecd1e9" />


## Tecnologías utilizadas

- Lenguaje de programación utilizado en el proyecto
-Python

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


## Aprendizaje obtenido

Con este proyecto se refuerzan los conceptos de producto vectorial, vectores en tres dimensiones y fuerza magnética sobre un conductor. Además, permite relacionar la programación con la resolución de problemas de física aplicada.

