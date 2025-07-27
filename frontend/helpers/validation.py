from jsonschema import validate, ValidationError

required_fields = {
        "full_name": { "type": "string", "minLength": 0, "maxLength": 20 },
        "id_number": { "type": "string", "minLength": 0, "maxLength": 20 },
        "gender": { "type": "string", "enum": ["זכר", "נקבה","male","female"] },
        "age": { "type": "integer", "minimum": 0, "maximum": 120 },
        "hmo_name": { "type": "string", "enum": ["מכבי", "מאוחדת", "כללית", "Maccabi", "Meuhedet", "Clalit"] },
        "hmo_card_number": { "type": "string", "minLength": 0, "maxLength": 20 },
        "membership_tier": { "type": "string", "enum": ["זהב", "כסף", "ארד", "Gold", "Silver", "Bronze"] },
}

def validate_user_info(user_info):
    missing_fields = [f.lower() for f in required_fields.keys() if f not in user_info]
    if not missing_fields:
        return True, None
    return False, f"Missing required fields: {', '.join(missing_fields)}"