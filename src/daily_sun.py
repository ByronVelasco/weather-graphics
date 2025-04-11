import pandas as pd
import matplotlib.pyplot as plt
import os

# Cargar los datos
df = pd.read_csv("data/datos_meteorologicos.csv", parse_dates=["date"])

# Convertir duración del día y del sol de segundos a horas
df["daylight_hours"] = df["daylight_duration"] / 3600
df["sunshine_hours"] = df["sunshine_duration"] / 3600

# Crear figura
plt.figure(figsize=(12, 6))
plt.plot(df["date"], df["daylight_hours"], label="Duración del día", linewidth=2, color="#FDB813")
plt.plot(df["date"], df["sunshine_hours"], label="Horas reales de sol", linewidth=2, color="#1F77B4", linestyle="--")
plt.fill_between(df["date"], df["sunshine_hours"], color="#1F77B4", alpha=0.1)

plt.xlabel("Fecha")
plt.ylabel("Horas")
plt.title("Duración del día vs. horas reales de sol")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Guardar imagen
output_path = "docs/daily_sun.png"
plt.savefig(output_path)
plt.close()

print(f"Gráfico guardado en: {output_path}")