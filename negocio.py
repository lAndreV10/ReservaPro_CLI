from datetime import datetime

def valFecha(fechaTexto):
    try:
        datetime.strptime(fechaTexto, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    
def valHora(horaTexto):
    try:
        datetime.strptime(horaTexto, "%H:%M")
        return True
    except ValueError:
        return False

def filtrar_por_fecha(citas, fecha):
    citas_del_dia = []
    for cita in citas:
        if cita["fecha"] == fecha:
            citas_del_dia.append(cita)
    return citas_del_dia