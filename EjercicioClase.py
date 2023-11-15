import pandas as pd
import matplotlib.pyplot as plt
import random

# Generar datos aleatorios para ventas mensuales
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
         "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
ventas = [random.randint(1000, 5000) for i in range(12)]

# Crear un DataFrame de Pandas con los datos
df_ventas = pd.DataFrame({"Mes": meses, "Ventas": ventas})
df_ventas

# Paso 2: Realizar el análisis
mes_max_ventas = df_ventas[df_ventas["Ventas"] ==
                           df_ventas["Ventas"].max()]["Mes"].values[0]
mes_min_ventas = df_ventas[df_ventas["Ventas"] ==
                           df_ventas["Ventas"].min()]["Mes"].values[0]

# Paso 3: Crear un gráfico de líneas
plt.figure(figsize=(10, 6))
plt.plot(df_ventas["Mes"], df_ventas["Ventas"], marker='o',
         linestyle='-', color='b', label='Ventas Mensuales')

# Etiquetas y título
plt.xlabel("Mes")
plt.ylabel("Ventas")
plt.title("Ventas Mensuales a lo largo del Año")
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.tight_layout()
plt.show()
