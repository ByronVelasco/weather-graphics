import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Cargar los datos
df = pd.read_csv("data/datos_meteorologicos.csv", parse_dates=["date"])

# Crear figura
fig, ax1 = plt.subplots(figsize=(12, 6))

# Primer eje Y: radiación solar
color_radiacion = 'darkorange'
ax1.set_xlabel("Fecha")
ax1.set_ylabel("Radiación solar (kWh/m²)", color=color_radiacion)
ax1.plot(df["date"], df["shortwave_radiation_sum"], color=color_radiacion, marker="o", label="Radiación solar")
ax1.tick_params(axis='y', labelcolor=color_radiacion)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax1.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
plt.xticks(rotation=45)

# Segundo eje Y: índice UV
ax2 = ax1.twinx()
color_uv = 'purple'
ax2.set_ylabel("Índice UV máximo", color=color_uv)
ax2.plot(df["date"], df["uv_index_max"], color=color_uv, linestyle="--", marker="x", label="Índice UV")
ax2.tick_params(axis='y', labelcolor=color_uv)

# Título y guardado
plt.title("Relación entre radiación solar e índice UV diario")
plt.tight_layout()
plt.savefig("docs/uv_radiation.png")