# mini-nivimu

Mini aplicación de RRHH para aprender programación e integración de IA con Python y Flask.

---

## 🚀 Estado del proyecto

### ✅ Nivel 1 — Completado
- Backend en Python:
  - Versión consola (`app.py`)
  - Versión web con Flask (`app_web.py`)
- CRUD completo de empleados:
  - Ver empleados
  - Añadir empleados
  - Eliminar empleados
- Persistencia de datos con JSON
- Manejo correcto de JSON vacío (`[]`)
- Frontend con HTML + CSS separados
- CSS limpio y reutilizable
- Buenas prácticas:
  - Sin estilos inline
  - Clases reutilizables (`.btn`, `.btn-primary`, `.btn-danger`)
  - Separación de responsabilidades
- Uso de Git y GitHub con commits claros

---

### ✅ Nivel 2 — Completado
- Validaciones de formularios:
  - HTML (experiencia de usuario)
  - Flask (seguridad backend)
- Uso de expresiones regulares (regex)
- Manejo de errores con `try / except`
- Código más robusto y mantenible
- Control de errores en JSON (archivo vacío o inexistente)
- UX mejorada (mensajes de error claros)

---

### ✅ Nivel 3.1 — Completado (IA)
- Integración real de OpenAI API
- Configuración segura de API Key mediante variables de entorno
- Manejo de errores externos (rate limit, caídas de API)
- Endpoint de prueba `/test-ia`
- Chatbot de RRHH integrado en la web (`/chat`)
- Formulario de preguntas + respuesta visible en pantalla
- Contexto dinámico para evitar respuestas inventadas
- IA funcional y estable dentro de la aplicación web

---

## 🧠 Próximo objetivo — Nivel 3.2
- Procesamiento de texto con IA:
  - Resumir textos
  - Clasificar textos (vacaciones, horarios, bajas, etc.)
- Reutilizar el motor de IA ya integrado
- Ampliar el proyecto sin romper lo existente

---

## ▶️ Cómo ejecutar el proyecto

1. Instalar dependencias:
```bash
pip install flask openai
