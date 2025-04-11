# Análisis de Gráficas - Datos Meteorológicos

Este archivo contiene un breve análisis de las principales visualizaciones generadas a partir de datos meteorológicos obtenidos vía API.

---

## 1. Mapa de calor de correlación

El mapa de calor permitió identificar relaciones entre las variables meteorológicas. Por ejemplo, la temperatura máxima tiene alta correlación con la radiación solar y con la duración del sol. También se observa que la precipitación tiene una correlación negativa con la duración del sol.

---

## 2. Precipitación diaria vs. probabilidad de lluvia

Esta gráfica muestra una relación general entre mayor probabilidad de lluvia y mayor precipitación. Se observan días con alta probabilidad y baja precipitación, lo que podría indicar falsos positivos o días de llovizna leve.

---

## 3. Evolución diaria de temperaturas

Se visualiza un comportamiento cíclico de las temperaturas máximas y mínimas. La amplitud térmica se mantiene relativamente constante, y no se identifican picos extremos durante el periodo.

---

## 4. Duración del día vs. horas reales de sol

Aunque la duración del día permanece casi constante (por la cercanía a los equinoccios), las horas reales de sol presentan gran variabilidad. Esto refleja la nubosidad o clima lluvioso durante el periodo.

---

## 5. Radiación solar vs. índice UV

Se observa una relación directa: a mayor radiación solar, mayor es el índice UV. Esto valida la consistencia de los datos y alerta sobre exposición al sol en días con alta radiación.

---

## 6. Precipitación vs. velocidad del viento

La mayoría de eventos de precipitación están asociados a velocidades moderadas de viento. No se evidencian picos extremos de viento, pero sí cierta relación con aumentos de lluvia.

---

Todas las visualizaciones se encuentran almacenadas en la carpeta `/docs` como imágenes PNG, generadas a partir de scripts individuales ubicados en la carpeta `/src`.