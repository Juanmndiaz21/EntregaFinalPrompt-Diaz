from pydantic import BaseModel, Field

class Circuito(BaseModel):
    nombre_circuito: str = Field(
        description="Nombre identificativo del circuito"
    )
    cargas: str = Field(
        description="Cargas o artefactos que alimenta el circuito"
    )
    potencia_estimada_w: float = Field(
        description="Potencia estimada del circuito en watts"
    )
    corriente_estimada_a: float = Field(
        description="Corriente estimada del circuito en amperios"
    )
    seccion_cable_mm2: str = Field(
        description="Sección del conductor recomendado"
    )
    termica_amperios: str = Field(
        description="Protección termomagnética recomendada"
    )
    fundamentacion: str = Field(
        description="Explicación técnica de la elección"
    )

class DimensionamientoElectrico(BaseModel):
    resumen_instalacion: str = Field(
        description="Análisis técnico general de la instalación y sus supuestos"
    )
    potencia_instalada_total_w: float = Field(
        description="Potencia instalada total estimada en watts"
    )
    corriente_total_estimada_a: float = Field(
        description="Corriente total estimada de la instalación en amperios"
    )
    tipo_suministro: str = Field(
        description="Tipo de suministro identificado o supuesto: monofásico, trifásico o no determinado"
    )
    circuitos: list[Circuito] = Field(
        description="Listado de circuitos dimensionados"
    )
    disyuntor_diferencial: str = Field(
        description="Recomendación del disyuntor diferencial general"
    )
    materiales_sugeridos: list[str] = Field(
        description="Lista de insumos recomendados para el dimensionamiento"
    )