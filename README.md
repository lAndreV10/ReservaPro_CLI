# ReservaPro

Sistema de gestión de citas desarrollado en Python. Disponible en dos versiones: aplicación de consola (CLI) y aplicación web con Flask.

---

## Descripción

ReservaPro es un sistema orientado a negocios que necesitan gestionar citas con clientes (peluquerías, consultorios, talleres, etc.). Permite crear, consultar y cancelar reservas. Los datos se guardan en un archivo JSON local.

---

## Tecnologías

- Python 3.x
- Flask 3.1.3
- Bootstrap 5
- Módulo `json` (librería estándar)
- Módulo `datetime` (librería estándar)

---

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/ReservaPro.git
cd ReservaPro
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

---

## Ejecución

**Versión Web (Flask)**
```bash
python app.py
```
Luego abre el navegador en `http://127.0.0.1:5000`

**Versión CLI**
```bash
python interfaz.py
```

---

## Funcionalidades

| Función | Descripción |
|--------|-------------|
| Crear cita | Registra una cita con nombre, servicio, fecha y hora |
| Ver citas del día | Consulta todas las citas de una fecha específica |
| Cancelar cita | Elimina una cita existente |

---

## Arquitectura

El proyecto sigue una arquitectura en 3 capas:

```
ReservaPro/
├── app.py            # Servidor web Flask (rutas y vistas)
├── interfaz.py       # Versión CLI (consola)
├── negocio.py        # Lógica: validaciones y filtros
├── datos.py          # Datos: lectura y escritura en citas.json
├── templates/        # Páginas HTML
│   ├── base.html
│   ├── index.html
│   ├── crear.html
│   ├── ver.html
│   └── cancelar.html
├── static/
│   └── css/
│       └── style.css
├── requirements.txt
├── .gitignore
└── README.md
```

- **`app.py`** — Maneja las rutas web y conecta la interfaz con la lógica
- **`interfaz.py`** — Versión de consola del sistema
- **`negocio.py`** — Valida fechas y horas, filtra citas por fecha
- **`datos.py`** — Gestiona la persistencia en `citas.json`

---

## Estructura de una cita

Cada cita se almacena en `citas.json` con el siguiente formato:

```json
{
    "nombre": "Juan Pérez",
    "servicio": "Corte de cabello",
    "fecha": "2026-07-15",
    "hora": "10:30"
}
```

---

## Autor

Desarrollado como proyecto de portafolio.
