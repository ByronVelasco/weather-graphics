# src/grafica_viento_precipitacion.py
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
df = pd.read_csv("data/datos_meteorologicos.csv", parse_dates=["date"])

# Crear la figura y el eje principal
fig, ax1 = plt.subplots(figsize=(12, 6))

# Precipitación diaria como barras
ax1.bar(df["date"], df["precipitation_sum"], color='skyblue', label='Precipitación (mm)')
ax1.set_xlabel("Fecha")
ax1.set_ylabel("Precipitación (mm)", color='skyblue')
ax1.tick_params(axis='y', labelcolor='skyblue')

# Crear un segundo eje para la velocidad del viento
ax2 = ax1.twinx()
ax2.plot(df["date"], df["wind_speed_10m_max"], color='darkred', marker='o', linestyle='--', label='Vel. viento máx (km/h)')
ax2.set_ylabel("Velocidad del viento (km/h)", color='darkred')
ax2.tick_params(axis='y', labelcolor='darkred')

# Título y leyendas
plt.title("Precipitación diaria vs. velocidad del viento máxima")
fig.tight_layout()
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))
plt.grid(axis='x', linestyle='--', alpha=0.5)

# Guardar la imagen
plt.savefig("docs/wind_precipitation.png", dpi=300)