from flask import Flask, render_template, request, redirect

import json

import re

import os

from openai import OpenAI


app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- Configuración ---

RUTA_JSON = "empleados.json"

# --- Funciones IA ---

def preguntar_a_la_ia(pregunta: str) -> str:
    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=pregunta
        )

        # Forma correcta en la API nueva
        texto = response.output_text

        if texto:
            return texto.strip()

        return "La IA respondió, pero no devolvió texto."

    except Exception as e:
        return f"Error al contactar con la IA: {str(e)}"
    

def formatear_clasificacion(texto: str) -> str:

    """
    Fuerza el formato: CATEGORIA - EXPLICACION
    
    """

    if not texto :
        
        return ""
    
    limpio = texto.strip().replace("\n", " ")

    match = re.match(r"^\s*([A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+)\s*-\s*(.+)$", limpio)
    if not match:
        return limpio

    categoria = match.group(1).upper()
    explicacion = match.group(2).strip()

    categorias_validas = {"VACACIONES", "HORARIOS", "BAJAS", "OTROS"}
    if categoria not in categorias_validas:
        categoria = "OTROS"

    palabras = explicacion.split()
    if len(palabras) > 12:
        explicacion = " ".join(palabras[:12]) + "..."

    return f"{categoria} - {explicacion}"

        
    # --- Funciones datos ---

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

# --- RUTAS ---

@app.route("/")
def inicio():
    empleados = cargar_empleados()
    return render_template("index.html", empleados=empleados)

@app.route("/test-ia")

def test_ia():
    empleados = cargar_empleados()
        
    contexto = (
            "Mini Nivimu es una mini aplicación web de RRHH hecha con python y Flask. "
            "Permite ver una lista de empleados, añadir empleados y eliminar empleados. "
            "Los datos se guardan en un archivo JSON llamado empleados.json. "
            f"Ahora mismo hay {len(empleados)}empleados."
    )        

    pregunta = "Explica qué hace Mini Nivimu en frase corta y clara. "

    return preguntar_a_la_ia(f"{contexto}\n\nPregunta: {pregunta}")    


@app.route("/chat", methods=["GET", "POST"])
def chat():
    respuesta = None

    if request.method == "POST":
        pregunta = request.form.get("pregunta", "").strip()

        if pregunta:
            empleados = cargar_empleados()

            contexto = (
                "Mini Nivimu es una aplicación web de RRHH hecha con python y Flask."
                "Permite ver, añadir y eliminar empleados."
                f"Actualmente hay {len(empleados)} empleados registrados."
            
            )

            respuesta = preguntar_a_la_ia(
                f"{contexto}\n\nPregunta del usuario: {pregunta}"
            )

    return render_template("chat.html", respuesta = respuesta)        
            


@app.route( "/procesar-texto", methods=["GET", "POST"])
def procesar_texto():

    resultado = None
    texto_original = ""
    accion = "resumir"

    if request.method == "POST":
        texto_original = request.form.get("texto", "").strip()
        accion = request.form.get("accion", "resumir")

        if texto_original:
            if accion == "resumir":
                prompt = (
                    "Resume el siguiente texto en español, en 5-7 lineas,"
                    "Con un tono claro y sencillo:\n\n"
                    f"{texto_original}"

                )

            elif accion == "clasificar":
                prompt = (
                    "Vas a clasificar un texto de RRHH.\n"
                    "Categorías posibles: vacaciones, horarios, bajas, otros.\n\n"
                    "Responde en ESTE formato exacto, en una sola línea:\n"
                    "CATEGORIA - EXPLICACION\n\n"
                    "Reglas:\n"
                    "- CATEGORIA debe ser una de las 4 palabras exactas.\n"
                    "- EXPLICACION debe ser una frase corta (máx 12 palabras).\n"
                    "- No uses comillas. No uses saltos de línea.\n\n"
                    f"Texto:\n{texto_original}"



                )  

            else:
                prompt = texto_original

                 # ✅ Aquí se llama SIEMPRE a la IA

            resultado = preguntar_a_la_ia(prompt)

            if not resultado:
                resultado = "No llegó ningua respuesta de la IA ( resultado vacio)."

        else:
            
            resultado = "Pega un texto antes de procesar."        

    return render_template(
        "procesar_texto.html",
        resultado = resultado,
        texto = texto_original,
        accion = accion
    )                  



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

        if edad < 1 or edad > 99:
            return render_template("nuevo.html", error="Edad fuera de rango: usa un número entre 1 y 99.")

        empleados = cargar_empleados()

        nuevo = {"Nombre": nombre, "Edad": edad, "Puesto": puesto}
        empleados.append(nuevo)

        guardar_empleados(empleados)
       
        return redirect("/?mensaje=Empleado%20guardado%20con%20éxito")

    return render_template("nuevo.html")

@app.route("/eliminar/<int:indice>", methods=["POST"])
def eliminar_empleado(indice):
    empleados = cargar_empleados()

    if 0 <= indice < len(empleados):
        empleados.pop(indice)
        guardar_empleados(empleados)

    return redirect("/?mensaje=Empleado%20eliminado%20con%20éxito")

# --- Arranque del servidor ---

if __name__ == "__main__":
    app.run(debug=True)

