from flask import Flask, render_template, request, redirect
import json
import re

app = Flask(__name__)

RUTA_JSON = "empleados.json"

def cargar_empleados():
    try:
        with open(RUTA_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_empleados(empleados):
    with open(RUTA_JSON, "w", encoding="utf-8") as f:
        json.dump(empleados, f, indent=4, ensure_ascii=False)

def solo_letras_y_espacios(texto: str) -> bool:
    # Letras (incluye acentos) y espacios. Mínimo 2 caracteres.
    return bool(re.fullmatch(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ ]{2,40}", texto))

@app.route("/")
def inicio():
    empleados = cargar_empleados()
    return render_template("index.html", empleados=empleados)

@app.route("/nuevo", methods=["GET", "POST"])
def nuevo_empleado():
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        puesto = request.form.get("puesto", "").strip()
        edad_txt = request.form.get("edad", "").strip()

        # Validar nombre
        if not solo_letras_y_espacios(nombre):
            return render_template("nuevo.html", error="Nombre inválido: solo letras y espacios (2-40).")

        # Validar puesto
        if not solo_letras_y_espacios(puesto):
            return render_template("nuevo.html", error="Puesto inválido: solo letras y espacios (2-40).")

        # Validar edad
        try:
            edad = int(edad_txt)
        except ValueError:
            return render_template("nuevo.html", error="Edad inválida: debe ser un número.")

        if edad <= 1 or edad > 99:
            return render_template("nuevo.html", error="Edad fuera de rango: usa un número entre 14 y 99.")

        empleados = cargar_empleados()

        nuevo = {"Nombre": nombre, "Edad": edad, "Puesto": puesto}
        empleados.append(nuevo)

        guardar_empleados(empleados)
        return redirect("/")

    return render_template("nuevo.html")

@app.route("/eliminar/<int:indice>", methods=["POST"])
def eliminar_empleado(indice):
    empleados = cargar_empleados()

    if 0 <= indice < len(empleados):
        empleados.pop(indice)
        guardar_empleados(empleados)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
