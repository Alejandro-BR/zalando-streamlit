# 👕 Clasificador de Prendas - Streamlit App 👟

Aplicación web interactiva desarrollada con **Streamlit** que permite subir imágenes de prendas y clasificarlas automáticamente utilizando un modelo de **Deep Learning** entrenado con TensorFlow/Keras (Fashion MNIST / Zalando).

[🔗 **App en línea**](http://zalando-alejandro.streamlit.app/)

## 🧠 Modelo

La aplicación utiliza un modelo entrenado previamente:

```
models/zalando.keras
```

El modelo recibe imágenes en escala de grises de tamaño **28×28 píxeles** y predice una de las siguientes clases:

| Índice | Clase       |
| ------ | ----------- |
| 0      | T-shirt/top |
| 1      | Trouser     |
| 2      | Pullover    |
| 3      | Dress       |
| 4      | Coat        |
| 5      | Shirt       |
| 6      | Sneaker     |
| 7      | Bag         |
| 8      | Ankle boot  |

## 📸 Ejemplo de uso

1. Sube una o varias imágenes de prendas.
2. La imagen se procesa automáticamente:

   * Escala de grises
   * Inversión de colores
   * Redimensionado a 28×28
   * Normalización
3. La app muestra:

   * La imagen procesada
   * El vector de predicción
   * La clase predicha

## 🐳 Ejecutar con Docker

### 1. Construir y levantar el contenedor

```bash
docker-compose up --build
```

### 2. Abrir en el navegador

```
http://localhost:8501
```

## ✍️ Créditos

**Alejandro Barrionuevo Rosado**
Máster de FP en Inteligencia Artificial y Big Data - CPIFP Alan Turing
