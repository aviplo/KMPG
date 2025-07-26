english_schema = {
  "type": "object",
  "properties": {
    "lastName": { "type": "string", "minLength": 0, "maxLength": 20 },
    "firstName": { "type": "string", "minLength": 0, "maxLength": 20 },
    "idNumber": { "type": "string", "minLength": 0, "maxLength": 20 },
    "gender": { "type": "string", "minLength": 0, "maxLength": 6 },
    "dateOfBirth": {
      "type": "object",
      "properties": {
        "day": { "type": "string", "minLength": 0, "maxLength": 2 },
        "month": { "type": "string", "minLength": 0, "maxLength": 2 },
        "year": { "type": "string", "minLength": 0, "maxLength": 4 }
      }
    },
    "address": {
      "type": "object",
      "properties": {
        "street": { "type": "string", "minLength": 0, "maxLength": 50 },
        "houseNumber": { "type": "string", "minLength": 0, "maxLength": 10 },
        "entrance": { "type": "string", "minLength": 0, "maxLength": 10 },
        "apartment": { "type": "string", "minLength": 0, "maxLength": 10 },
        "city": { "type": "string", "minLength": 0, "maxLength": 50 },
        "postalCode": { "type": "string", "minLength": 0, "maxLength": 10 },
        "poBox": { "type": "string", "minLength": 0, "maxLength": 20 }
      }
    },
    "landlinePhone": { "type": "string", "minLength": 0, "maxLength": 20 },
    "mobilePhone": { "type": "string", "minLength": 0, "maxLength": 20 },
    "jobType": { "type": "string", "minLength": 0, "maxLength": 20 },
    "dateOfInjury": {
      "type": "object",
      "properties": {
        "day": { "type": "string", "minLength": 0, "maxLength": 2 },
        "month": { "type": "string", "minLength": 0, "maxLength": 2 },
        "year": { "type": "string", "minLength": 0, "maxLength": 4 }
      }
    },
    "timeOfInjury": { "type": "string", "minLength": 0, "maxLength": 8 },
    "accidentLocation": { "type": "string", "minLength": 0, "maxLength": 100 },
    "accidentAddress": { "type": "string", "minLength": 0, "maxLength": 100 },
    "accidentDescription": { "type": "string", "minLength": 0, "maxLength": 100 },
    "injuredBodyPart": { "type": "string", "minLength": 0, "maxLength": 100 },
    "signature": { "type": "string", "minLength": 0, "maxLength": 100 },
    "formFillingDate": {
      "type": "object",
      "properties": {
        "day": { "type": "string", "minLength": 0, "maxLength": 2 },
        "month": { "type": "string", "minLength": 0, "maxLength": 2 },
        "year": { "type": "string", "minLength": 0, "maxLength": 4 }
      }
    },
    "formReceiptDateAtClinic": {
      "type": "object",
      "properties": {
        "day": { "type": "string", "minLength": 0, "maxLength": 2 },
        "month": { "type": "string", "minLength": 0, "maxLength": 2 },
        "year": { "type": "string", "minLength": 0, "maxLength": 4 }
      }
    },
    "medicalInstitutionFields": {
      "type": "object",
      "properties": {
        "healthFundMember": { "type": "string", "minLength": 0, "maxLength": 10 },
        "natureOfAccident": { "type": "string", "minLength": 0, "maxLength": 50 },
        "medicalDiagnoses": { "type": "string", "minLength": 0, "maxLength": 50 }
      }
    }
  }
}

hebrew_schema ={
  "type": "object",
  "properties": {
    "שם משפחה": { "type": "string", "minLength": 0, "maxLength": 20 },
    "שם פרטי": { "type": "string", "minLength": 0, "maxLength": 20 },
    "מספר זהות": { "type": "string", "minLength": 0, "maxLength": 10 },
    "מין": { "type": "string", "minLength": 0, "maxLength": 4 },
    "תאריך לידה": {
      "type": "object",
      "properties": {
        "יום": { "type": "string", "minLength": 0, "maxLength": 2 },
        "חודש": { "type": "string", "minLength": 0, "maxLength": 2 },
        "שנה": { "type": "string", "minLength": 0, "maxLength": 4 }
      }
    },
    "כתובת": {
      "type": "object",
      "properties": {
        "רחוב": { "type": "string", "minLength": 0, "maxLength": 50 },
        "מספר בית": { "type": "string", "minLength": 0, "maxLength": 10 },
        "כניסה": { "type": "string", "minLength": 0, "maxLength": 10 },
        "דירה": { "type": "string", "minLength": 0, "maxLength": 10 },
        "ישוב": { "type": "string", "minLength": 0, "maxLength": 50 },
        "מיקוד": { "type": "string", "minLength": 0, "maxLength": 10 },
        "תא דואר": { "type": "string", "minLength": 0, "maxLength": 10 }
      }
    },
    "טלפון קווי": { "type": "string", "minLength": 0, "maxLength": 12 },
    "טלפון נייד": { "type": "string", "minLength": 0, "maxLength": 15 },
    "סוג העבודה": { "type": "string", "minLength": 0, "maxLength": 50 },
    "תאריך הפגיעה": {
      "type": "object",
      "properties": {
        "יום": { "type": "string", "minLength": 0, "maxLength": 2 },
        "חודש": { "type": "string", "minLength": 0, "maxLength": 2 },
        "שנה": { "type": "string", "minLength": 0, "maxLength": 4 }
      }
    },
    "שעת הפגיעה": { "type": "string", "minLength": 0, "maxLength": 8 },
    "מקום התאונה": { "type": "string", "minLength": 0, "maxLength": 100 },
    "כתובת מקום התאונה": { "type": "string", "minLength": 0, "maxLength": 100 },
    "תיאור התאונה": { "type": "string", "minLength": 0, "maxLength": 100 },
    "האיבר שנפגע": { "type": "string", "minLength": 0, "maxLength": 100 },
    "חתימה": { "type": "string", "minLength": 0, "maxLength": 50 },
    "תאריך מילוי הטופס": {
      "type": "object",
      "properties": {
        "יום": { "type": "string", "minLength": 0, "maxLength": 2 },
        "חודש": { "type": "string", "minLength": 0, "maxLength": 2 },
        "שנה": { "type": "string", "minLength": 0, "maxLength": 4 }
      }
    },
    "תאריך קבלת הטופס בקופה": {
      "type": "object",
      "properties": {
        "יום": { "type": "string", "minLength": 0, "maxLength": 2 },
        "חודש": { "type": "string", "minLength": 0, "maxLength": 2 },
        "שנה": { "type": "string", "minLength": 0, "maxLength": 4 }
      }
    },
    "למילוי ע\"י המוסד הרפואי": {
      "type": "object",
      "properties": {
        "חבר בקופת חולים": { "type": "string", "minLength": 0, "maxLength": 10 },
        "מהות התאונה": { "type": "string", "minLength": 0, "maxLength": 50 },
        "אבחנות רפואיות": { "type": "string", "minLength": 0, "maxLength": 50 }
      }
    }
  }
}
