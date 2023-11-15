import pandas as pd
import matplotlib.pyplot as plt

fbk = ['Facebook', 2449, 2006]
twt = ['Twitter', 339,  2006]
ig = ['Instagram', 2449, 2006]
yt = ['Youtube', 339,  2006]
wsp = ['Whatssapp', 2449, 2006]

lista_redes = [fbk, twt, ig, yt, wsp]

df_redes = pd.DataFrame(lista_redes, columns=['Nombre', 'Cantidad', 'Año'])
df_redes

plt.plot(df_redes['Nombre'], df_redes['Cantidad'])
plt.show

plt.plot(df_redes['Nombre'], df_redes['Cantidad'])
plt.title('Diograma de lineas')
plt.xlabel('Redes')
plt.ylabel('Cantidad')
plt.show()


df_redes_ordenas = df_redes.sort_values('Cantidad', ascending=False)
plt.bar(df_redes_ordenas['Nombre'],
        df_redes_ordenas['Cantidad'], color=['r', 'g', 'b'])
plt.title('Diograma de lineas')
plt.xlabel('Redes')
plt.ylabel('Cantidad')
plt.show()

lista_colores = ['#3b5998', '#ff0000', '#25d366', '#8a3ab9', '#00acee']
plt.pie(df_redes_ordenas['Cantidad'],
        labels=df_redes_ordenas['Nombre'], colors=lista_colores)
plt.title('Grafico de lineas')
plt.show()
