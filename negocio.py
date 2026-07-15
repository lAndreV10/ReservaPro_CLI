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