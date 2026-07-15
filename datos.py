import json
archivo_citas = "citas.json"

def leer_citas():
    try:
        with open(archivo_citas, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
        
    except FileNotFoundError:
        return[]

