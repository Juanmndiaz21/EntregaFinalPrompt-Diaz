# ⚡ Asistente de Dimensionamiento Eléctrico con IA

Aplicación web interactiva desarrollada con **Streamlit** y la API de **Google Gemini** para asistir en el cálculo, recomendación de protecciones, dimensionamiento de cables y estructuración de circuitos eléctricos residenciales y comerciales.

---

##  Características Principales

- **Entrada en Lenguaje Natural:** Describe los consumos o ambientes de manera sencilla (ej: *"Necesito armar el tablero para un local comercial con 15 paneles LED de 18W y 4 aires acondicionados"*).
- **Modelos Múltiples con Resilencia:** Implementa un sistema de respaldo automático entre modelos Gemini (Flash / Pro) para garantizar respuestas robustas.
- **Salida Estructurada Técnica:** Proporciona un desglose completo que incluye:
  - Potencia estimada y corriente total.
  - Circuitos recomendados (iluminación, tomacorrientes, usos específicos).
  - Secciones normalizadas de conductores (cables en mm²).
  - Protecciones termomagnéticas y diferenciales adecuadas.
  - Lista de materiales para cotización rápida.
- **Interfaz Moderna y Personalizada:** Diseño optimizado con hojas de estilo CSS dedicadas (`static/styles.css`).

---

##  Tecnologías y Librerías

- **Python** (3.10+)
- **Streamlit** (Interfaz de usuario web)
- **Google GenAI SDK** (`google-genai`)
- **Pandas** (Manipulación de datos tabulares)

---

##  Instalación y Ejecución Local

Si deseas correr el proyecto en tu máquina local, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/electrospec-ai.git
   cd electrospec-ai
   ```

2. **Crear y activar un entorno virtual:**
   - En Windows (PowerShell):
     ```powershell
     python -m venv venv
     venv\Scripts\Activate.ps1
     ```
   - En macOS / Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar la API Key de Gemini:**
   Puedes configurar tu clave mediante una variable de entorno o creando un archivo `.streamlit/secrets.toml`:
   - **Opción A (Variable de entorno en PowerShell):**
     ```powershell
     $env:GEMINI_API_KEY="tu_api_key_de_gemini"
     ```
   - **Opción B (Archivo `secrets.toml`):**
     Crea la carpeta `.streamlit` y dentro el archivo `secrets.toml`:
     ```toml
     GEMINI_API_KEY = "tu_api_key_de_gemini"
     ```

5. **Ejecutar la aplicación:**
   ```bash
   streamlit run app.py
   ```

---

##  Despliegue en Streamlit Community Cloud

Para desplegar la aplicación en la nube de forma gratuita:

1. Sube tu repositorio a **GitHub**.
2. Entra a [Streamlit Community Cloud](https://share.streamlit.io/).
3. Haz clic en **New app** y selecciona tu repositorio, rama (`main`) y archivo principal (`app.py`).
4. Ve a **Settings > Secrets** en el panel de Streamlit Cloud y añade tu clave:
   ```toml
   GEMINI_API_KEY = "tu_api_key_de_gemini"
   ```
5. Haz clic en **Save** y tu aplicación estará en línea.

---

##  Estructura del Proyecto

```text
electrospec-ai/
├── .streamlit/
│   └── config.toml
├── static/
│   └── styles.css
├── src/
│   ├── __init__.py
│   ├── models.py
│   ├── prompts.py
│   └── services.py
├── app.py
├── requirements.txt
├── .gitignore
└── readme.md
```

---

##  Licencia

Este proyecto es de uso libre bajo la licencia MIT.
