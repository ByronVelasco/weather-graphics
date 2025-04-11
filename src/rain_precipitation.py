# src/precipitacion_lluvia.py
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el CSV generado por get_data.py
df = pd.read_csv("data/datos_meteorologicos.csv", parse_dates=["date"])

# Convertir segundos a milímetros y mantener porcentajes
df["precipitation_sum"] = df["precipitation_sum"].round(2)
df["precipitation_probability_max"] = df["precipitation_probability_max"].round(1)

# Crear gráfico de barras para precipitación y línea para probabilidad de lluvia
fig, ax1 = plt.subplots(figsize=(12, 6))

# Eje de precipitación (mm)
ax1.bar(df["date"], df["precipitation_sum"], color="skyblue", label="Precipitación (mm)")
ax1.set_ylabel("Precipitación (mm)", color="skyblue")
ax1.tick_params(axis="y", labelcolor="skyblue")

# Eje de probabilidad de lluvia (%)
ax2 = ax1.twinx()
ax2.plot(df["date"], df["precipitation_probability_max"], color="darkblue", linestyle="--", marker="o", label="Probabilidad de lluvia (%)")
ax2.set_ylabel("Probabilidad de lluvia (%)", color="darkblue")
ax2.tick_params(axis="y", labelcolor="darkblue")

# Título y leyendas
plt.title("Precipitación diaria y probabilidad de lluvia")
fig.tight_layout()
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))

# Guardar figura
plt.savefig("docs/rain_precipitation.png")
plt.close()