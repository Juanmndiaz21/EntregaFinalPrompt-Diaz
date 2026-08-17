import os
import json
import streamlit as st
import pandas as pd

from src.services import generar_dimensionamiento

# ------------------------------------------------------------------------------
# Configuración de la página
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Asistente de Dimensionamiento Eléctrico",
    layout="wide"
)

# ------------------------------------------------------------------------------
# Carga de CSS Personalizado desde archivo externo
# ------------------------------------------------------------------------------
def load_css(file_name="static/styles.css"):
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

load_css("static/styles.css")

# ------------------------------------------------------------------------------
# Encabezado Principal
# ------------------------------------------------------------------------------
st.markdown(
    """
    <div class="hero-card">
        <div class="eyebrow">Panel</div>
        <h1>Asistente para Dimensionamiento de Tableros Eléctricos</h1>
        <p>
            Herramienta de uso interno para la recomendación de protecciones,
            dimensionamiento de cables y estructuración de circuitos eléctricos.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.expander("¿Cómo funciona esta herramienta?"):
    st.markdown("""
    1. **Ingreso de datos:** Escribe los consumos o descripción del proyecto.
    2. **Análisis con IA:** La aplicación analiza las cargas y estima potencia y corriente.
    3. **Distribución de circuitos:** Se proponen circuitos, conductores y protecciones.
    4. **Resultado estructurado:** Obtendrás el dimensionamiento técnico y los materiales sugeridos.
    """)

st.markdown("<br>", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# Gestión de API Key
# ------------------------------------------------------------------------------
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key and "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]

if not api_key:
    st.error(
        "No se encontró la API Key de Gemini en las variables de entorno "
        "o secrets.toml."
    )
    st.stop()

# ------------------------------------------------------------------------------
# Entrada de Datos e Interfaz
# ------------------------------------------------------------------------------
st.subheader("Ingreso de Requerimientos de la Instalación")

user_input = st.text_area(
    "Detalle los artefactos, ambientes o consumos previstos:",
    placeholder=(
        "Ej: Necesito armar el tablero para un comercio pequeño: "
        "15 paneles LED de 18W"
    ),
    height=130
)

st.markdown(
    "<div style='margin-top: 10px;'></div>",
    unsafe_allow_html=True
)

# ------------------------------------------------------------------------------
# Procesamiento
# ------------------------------------------------------------------------------
if st.button(
    "Calcular y Generar Recomendación Técnica",
    type="primary"
):
    if not user_input.strip():
        st.warning(
            "Por favor, ingrese el detalle de la instalación antes de continuar."
        )
    else:
        with st.spinner(
            "Analizando requerimientos técnicos con IA..."
        ):
            try:
                data = generar_dimensionamiento(api_key, user_input)

                st.success("Análisis completado con éxito")

                st.markdown("<br>", unsafe_allow_html=True)

                # ------------------------------------------------------------------
                # Resumen General
                # ------------------------------------------------------------------
                st.subheader("Resumen Técnico de la Instalación")

                st.info(data.resumen_instalacion)

                # ------------------------------------------------------------------
                # Indicadores Generales
                # ------------------------------------------------------------------
                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "Potencia instalada",
                        f"{data.potencia_instalada_total_w:,.0f} W"
                    )

                with col2:
                    st.metric(
                        "Corriente estimada",
                        f"{data.corriente_total_estimada_a:.2f} A"
                    )

                with col3:
                    st.metric(
                        "Tipo de suministro",
                        data.tipo_suministro
                    )

                st.markdown("<br>", unsafe_allow_html=True)

                # ------------------------------------------------------------------
                # Desglose de Circuitos
                # ------------------------------------------------------------------
                st.subheader(
                    "Desglose de Circuitos y Protecciones Recomendadas"
                )

                if data.circuitos:
                    df_circuitos = pd.DataFrame(
                        [c.model_dump() for c in data.circuitos]
                    )

                    df_circuitos.columns = [
                        "Circuito",
                        "Cargas",
                        "Potencia (W)",
                        "Corriente (A)",
                        "Cable (mm²)",
                        "Térmica (A)",
                        "Fundamentación"
                    ]

                    st.dataframe(
                        df_circuitos,
                        width="stretch",
                        hide_index=True
                    )

                else:
                    st.warning(
                        "No se pudieron determinar circuitos para la instalación."
                    )

                st.markdown("<br>", unsafe_allow_html=True)

                # ------------------------------------------------------------------
                # Protección y Materiales
                # ------------------------------------------------------------------
                col1, col2 = st.columns(2)

                with col1:
                    st.subheader("Protección Diferencial General")

                    st.success(
                        data.disyuntor_diferencial
                    )

                with col2:
                    st.subheader("Lista de Materiales Sugeridos")

                    if data.materiales_sugeridos:
                        for material in data.materiales_sugeridos:
                            st.markdown(f"• {material}")
                    else:
                        st.info(
                            "No se identificaron materiales adicionales."
                        )

                # ------------------------------------------------------------------
                # Exportación JSON
                # ------------------------------------------------------------------
                st.divider()

                json_data = json.dumps(
                    data.model_dump(),
                    indent=2,
                    ensure_ascii=False
                )

                st.download_button(
                    label="Descargar Cotización (JSON)",
                    data=json_data,
                    file_name="dimensionamiento_electrico.json",
                    mime="application/json"
                )

            except Exception as e:
                st.error(
                    f"Ocurrió un error durante el procesamiento: {str(e)}"
                )