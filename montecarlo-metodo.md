# Método Montecarlo

## 📖 Introducción

El **Método Montecarlo** es una técnica computacional que utiliza números aleatorios para resolver problemas que podrían ser determinísticos en principio. Fue desarrollado durante el Proyecto Manhattan en la década de 1940 por Stanislaw Ulam y John von Neumann.

## 🧮 Fundamentos Teóricos

### Ley de los Grandes Números

El método se basa en la **Ley de los Grandes Números**, que establece que:

> La media de una muestra aleatoria de una variable aleatoria converge a su valor esperado a medida que el tamaño de la muestra tiende a infinito.

$$
\lim_{n \to \infty} \frac{1}{n} \sum_{i=1}^{n} X_i = E[X]
$$

### Teorema del Límite Central

El error de aproximación sigue una distribución normal:

$$
\bar{X}_n \sim N\left(\mu, \frac{\sigma^2}{n}\right)
$$

Donde:
- $\mu$ es la media poblacional
- $\sigma^2$ es la varianza
- $n$ es el tamaño de la muestra

## 🔢 Generación de Números Pseudoaleatorios

### Generador Congruencial Lineal

El método más común usa la fórmula:

$$
X_{n+1} = (aX_n + c) \mod m
$$

**Parámetros típicos:**

| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| a | 1103515245 | Multiplicador |
| c | 12345 | Incremento |
| m | 2^31 | Módulo |

### Ejemplo de generación en Python

```python
def generador_congruencial(seed, n, a=1103515245, c=12345, m=2**31):
    numeros = []
    x = seed
    for _ in range(n):
        x = (a * x + c) % m
        numeros.append(x / m)  # Normalizar a [0,1)
    return numeros