import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Nutresa Conecta", page_icon="🥗", layout="centered")

st.title("🥗 Nutresa Conecta")
st.subtitle("Conectando tu experiencia de consumo con la familia Nutresa")

# Pantalla 1: Selección / Escaneo del producto
st.header("1. Producto Detectado por QR")
producto = st.selectbox(
    "Selecciona un producto escaneado (Simulación):",
    ["Pastas Doria Spaghetti 500g", "Galletas Tosh Miel", "Chocolates Jet 12u", "Café Colcafé Clásico"]
)

st.success(f"¡Has validado tu empaque de **{producto}**!")

# Pantalla 2: Recomendaciones e IA
st.header("2. Experiencia & Venta Cruzada (IA)")
if "Doria" in producto:
    st.info("💡 **Receta Sugerida:** Pastas Doria en salsa de Carne Zenú y Queso Alpina.")
    st.markdown("👉 **Recomendación cruzada:** Acompaña esta comida con una taza de **Café Matiz**.")
elif "Tosh" in producto:
    st.info("💡 **Tip Saludable:** Disfruta tus galletas Tosh con una taza de **Colcafé Granulado**.")

# Pantalla 3: Captura de Datos y Fidelización
st.header("3. Nutresa Puntos & Perfilamiento")
with st.form("registro_puntos"):
    nombre = st.text_input("Nombre completo:")
    email = st.text_input("Correo electrónico:")
    preferencia = st.multiselect(
        "¿Cuáles son tus intereses nutricionales?",
        ["Bajo en azúcar", "Alto en proteína", "Recetas rápidas", "Snacks saludables"]
    )
    submit = st.form_submit_button("Sumar 50 Puntos Nutresa")
    
    if submit:
        st.balloons()
        st.success(f"¡Gracias {nombre}! Has acumulado 50 puntos. Tus preferencias han sido registradas de forma segura.")
