from flask import Flask, render_template, request, redirect, flash
from datos import agregar_cita, leer_citas, eliminar_cita
from negocio import valFecha, valHora, filtrar_por_fecha

app = Flask(__name__)
app.secret_key = "reservapro2026"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/crear", methods=["GET", "POST"])
def crear():
    if request.method == "POST":
        nombre = request.form.get("nombre").strip()
        servicio = request.form.get("servicio").strip()
        fecha = request.form.get("fecha").strip()
        hora = request.form.get("hora").strip()

        if not nombre or not servicio:
            flash("Todos los campos son obligatorios.", "danger")
            return redirect("/crear")

        if not valFecha(fecha):
            flash("La fecha no es válida.", "danger")
            return redirect("/crear")

        if not valHora(hora):
            flash("La hora no es válida.", "danger")
            return redirect("/crear")

        cita = {
            "nombre": nombre,
            "servicio": servicio,
            "fecha": fecha,
            "hora": hora
        }
        agregar_cita(cita)
        flash("Cita creada exitosamente.", "success")
        return redirect("/")

    return render_template("crear.html")

@app.route("/ver", methods=["GET", "POST"])
def ver():
    citas_del_dia = []
    fecha_buscada = ""

    if request.method == "POST":
        fecha_buscada = request.form.get("fecha").strip()

        if not valFecha(fecha_buscada):
            flash("La fecha no es válida.", "danger")
            return redirect("/ver")

        citas = leer_citas()
        citas_del_dia = filtrar_por_fecha(citas, fecha_buscada)

    return render_template("ver.html", citas=citas_del_dia, fecha=fecha_buscada)

@app.route("/cancelar", methods=["GET", "POST"])
def cancelar():
    citas_del_dia = []
    fecha_buscada = ""

    if request.method == "POST":
        fecha_buscada = request.form.get("fecha").strip()

        if not valFecha(fecha_buscada):
            flash("La fecha no es válida.", "danger")
            return redirect("/cancelar")

        citas = leer_citas()
        citas_filtradas = filtrar_por_fecha(citas, fecha_buscada)

        for i, cita in enumerate(leer_citas()):
            for cita_filtrada in citas_filtradas:
                if cita == cita_filtrada:
                    cita_filtrada["indice_real"] = i

        citas_del_dia = citas_filtradas

    return render_template("cancelar.html", citas=citas_del_dia, fecha=fecha_buscada)

@app.route("/eliminar", methods=["POST"])
def eliminar():
    indice = int(request.form.get("indice"))
    eliminar_cita(indice)
    flash("Cita cancelada exitosamente.", "success")
    return redirect("/cancelar")

if __name__ == "__main__":
    app.run(debug=True)
