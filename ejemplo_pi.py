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

def visualizar_pi(n_puntos=10000):
    """Visualiza el método para estimar pi"""
    
    pi_est, x, y, dentro = estimar_pi(n_puntos)
    
    # Crear figura
    plt.figure(figsize=(10, 8))
    
    # Dibujar puntos
    plt.scatter(x[dentro], y[dentro], c='blue', s=1, alpha=0.5, label='Dentro del círculo')
    plt.scatter(x[~dentro], y[~dentro], c='red', s=1, alpha=0.5, label='Fuera del círculo')
    
    # Dibujar círculo
    theta = np.linspace(0, 2*np.pi, 100)
    plt.plot(np.cos(theta), np.sin(theta), 'k-', linewidth=2)
    
    plt.axis('equal')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Estimación de π = {pi_est:.6f} con {n_puntos} puntos')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('../imagenes/pi_visualizacion.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return pi_est

def analizar_convergencia():
    """Analiza la convergencia del método"""
    
    n_puntos_lista = [10, 100, 1000, 5000, 10000, 50000, 100000]
    estimaciones = []
    
    for n in n_puntos_lista:
        pi_est, _, _, _ = estimar_pi(n)
        estimaciones.append(pi_est)
    
    # Crear gráfica de convergencia
    plt.figure(figsize=(10, 6))
    plt.semilogx(n_puntos_lista, estimaciones, 'bo-', label='Estimación')
    plt.axhline(y=np.pi, color='r', linestyle='--', label='Valor real de π')
    plt.xlabel('Número de puntos (escala logarítmica)')
    plt.ylabel('π estimado')
    plt.title('Convergencia del método Montecarlo para π')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('../imagenes/pi_convergencia.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    return estimaciones

if __name__ == "__main__":
    # Ejecutar simulación principal
    print("=== Cálculo de π con Montecarlo ===")
    pi_est = visualizar_pi(10000)
    print(f"\nπ estimado: {pi_est:.6f}")
    print(f"Error absoluto: {abs(pi_est - np.pi):.6f}")
    print(f"Error relativo: {abs(pi_est - np.pi)/np.pi*100:.4f}%")
    
    # Analizar convergencia
    print("\n=== Análisis de Convergencia ===")
    analizar_convergencia()