# codigo/generar_esquema.py
import os

import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 🔧 CREAR LA CARPETA imagenes SI NO EXISTE
os.makedirs('../imagenes', exist_ok=True)

def generar_esquema():
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Dibujar caja
    ax.add_patch(patches.Rectangle((0.1, 0.1), 0.8, 0.8, 
                                   fill=False, edgecolor='black', linewidth=2))
    
    # Etapas del método
    etapas = [
        (0.3, 0.7, "1. Definir\nel problema"),
        (0.3, 0.5, "2. Generar\nnúmeros aleatorios"),
        (0.3, 0.3, "3. Realizar\nsimulaciones"),
        (0.3, 0.1, "4. Analizar\nresultados"),
    ]
    
    for x, y, texto in etapas:
        ax.add_patch(patches.Rectangle((x-0.15, y-0.08), 0.3, 0.16, 
                                       fill=True, facecolor='lightblue', 
                                       edgecolor='black'))
        ax.text(x, y, texto, ha='center', va='center', fontsize=10)
    
    # Flechas
    ax.annotate('', xy=(0.3, 0.58), xytext=(0.3, 0.62),
                arrowprops=dict(arrowstyle='->', lw=2))
    ax.annotate('', xy=(0.3, 0.38), xytext=(0.3, 0.42),
                arrowprops=dict(arrowstyle='->', lw=2))
    ax.annotate('', xy=(0.3, 0.18), xytext=(0.3, 0.22),
                arrowprops=dict(arrowstyle='->', lw=2))
    
    # Caja de resultados
    ax.add_patch(patches.Rectangle((0.6, 0.1), 0.3, 0.8, 
                                   fill=True, facecolor='lightgreen', 
                                   edgecolor='black', alpha=0.3))
    ax.text(0.75, 0.5, "SOLUCIÓN\nAPROXIMADA", 
            ha='center', va='center', fontsize=14, fontweight='bold')
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('Esquema del Método Montecarlo', fontsize=16, fontweight='bold')
    
    plt.savefig('../imagenes/montecarlo_esquema.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    generar_esquema()