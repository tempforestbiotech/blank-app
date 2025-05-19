import streamlit as st
import pandas as pd
import joblib

# Cargar modelo y codificadores
model = joblib.load("modelo_valor_uf.pkl")
le_comuna = joblib.load("label_encoder_comuna.pkl")
le_tipo = joblib.load("label_encoder_tipo.pkl")

# Título
st.title("🏡 Estimador de Valor de Propiedad en UF")
st.write("Ingresa las características de la propiedad para estimar su precio.")

# Entradas del usuario
comuna = st.selectbox("Comuna", le_comuna.classes_)
tipo = st.selectbox("Tipo de vivienda", le_tipo.classes_)
habitaciones = st.number_input("N° Habitaciones", 1, 10, 3)
banos = st.number_input("N° Baños", 1, 6, 2)
estacionamientos = st.number_input("N° Estacionamientos", 0, 5, 1)
sup_total = st.number_input("Superficie total (m²)", 10, 10000, 500)
sup_construida = st.number_input("Superficie construida (m²)", 10, 1000, 150)

# Convertir datos
X_nueva = pd.DataFrame([[
    le_comuna.transform([comuna])[0],
    le_tipo.transform([tipo])[0],
    habitaciones,
    banos,
    estacionamientos,
    sup_total,
    sup_construida
]], columns=['Comuna', 'Tipo_Vivienda', 'N_Habitaciones', 'N_Baños',
             'N_Estacionamientos', 'Total_Superficie_M2', 'Superficie_Construida_M2'])

# Predicción
if st.button("Estimar Valor"):
    prediccion = model.predict(X_nueva)[0]
    st.success(f"💰 Valor estimado: {round(prediccion):,.0f} UF")
