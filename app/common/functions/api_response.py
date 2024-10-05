
from flask import jsonify
from typing import Type, Any
from marshmallow import Schema
from sqlalchemy.orm import DeclarativeMeta
from datetime import datetime
from common.schemas.api_response_schema import StandardResponse


def standard_response(status: int, message: str, data: Any = None, marshmallow_schema: Type[Schema] = None):
    # Si los datos son una lista de modelos de SQLAlchemy
    if isinstance(data, list) and marshmallow_schema is not None:
        data = marshmallow_schema(many=True).dump(data)
        # Convertir datetime a formato ISO en listas
        for item in data:
            for key, value in item.items():
                if isinstance(value, datetime):
                    item[key] = value.isoformat()

    # Si los datos son un solo objeto SQLAlchemy
    elif isinstance(type(data), DeclarativeMeta) and marshmallow_schema is not None:
        data = marshmallow_schema().dump(data)
        # Convertir datetime a formato ISO
        for key, value in data.items():
            if isinstance(value, datetime):
                data[key] = value.isoformat()

    # Contenido de la respuesta
    response_content = {
        "status": status,
        "message": message,
        "data": data
    }

    # Usar StandardResponse para la respuesta final
    standard_response_schema = StandardResponse()
    response_serialized = standard_response_schema.dump(response_content)
    
    return jsonify(response_serialized), status
