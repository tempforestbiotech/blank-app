# 🏡 Estimador de Valor de Propiedad en UF

Esta aplicación interactiva desarrollada con **Streamlit** permite estimar el valor de propiedades residenciales en **UF**, a partir de características básicas como superficie, comuna, tipo de vivienda y número de habitaciones, baños y estacionamientos.

---

## 🚀 Demo

👉 Puedes probar la app aquí: [https://blank-app.streamlit.app](https://blank-app.streamlit.app)

---

## 🧠 Descripción técnica

Se utilizó un modelo de **Random Forest Regressor**, entrenado con datos de propiedades reales, para predecir el valor en UF. El modelo fue entrenado previamente en Jupyter y guardado como archivo `.pkl`, junto con los codificadores de las variables categóricas (`LabelEncoder` para `Comuna` y `Tipo_Vivienda`).

---

## ⚙️ ¿Qué incluye la app?

- Formulario interactivo para ingresar:
  - Comuna
  - Tipo de vivienda
  - Número de habitaciones
  - Número de baños
  - Número de estacionamientos
  - Superficie total del terreno
  - Superficie construida
- Botón para estimar el valor
- Resultado en UF

---

## 📦 Archivos importantes

| Archivo | Descripción |
|--------|-------------|
| `streamlit_app.py` | Código principal de la app |
| `modelo_valor_uf.pkl` | Modelo entrenado de regresión |
| `label_encoder_comuna.pkl` | Codificador de comuna |
| `label_encoder_tipo.pkl` | Codificador de tipo de vivienda |
| `requirements.txt` | Lista de dependencias |
| `BaseCorregida (1).csv` | Base original usada para el entrenamiento |

---

## 🧪 Librerías necesarias

Incluidas en `requirements.txt`:

