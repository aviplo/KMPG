from jsonschema import validate, ValidationError
import json

def parse_and_validate_response(response, schema):
    try:
        result = json.loads(response)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON response: {e}")
    if not isinstance(result, dict):
        raise ValueError(f"Expected JSON object, got: {type(result)}")
    if not check_validation(schema, result):
        raise ValueError("JSON validation failed")
    return result

def check_validation(schema, data):
    try:
        validate(instance=data, schema=schema)
        print("JSON validation passed")
        return True
    except ValidationError as e:
        error_details = {
            "message": e.message,
            "field": list(e.path),
            "schema_rule": e.validator,
            "expected": e.validator_value,
            "invalid_value": e.instance,
        }
        print("JSON validation failed:", error_details)
        raise ValueError(f"JSON validation failed: {error_details}")
    
    
    # {
    #     "first_name": lambda v: isinstance(v, str) and v.strip() != "",
    #     "last_name": lambda v: isinstance(v, str) and v.strip() != "",
    #     "id_number": lambda v: re.fullmatch(r"\d{9}", str(v)) is not None,
    #     "gender": lambda v: v in ["זכר", "נקבה", "male", "female"],
    #     "age": lambda v: isinstance(v, int) and 0 <= v <= 120,
    #     "hmo": lambda v: v in ["מכבי", "מאוחדת", "כללית", "Maccabi", "Meuhedet", "Clalit"],
    #     "hmo_card_number": lambda v: re.fullmatch(r"\d{9}", str(v)) is not None,
    #     "membership_tier": lambda v: v in ["זהב", "כסף", "ארד", "Gold", "Silver", "Bronze"]
    # }