import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """Función a integrar: f(x) = x²"""
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

def visualizar_integral(n_puntos=10000):
    """Visualiza el método para calcular integrales"""
    
    a, b = 0, 2
    integral_est, x, y, bajo_curva, M = montecarlo_integral(f, a, b, n_puntos)
    integral_exacta = 8/3
    
    # Crear figura
    plt.figure(figsize=(12, 8))
    
    # Curva de la función
    x_curve = np.linspace(a, b, 1000)
    y_curve = f(x_curve)
    plt.plot(x_curve, y_curve, 'r-', linewidth=2, label='f(x) = x²')
    
    # Puntos aleatorios
    plt.scatter(x[bajo_curva], y[bajo_curva], 
               c='blue', s=5, alpha=0.3, label='Bajo la curva')
    plt.scatter(x[~bajo_curva], y[~bajo_curva], 
               c='red', s=5, alpha=0.3, label='Sobre la curva')
    
    # Rectángulo de integración
    plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
    plt.axhline(y=M, color='black', linestyle='--', alpha=0.3)
    plt.axvline(x=a, color='black', linestyle='--', alpha=0.3)
    plt.axvline(x=b, color='black', linestyle='--', alpha=0.3)
    
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Integral de f(x) = x² en [0,2]\nEstimación = {integral_est:.4f}, Exacta = {integral_exacta:.4f}')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('../imagenes/integral_puntos.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return integral_est

def analizar_convergencia_integral():
    """Analiza la convergencia del método para integrales"""
    
    a, b = 0, 2
    integral_exacta = 8/3
    n_puntos_lista = [100, 500, 1000, 5000, 10000, 50000, 100000]
    estimaciones = []
    errores = []
    
    for n in n_puntos_lista:
        integral_est, _, _, _, _ = montecarlo_integral(f, a, b, n)
        estimaciones.append(integral_est)
        errores.append(abs(integral_est - integral_exacta))
    
    # Crear figura con dos subplots
    plt.figure(figsize=(12, 5))
    
    # Gráfica 1: Convergencia
    plt.subplot(1, 2, 1)
    plt.semilogx(n_puntos_lista, estimaciones, 'bo-', label='Estimación Montecarlo')
    plt.axhline(y=integral_exacta, color='r', linestyle='--', label='Valor exacto')
    plt.xlabel('Número de puntos (escala log)')
    plt.ylabel('Valor de la integral')
    plt.title('Convergencia de la estimación')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Gráfica 2: Error
    plt.subplot(1, 2, 2)
    plt.loglog(n_puntos_lista, errores, 'go-', label='Error absoluto')
    plt.loglog(n_puntos_lista, [1/np.sqrt(n) for n in n_puntos_lista], 
              'r--', label='$O(1/\sqrt{n})$')
    plt.xlabel('Número de puntos (escala log)')
    plt.ylabel('Error absoluto (escala log)')
    plt.title('Comportamiento del error')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('../imagenes/integral_convergencia.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return estimaciones

if __name__ == "__main__":
    # Ejecutar simulación principal
    print("=== Cálculo de Integral con Montecarlo ===")
    integral_est = visualizar_integral(10000)
    integral_exacta = 8/3
    print(f"\nIntegral exacta: {integral_exacta:.6f}")
    print(f"Integral estimada: {integral_est:.6f}")
    print(f"Error absoluto: {abs(integral_est - integral_exacta):.6f}")
    print(f"Error relativo: {abs(integral_est - integral_exacta)/integral_exacta*100:.4f}%")
    
    # Analizar convergencia
    print("\n=== Análisis de Convergencia ===")
    analizar_convergencia_integral()