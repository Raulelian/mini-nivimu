# mini-nivimu

Mini app de RRHH para practicar Python y Flask.

## Funciones
- Ver lista de empleados desde la web
- Añadir empleados con formulario
- Eliminar empleados con un botón
- Guardado de datos en archivo JSON

## Estructura del proyecto
- app.py → versión consola
- app_web.py → versión web con Flask
- templates/ → archivos HTML
- empleados.json → datos de empleados

## Cómo ejecutar el proyecto
1. Instalar dependencias:
   pip install flask

2. Ejecutar la aplicación:
   python app_web.py

3. Abrir en el navegador:
   http://127.0.0.1:5000


## Últimos avances (UI y CSS)

- Conexión correcta  de archivos CSS en Flask
- Mejora visual de la lista de empleados
- Uso clases CSS reutilizables (.btn, .btn-danger)
- Alineación de texto y botones con Flexbox
- Separación clara entre HTML (ESTRUCTURA) y CSS ( ESTILOS)


## Bloque 1 - pulido final (Nivel 1)

- Corrección de errores en HTML
- Limpieza y organización del CSS
- Eliminación de estilos duplicados
- Mejoras de la experiencia de usuario:
- Configuración antes de eliminar empleados
- Codigo mas mantenible y profecional

Este bloque deja la aplicacion lista para ampliaciones (IA).


---

## Estado actual del proyecto

### Nivel 1 — Completado ✅
- Backend en Python (consola y web con Flask)
- CRUD completo de empleados:
  - Ver
  - Añadir
  - Eliminar
- Persistencia de datos con JSON
- Manejo correcto de JSON vacío (uso de `[]`)
- Frontend con HTML + CSS separados
- CSS limpio y organizado (sin duplicados)
- Buenas prácticas:
  - Sin estilos inline
  - Clases reutilizables
  - Separación de responsabilidades
- Uso de Git y GitHub con commits claros

### Nivel 2 — En progreso 🟡
- Preparación del proyecto para ampliaciones
- Refactor inicial del backend
- Enfoque en robustez, UX y mantenibilidad

### Próximo objetivo 🚀
- Integrar IA en el proyecto (Nivel 3):
  - Chatbot básico de RRHH
  - Procesamiento de texto (resúmenes y clasificación)


---

## Nivel 2 – Robustez del backend (en progreso)

### Manejo seguro de datos
- Lectura de empleados protegida contra errores:
  - Archivo JSON inexistente
  - Archivo JSON vacío o mal formado
- Uso de código defensivo para evitar caídas de la aplicación
- Inicialización automática con lista vacía (`[]`) cuando hay errores

Este paso garantiza que la aplicación siga funcionando
aunque los datos fallen, preparando el proyecto para crecer
y para integrar IA sin romper la base.
