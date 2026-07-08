# Cálculo de π usando el Método Montecarlo

## 🎯 Objetivo

Estimar el valor de $\pi$ utilizando el método Montecarlo mediante el lanzamiento de puntos aleatorios en un cuadrado que contiene un círculo inscrito.

## 📐 Fundamentos Matemáticos

### Relación de Áreas

Consideremos un cuadrado de lado 2 y un círculo inscrito de radio 1:

- Área del cuadrado: $A_c = 4$
- Área del círculo: $A_o = \pi r^2 = \pi$

La probabilidad de que un punto aleatorio caiga dentro del círculo es:

$$
P = \frac{\text{Área del círculo}}{\text{Área del cuadrado}} = \frac{\pi}{4}
$$

Por lo tanto:

$$
\pi = 4 \times P \approx 4 \times \frac{\text{puntos dentro}}{\text{total de puntos}}
$$

## 🖥️ Implementación

### Código Python

```python
import numpy as np
import matplotlib.pyplot as plt

def estimar_pi(n_puntos):
    """Estima pi usando el método Montecarlo"""
    
    # Generar puntos aleatorios en [-1, 1] x [-1, 1]
    x = np.random.uniform(-1, 1, n_puntos)
    y = np.random.uniform(-1, 1, n_puntos)
    
    # Calcular distancia al origen
    distancias = np.sqrt(x**2 + y**2)
    
    # Contar puntos dentro del círculo
    dentro = distancias <= 1
    n_dentro = np.sum(dentro)
    
    # Estimar pi
    pi_estimado = 4 * n_dentro / n_puntos
    
    return pi_estimado, x, y, dentro

# Ejecutar simulación
n_puntos = 10000
pi_est, x, y, dentro = estimar_pi(n_puntos)

print(f"π estimado: {pi_est:.6f}")
print(f"Error: {abs(pi_est - np.pi):.6f}")