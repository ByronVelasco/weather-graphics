import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# ------------------ CARGA DE DATOS ------------------ #

# Ruta del CSV generado desde get_data.py
csv_path = "data/datos_meteorologicos.csv"
df = pd.read_csv(csv_path, parse_dates=["date"])

# Variables numéricas relevantes
variables = [
    "temperature_2m_max", "temperature_2m_min",
    "daylight_duration", "sunshine_duration",
    "uv_index_max", "precipitation_sum",
    "precipitation_probability_max", "shortwave_radiation_sum",
    "wind_speed_10m_max"
]

# Copiamos solo esas columnas
df_corr = df[variables].copy()

# Convertimos segundos a horas para mejor escala
df_corr["daylight_duration"] = df_corr["daylight_duration"] / 3600
df_corr["sunshine_duration"] = df_corr["sunshine_duration"] / 3600

# ------------------ HEATMAP ------------------ #

plt.figure(figsize=(12, 8))
sns.heatmap(
    df_corr.corr(),
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5,
    cbar_kws={"shrink": 0.8},
    square=True
)

plt.title("Mapa de calor: correlación entre variables meteorológicas", fontsize=14)
plt.tight_layout()

# ------------------ GUARDAR FIGURA ------------------ #

output_path = "docs/heatmap_correlation.png"
plt.savefig(output_path)
plt.close()

print(f"Gráfico guardado en: {output_path}")