import json
archivo_citas = "citas.json"

def leer_citas():
    try:
        with open(archivo_citas, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return[]

def guardar_citas(citas):
    with open(archivo_citas, "w", encoding="utf-8") as archivo:
        json.dump(citas, archivo, indent=4, ensure_ascii=False)

def agregar_cita(cita):
    citas = leer_citas()
    citas.append(cita)
    guardar_citas(citas)
    
