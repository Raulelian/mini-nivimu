# mini-nivimu

Mini aplicación de RRHH para aprender programación desde cero con Python, Flask, HTML, CSS y Git.

Proyecto guiado paso a paso con enfoque en buenas prácticas, lógica clara y preparación para integrar IA.

---

## 📌 Estado actual del proyecto

### 🟢 Nivel 1 — COMPLETADO
- Backend en Python:
  - Versión consola (`app.py`)
  - Versión web con Flask (`app_web.py`)
- CRUD completo de empleados:
  - Ver empleados
  - Añadir empleados
  - Eliminar empleados
- Persistencia de datos con archivo `empleados.json`
- Separación de responsabilidades:
  - Python → lógica
  - HTML → estructura
  - CSS → diseño
- Uso correcto de Git y GitHub con commits claros

---

### 🟡 Nivel 2 — EN PROGRESO AVANZADO
- Refactor del backend para mayor robustez
- Manejo de errores:
  - JSON vacío (`[]`)
  - Errores de lectura/escritura
- Validaciones de datos:
  - HTML (UX)
  - Flask (seguridad)
- Validación con expresiones regulares (regex):
  - Nombre y puesto solo texto
  - Edad numérica
- Frontend mejorado:
  - CSS limpio (sin duplicados)
  - Clases reutilizables (`.btn`, `.container`, `.form-group`)
  - Eliminación de estilos inline
- Buenas prácticas:
  - Código legible
  - No tocar lo que ya funciona
  - Mejorar antes que duplicar

---

### 🚀 Próximo paso — Nivel 3 (IA)
- Integrar IA en el proyecto:
  - Chatbot básico de RRHH
  - Procesamiento de texto (resúmenes y clasificación)
- Preparar el proyecto para crecimiento real

---

## ▶️ Cómo ejecutar el proyecto

1. Instalar dependencias:
```bash
pip install flask
