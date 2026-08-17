from google import genai
from google.genai import types
from src.models import DimensionamientoElectrico
from src.prompts import SYSTEM_PROMPT

def generar_dimensionamiento(api_key: str, user_input: str) -> DimensionamientoElectrico:
    client = genai.Client(api_key=api_key)

    # Lista de modelos en orden de preferencia: si uno falla (por tokens, cuota, etc.), se intenta con el siguiente
    modelos = [
        "gemini-3.5-flash-lite",       
        "gemini-3.6-flash",
        "gemini-3.1-pro"   
    ]

    ultimo_error = None

    for modelo in modelos:
        try:
            chat = client.chats.create(
                model=modelo,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    response_mime_type="application/json",
                    response_schema=DimensionamientoElectrico,
                    temperature=0.2,
                )
            )

            response = chat.send_message(user_input)
            
            if response.parsed:
                return response.parsed  # type: ignore
            else:
                return DimensionamientoElectrico.model_validate_json(response.text) # type: ignore
                
        except Exception as e:
            ultimo_error = e
            # Continúa con el siguiente modelo en caso de error (ResourceExhausted, TokenLimit, etc.)
            continue

    # Si todos los modelos fallaron, lanzamos el último error registrado para depuración
    raise ultimo_error or RuntimeError("Todos los modelos de Gemini fallaron al procesar la solicitud.")
