from flask import Flask, render_template, request, redirect

import json

app = Flask(__name__)

# Cargar empleados desde el JSON
with open("empleados.json", "r", encoding="utf-8") as f:
    empleados = json.load(f)

@app.route("/")
def inicio():
    return render_template("index.html", empleados=empleados)


# Nueva ruta para añadir empleados

@app.route ("/nuevo", methods=["GET", "POST"])

def nuevo_empleado():
    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        puesto = request.form["puesto"]

        nuevo = {
            "Nombre": nombre,
            "Edad": edad,
            "Puesto": puesto
        }

        empleados.append(nuevo)

        with open("empleados.json", "w", encoding="utf-8") as f:
            json.dump(empleados, f, indent=4, ensure_ascii= False)


        return redirect("/")
    
    
    return render_template("nuevo.html")

@app.route("/eliminar/<int:indice>", methods=["POST"])
def eliminar_empleado(indice):

    empleados.pop(indice)

    with open("empleados.json", "w", encoding="utf-8") as f:
        json.dump(empleados, f, indent=4, ensure_ascii=False)

    return redirect("/")


# Arranque del servidor

if __name__ == "__main__":
    app.run(debug=True)
