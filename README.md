# Weather Forecast Visualization Project 🌤️

Este proyecto realiza la **adquisición de datos meteorológicos** a través de la API de Open-Meteo y la **visualización de distintas variables climáticas** para el análisis exploratorio.

---

## 📁 Estructura del Proyecto

```
WEATHER-FORECAST-TOOL/
├── data/
│   └── datos_meteorologicos.csv
├── docs/
│   ├── heatmap_correlation.png
│   ├── temperatures_line.png
│   ├── rain_precipitation.png
│   ├── daily_sun.png
│   ├── uv_radiation.png
│   ├── wind_precipitation.png
│   └── analisis.md
├── src/
│   ├── get_data.py
│   ├── heatmap_correlation.py
│   ├── temperatures_line.py
│   ├── rain_precipitation.py
│   ├── daily_sun.py
│   ├── uv_radiation.py
│   ├── wind_precipitation.py
│   └── grafica_uv_radiacion.py
├── requirements.txt
└── .cache.sqlite
```

---

## ⚙️ Requisitos

Instala las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
```

---

## 🚀 Scripts disponibles

- `get_data.py`: descarga los datos meteorológicos desde la API y los guarda como archivo CSV.
- Los scripts en `src/` generan visualizaciones individuales y guardan las imágenes en `docs/`.

---

## 📊 Visualizaciones Generadas

- **Mapa de calor de correlación:** `heatmap_correlation.png`
- **Evolución diaria de temperatura:** `temperatures_line.png`
- **Precipitación diaria + probabilidad de lluvia:** `rain_precipitation.png`
- **Duración del día vs. horas reales de sol:** `daily_sun.png`
- **Radiación solar vs. índice UV:** `uv_radiation.png`
- **Precipitación vs. velocidad del viento:** `wind_precipitation.png`

Todas las imágenes se encuentran en la carpeta `docs/`.

---

## 📈 Análisis

Puedes consultar el análisis interpretativo de cada gráfica en:

👉 [`docs/analisis.md`](docs/analisis.md)

---

## 🛰️ Fuente de datos

Datos obtenidos a través de la [API de Open-Meteo](https://open-meteo.com/).

---

## 📌 Autor

Byron Velasco – 2025  
Maestría en Ciencia de Datos