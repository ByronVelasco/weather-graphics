import pandas as pd
import plotly.express as px

# Cargar los datos meteorológicos
df = pd.read_csv("data/datos_meteorologicos.csv", parse_dates=["date"])

# Crear gráfico de líneas para temperatura máxima y mínima
fig = px.line(
    df,
    x="date",
    y=["temperature_2m_max", "temperature_2m_min"],
    labels={
        "date": "Fecha",
        "value": "Temperatura (°C)",
        "variable": "Tipo"
    },
    title="Evolución diaria de la temperatura máxima y mínima",
    markers=True,
    template="plotly_white"
)

# Guardar como imagen (también puedes usar .show() para visualizar en HTML)
fig.write_image("docs/temperatures_line.png")

print("Gráfico guardado en docs/linea_temperaturas.png")