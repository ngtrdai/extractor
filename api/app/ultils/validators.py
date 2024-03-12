from typing import Dict, Any

from jsonschema.exceptions import ValidationError
from jsonschema.validators import Draft202012Validator


def validate_json_schema(schema: Dict[str, Any]) -> None:
    try:
        Draft202012Validator.check_schema(schema)
    except ValidationError as e:
        raise ValueError(e.message)
