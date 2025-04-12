# Contexto de los Datos Meteorológicos

Este documento describe el contexto y las características del dataset utilizado en el proyecto `weather-analysis`, generado a partir de la API pública de [Open-Meteo](https://open-meteo.com).

---

## Ubicación Geográfica

- **Latitud:** -1.25  
- **Longitud:** -78.25  
Esta coordenada se ubica en la región central de Ecuador, cercana a la zona andina.

---

## Configuración de Zona Horaria

- **Parámetro utilizado:** `timezone=auto`  
  Esto permite que la API ajuste automáticamente los datos a la zona horaria local correspondiente a la ubicación seleccionada. En este caso, Ecuador Continental (UTC-5).

---

## Rango de Fechas

- **Fecha de inicio:** 10 de marzo de 2025  
- **Fecha de fin:** 10 de abril de 2025  
- Los datos corresponden a **intervalos diarios**.

---

## Variables Seleccionadas

| Variable                        | Descripción                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| `temperature_2m_max`           | Temperatura máxima diaria (a 2 metros del suelo)                           |
| `temperature_2m_min`           | Temperatura mínima diaria (a 2 metros del suelo)                           |
| `daylight_duration`            | Duración del día (en segundos)                                             |
| `sunshine_duration`            | Duración del sol directo (en segundos)                                     |
| `uv_index_max`                 | Índice UV máximo diario                                                    |
| `precipitation_sum`           | Precipitación total diaria (mm)                                            |
| `precipitation_probability_max` | Probabilidad máxima de precipitación (%)                                  |
| `shortwave_radiation_sum`     | Radiación solar de onda corta (MJ/m²)                                      |
| `wind_speed_10m_max`          | Velocidad máxima del viento a 10 metros (km/h)                             |

---

## Formato y Estructura

- Los datos fueron solicitados a través de la **URL base**:  
  `https://api.open-meteo.com/v1/forecast`
- Se solicitaron como **variables diarias** (`daily`) y fueron almacenados como archivo CSV.
- La columna `date` fue convertida automáticamente al tipo `datetime`.

---

## Propósito del Dataset

Estas variables permiten realizar análisis exploratorio, identificar relaciones meteorológicas, y visualizar patrones relevantes como lluvias, vientos, días nublados o radiación peligrosa.