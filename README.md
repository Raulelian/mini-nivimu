# mini-nivimu

Mini aplicación de RRHH para aprender programación e integración de IA con Python y Flask.

---

## 🚀 Estado del proyecto

### ✅ Nivel 1 — Completado
- Backend en Python:
  - Versión consola (`app.py`)
  - Versión web con Flask (`app_web.py`)
- CRUD completo de empleados:
  - Ver
  - Añadir
  - Eliminar
- Persistencia de datos con JSON
- Manejo correcto de JSON vacío (`[]`)
- Frontend con HTML + CSS separados
- CSS limpio, reutilizable y sin duplicados
- Buenas prácticas:
  - Sin estilos inline
  - Clases reutilizables (`.btn`, `.btn-primary`, `.btn-danger`)
  - Separación de responsabilidades
- Uso de Git y GitHub con commits claros

---

### 🟡 Nivel 2 — Completado
- Validaciones de formularios:
  - HTML (UX)
  - Flask (seguridad backend)
- Uso de expresiones regulares (regex)
- Manejo de errores con `try / except`
- Código más robusto y mantenible
- Confirmación de acciones críticas (eliminación)

---

### 🟢 Nivel 3.1 — En progreso (IA)
- Integración de OpenAI API
- Configuración segura de API Key con variables de entorno
- Endpoint de prueba `/test-ia`
- Manejo de errores externos (rate limit, caídas de API)
- Contexto dinámico para evitar respuestas inventadas
- IA responde correctamente sobre el proyecto

---

## 🧠 Próximo paso
- Crear interfaz web del chatbot de RRHH:
  - Formulario para preguntas
  - Respuesta visible en pantalla
- Cerrar Nivel 3.1
- Pasar a Nivel 3.2: procesamiento de texto con IA

---

## ▶️ Cómo ejecutar el proyecto

1. Instalar dependencias:
```bash
pip install flask openai
