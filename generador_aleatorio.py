"""
Generador de números pseudoaleatorios
Método Congruencial Lineal
"""

import numpy as np
import matplotlib.pyplot as plt

class GeneradorCongruencial:
    """Generador de números pseudoaleatorios usando el método congruencial lineal"""
    
    def __init__(self, seed=12345, a=1103515245, c=12345, m=2**31):
        """
        Inicializa el generador
        
        Parámetros:
        seed: Semilla inicial
        a: Multiplicador
        c: Incremento
        m: Módulo
        """
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m
        self.actual = seed
    
    def next(self):
        """Genera el siguiente número pseudoaleatorio en [0, 1)"""
        self.actual = (self.a * self.actual + self.c) % self.m
        return self.actual / self.m
    
    def generar_secuencia(self, n):
        """Genera una secuencia de n números pseudoaleatorios"""
        return [self.next() for _ in range(n)]

def comparar_generadores():
    """Compara el generador congruencial con numpy.random"""
    
    # Generador personalizado
    gen = GeneradorCongruencial(seed=42)
    secuencia_personalizada = gen.generar_secuencia(10000)
    
    # Generador de numpy
    np.random.seed(42)
    secuencia_numpy = np.random.random(10000)
    
    # Visualizar comparación
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
    
    # Histogramas
    ax1.hist(secuencia_personalizada, bins=50, alpha=0.7, label='Generador personalizado')
    ax1.set_title('Histograma - Generador Congruencial')
    ax1.set_xlabel('Valor')
    ax1.set_ylabel('Frecuencia')
    
    ax2.hist(secuencia_numpy, bins=50, alpha=0.7, label='NumPy', color='orange')
    ax2.set_title('Histograma - NumPy')
    ax2.set_xlabel('Valor')
    ax2.set_ylabel('Frecuencia')
    
    # Dispersión de puntos consecutivos
    ax3.scatter(secuencia_personalizada[:-1], secuencia_personalizada[1:], 
               s=1, alpha=0.5)
    ax3.set_title('Dispersión - Generador Congruencial')
    ax3.set_xlabel('x_n')
    ax3.set_ylabel('x_{n+1}')
    
    ax4.scatter(secuencia_numpy[:-1], secuencia_numpy[1:], 
               s=1, alpha=0.5, color='orange')
    ax4.set_title('Dispersión - NumPy')
    ax4.set_xlabel('x_n')
    ax4.set_ylabel('x_{n+1}')
    
    plt.tight_layout()
    plt.savefig('../imagenes/comparacion_generadores.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    # Test del generador
    gen = GeneradorCongruencial(seed=42)
    print("Primeros 10 números generados:")
    for i in range(10):
        print(f"{i+1}: {gen.next():.6f}")
    
    # Comparar con NumPy
    print("\nComparando generadores...")
    comparar_generadores()