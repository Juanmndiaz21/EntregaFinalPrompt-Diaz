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
   git clone https://github.com/Juanmndiaz21/EntregaFinalPrompt-Diaz.git
   cd EntregaFinalPrompt-Diaz.git
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

5. **Ejecutar la aplicación:**
   ```bash
   streamlit run app.py
   ```

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

##  Aplicación en Producción

Puedes probar la aplicación en línea en el siguiente enlace:
[https://entregafinalprompt-diaz.streamlit.app/](https://entregafinalprompt-diaz.streamlit.app/)

