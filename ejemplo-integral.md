# Aproximación de Integrales Definidas con Montecarlo

## 🎯 Objetivo

Calcular la integral definida de una función utilizando el método Montecarlo, comparando diferentes enfoques y analizando la convergencia.

## 📐 Fundamentos Matemáticos

### Integral Definida

Dada una función $f(x)$ definida en el intervalo $[a, b]$, queremos calcular:

$$
I = \int_a^b f(x) dx
$$

### Método de Montecarlo

El método consiste en generar puntos aleatorios en el rectángulo $[a, b] \times [0, M]$, donde $M$ es un valor mayor que el máximo de $f(x)$ en $[a, b]$.

La probabilidad de que un punto caiga bajo la curva es:

$$
P = \frac{I}{M \cdot (b-a)}
$$

Por lo tanto:

$$
I \approx M \cdot (b-a) \cdot \frac{\text{puntos bajo la curva}}{\text{total de puntos}}
$$

## 🖥️ Implementación

### Función Ejemplo: $f(x) = x^2$ en $[0, 2]$

La integral exacta es:

$$
\int_0^2 x^2 dx = \left[\frac{x^3}{3}\right]_0^2 = \frac{8}{3} \approx 2.6667
$$

```python
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """Función a integrar"""
    return x**2

def montecarlo_integral(f, a, b, n_puntos):
    """Aproxima la integral usando Montecarlo"""
    
    # Encontrar máximo de la función
    x_vals = np.linspace(a, b, 1000)
    M = max(f(x_vals)) * 1.1  # Margen de seguridad
    
    # Generar puntos aleatorios
    x = np.random.uniform(a, b, n_puntos)
    y = np.random.uniform(0, M, n_puntos)
    
    # Evaluar función en los puntos x
    y_f = f(x)
    
    # Contar puntos bajo la curva
    bajo_curva = y <= y_f
    n_bajo = np.sum(bajo_curva)
    
    # Estimar integral
    area_rectangulo = M * (b - a)
    integral_est = area_rectangulo * n_bajo / n_puntos
    
    return integral_est, x, y, bajo_curva, M

# Parámetros
a, b = 0, 2
n_puntos = 10000

# Calcular integral
integral_est, x, y, bajo_curva, M = montecarlo_integral(f, a, b, n_puntos)
integral_exacta = 8/3

print(f"Integral exacta: {integral_exacta:.6f}")
print(f"Integral estimada: {integral_est:.6f}")
print(f"Error absoluto: {abs(integral_est - integral_exacta):.6f}")