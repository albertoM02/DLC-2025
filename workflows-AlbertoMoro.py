import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
file_path = 'Madera_daily_data.csv'
data = pd.read_csv(file_path)

# Asegurarse de que las columnas esperadas existen
if 'Date' not in data.columns or 'Close' not in data.columns:
    raise ValueError("El dataset debe contener columnas 'Date' y 'Close'.")

# Convertir la columna de fecha al formato datetime
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Filtrar filas con fechas inválidas
data = data.dropna(subset=['Date'])

# Ordenar el dataset por fecha
data = data.sort_values(by='Date')

# Graficar la evolución del precio con el tiempo
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Close'], label='Evolución del Precio', marker='o', linestyle='-')
plt.title('Evolución del Precio con el Tiempo')
plt.xlabel('Fecha')
plt.ylabel('Precio (Close)')
plt.grid(True)
plt.legend()

# Guardar la gráfica como una imagen PNG
output_path = 'evolucion_precio.png'
plt.savefig(output_path)
print(f'Gráfica guardada como {output_path}')

# Mostrar la gráfica por pantalla
#plt.show()
