import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Datos ficticios de consumo
# -----------------------------
data_consumo = {
    "Mes": ["Enero","Febrero","Marzo","Abril","Mayo","Junio",
            "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"],
    "Consumo Convencional (kWh)": [180,175,190,185,200,195,210,205,190,185,175,220],
    "Costo (COP)": [144000,140000,152000,148000,160000,156000,
                    168000,164000,152000,148000,140000,176000]
}
df = pd.DataFrame(data_consumo)

# -----------------------------
# Interfaz Streamlit
# -----------------------------
st.title("📊 Análisis de Consumo Energético Convencional")
st.write("Ejemplo de estadísticas descriptivas y visualización de datos.")

# Mostrar tabla de datos
st.subheader("📋 Datos Originales")
st.dataframe(df)

# -----------------------------
# Estadísticas Descriptivas
# -----------------------------
st.subheader("📈 Estadísticas Descriptivas")

desc_stats = df[["Consumo Convencional (kWh)", "Costo (COP)"]].describe()
st.dataframe(desc_stats)

# Moda
st.write("🔹 Moda de Consumo (kWh):", df["Consumo Convencional (kWh)"].mode()[0])
st.write("🔹 Moda de Costo (COP):", df["Costo (COP)"].mode()[0])

# -----------------------------
# Gráficos Univariados
# -----------------------------
st.subheader("📊 Distribución Univariada")

# Histograma
fig1, ax1 = plt.subplots()
ax1.hist(df["Consumo Convencional (kWh)"], bins=6, color="skyblue", edgecolor="black")
ax1.set_title("Histograma - Consumo de Energía")
ax1.set_xlabel("Consumo (kWh)")
ax1.set_ylabel("Frecuencia")
st.pyplot(fig1)

# Diagrama de caja
fig2, ax2 = plt.subplots()
ax2.boxplot(df["Consumo Convencional (kWh)"], vert=False, patch_artist=True)
ax2.set_title("Diagrama de Caja - Consumo de Energía")
st.pyplot(fig2)

# -----------------------------
# Gráficos Bivariados
# -----------------------------
st.subheader("🔗 Relación entre Consumo y Costo")

# Dispersión
fig3, ax3 = plt.subplots()
ax3.scatter(df["Consumo Convencional (kWh)"], df["Costo (COP)"], color="red", alpha=0.7)
ax3.set_xlabel("Consumo (kWh)")
ax3.set_ylabel("Costo (COP)")
ax3.set_title("Gráfico de Dispersión")
st.pyplot(fig3)

# Correlación con mapa de calor
st.subheader("🔥 Mapa de Calor de Correlaciones")
corr = df[["Consumo Convencional (kWh)", "Costo (COP)"]].corr()
fig4, ax4 = plt.subplots()
sns.heatmap(corr, annot=True, cmap="Blues", ax=ax4)
st.pyplot(fig4)

# -----------------------------
# Visualización Clave
# -----------------------------
st.subheader("🌟 Información Clave")
st.markdown("""
- Existe una *correlación fuerte positiva* entre consumo y costo (a más kWh, mayor valor en la factura).
- El histograma muestra que la mayoría de meses se concentran entre *175 y 200 kWh*.
- El diagrama de caja revela un posible *outlier en diciembre (220 kWh)*, lo que puede ser explicado por mayor uso de luces y electrodomésticos en fiestas.
""")