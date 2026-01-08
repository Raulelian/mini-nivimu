from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

# =========================
# FUNCIONES DE DATOS
# =========================

def cargar_empleados():

    try:
        with open("empleados.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_empleados(empleados):
    with open("empleados.json", "w", encoding="utf-8") as f:
        json.dump(empleados, f, indent=4, ensure_ascii=False)

# =========================
# RUTAS
# =========================

@app.route("/")
def inicio():
    empleados = cargar_empleados()
    return render_template("index.html", empleados=empleados)

@app.route("/nuevo", methods=["GET", "POST"])
def nuevo_empleado():
    if request.method == "POST":
        empleados = cargar_empleados()

        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        puesto = request.form["puesto"]

        nuevo = {
            "Nombre": nombre,
            "Edad": edad,
            "Puesto": puesto
        }

        empleados.append(nuevo)
        guardar_empleados(empleados)

        return redirect("/")

    return render_template("nuevo.html")

@app.route("/eliminar/<int:indice>", methods=["POST"])

def eliminar_empleado(indice):
    
    empleados = cargar_empleados()
    
    empleados.pop(indice)
    
    guardar_empleados(empleados)
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
