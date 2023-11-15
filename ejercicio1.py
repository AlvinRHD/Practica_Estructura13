import pandas as pd
import matplotlib.pyplot as plt

data = {'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
        'Ventas': [5000, 6000, 7500, 9000, 8000]}
df = pd.DataFrame(data)

# Crear grafico de barras horizontales
plt.barh(df['Mes'], df['Ventas'], color='skyblue')
plt.xlabel('Ventas Totales')
plt.ylabel('Meses')
plt.title('Ventas Mensuales por Mes')
plt.grid(True)
plt.show()
