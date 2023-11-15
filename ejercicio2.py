import pandas as pd
import matplotlib.pyplot as plt

data = {'Examen1': [80, 90, 75, 85, 95],
        'Examen2': [70, 85, 80, 90, 88]}
df = pd.DataFrame(data)

# Crear grafico de areas
plt.fill_between(df.index, df['Examen1'],
                 df['Examen2'], color='skyblue', alpha=0.4)
plt.plot(df['Examen1'], label='Examen 1', marker='o')
plt.plot(df['Examen2'], label='Examen 2', marker='o')

plt.xlabel('Estudiantes')
plt.ylabel('Puntajes')
plt.title('Relación entre Puntajes de Examen 1 y Examen 2')
plt.legend()
plt.grid(True)
plt.show()
