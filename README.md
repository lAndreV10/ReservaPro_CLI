# ReservaPro CLI

Sistema de gestión de citas por consola desarrollado en Python. Permite crear, consultar y cancelar reservas de forma sencilla desde la terminal.

---

## Descripción

ReservaPro CLI es una aplicación de línea de comandos orientada a negocios que necesitan gestionar citas con clientes (peluquerías, consultorios, talleres, etc.). Los datos se persisten en un archivo JSON local.

---

## Tecnologías

- Python 3.x
- Módulo `json` (librería estándar)
- Módulo `datetime` (librería estándar)

No requiere instalar dependencias externas.

---

## Instalación y ejecución

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/ReservaPro.git
cd ReservaPro
```

2. Ejecuta el programa:
```bash
python interfaz.py
```

---

## Funcionalidades

| Opción | Descripción |
|--------|-------------|
| 1. Crear nueva cita | Registra una cita con nombre, servicio, fecha y hora |
| 2. Ver citas del día | Consulta todas las citas de una fecha específica |
| 3. Cancelar cita | Elimina una cita existente con confirmación previa |
| 4. Salir | Cierra el programa |

---

## Arquitectura

El proyecto sigue una arquitectura en 3 capas:

```
ReservaPro/
├── interfaz.py   # Capa de presentación: menú e interacción con el usuario
├── negocio.py    # Capa de lógica: validaciones y filtros
├── datos.py      # Capa de datos: lectura y escritura en citas.json
├── .gitignore
└── README.md
```

- **`interfaz.py`** — Captura inputs del usuario, muestra resultados y coordina el flujo
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
