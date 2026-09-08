# Desarrollo de una aplicación web con panel de administración

La empresa necesita una aplicación web que permita a los usuarios registrarse, iniciar sesión y gestionar sus perfiles. Además, se requiere un panel de administración para que los administradores puedan crear, leer, actualizar y eliminar usuarios. La aplicación debe manejar la autenticación y autorización de usuarios de manera segura.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Desarrollo de aplicaciones web con Django |
| **Nivel** | junior-l1 |
| **Tipo** | practical |
| **Tiempo estimado** | 20 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Configuración del proyecto y modelos

**Objetivo:** Configurar el proyecto Django y definir los modelos de usuario y perfil.

**Tiempo estimado:** 5 horas

**Instrucciones:**

- Configura un nuevo proyecto Django.
- Define los modelos de usuario y perfil, incluyendo campos como nombre, correo electrónico, contraseña y fecha de registro.
- Asegúrate de que los modelos soporten la autenticación y autorización de usuarios.

**Entregable:** Proyecto Django configurado con modelos de usuario y perfil definidos.

<details>
<summary>Pistas de conocimiento</summary>

- Considera la estructura de la base de datos y cómo los modelos se relacionan.
- Piensa en la seguridad de las contraseñas y cómo manejarlas en Django.

</details>

### Fase 2: Implementación de las vistas y templates

**Objetivo:** Crear las vistas y templates para el registro, inicio de sesión y gestión de perfiles de usuario.

**Tiempo estimado:** 7 horas

**Instrucciones:**

- Implementa las vistas para el registro, inicio de sesión y gestión de perfiles de usuario.
- Crea las templates correspondientes a cada vista.
- Asegúrate de que las vistas manejen correctamente los formularios y la lógica de autenticación.

**Entregable:** Vistas y templates implementadas para el registro, inicio de sesión y gestión de perfiles de usuario.

<details>
<summary>Pistas de conocimiento</summary>

- Considera la estructura de las URLs y cómo enrutar las vistas.
- Piensa en la validación de formularios y cómo manejar los errores.

</details>

### Fase 3: Desarrollo del panel de administración

**Objetivo:** Crear un panel de administración para gestionar usuarios.

**Tiempo estimado:** 6 horas

**Instrucciones:**

- Implementa el panel de administración utilizando Django Admin.
- Agrega funcionalidades para crear, leer, actualizar y eliminar usuarios.
- Asegúrate de que el panel de administración tenga las restricciones de acceso necesarias.

**Entregable:** Panel de administración implementado con funcionalidades para gestionar usuarios.

<details>
<summary>Pistas de conocimiento</summary>

- Considera las restricciones de acceso y cómo asegurarte de que solo los administradores puedan acceder al panel.
- Piensa en la estructura de las URLs y cómo enrutar las vistas del panel de administración.

</details>

### Fase 4: Pruebas y optimización

**Objetivo:** Realizar pruebas y optimizar la aplicación.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Realiza pruebas unitarias y de integración para asegurar la funcionalidad de la aplicación.
- Optimiza la aplicación para mejorar el rendimiento y la seguridad.
- Documenta el código y proporciona instrucciones de uso.

**Entregable:** Aplicación optimizada y documentada, lista para su despliegue.

<details>
<summary>Pistas de conocimiento</summary>

- Considera diferentes escenarios de prueba para asegurar la robustez de la aplicación.
- Piensa en las mejores prácticas para optimizar el rendimiento y la seguridad de la aplicación.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es Django y para qué se utiliza en el desarrollo de aplicaciones web?
- **paraQueSirve**: ¿Para qué sirve el panel de administración en una aplicación web?
- **comoSeUsa**: ¿Cómo se utiliza Django Admin para crear y gestionar usuarios?
- **erroresComunes**: ¿Cuáles son los errores comunes al implementar la autenticación y autorización en Django?
- **queDecisionesImplica**: ¿Qué decisiones implica el desarrollo de un panel de administración seguro y eficiente?

## Criterios de Evaluacion

- Configuración correcta del proyecto Django y definición de modelos.
- Implementación de vistas y templates funcionales para el registro, inicio de sesión y gestión de perfiles de usuario.
- Desarrollo de un panel de administración seguro y eficiente para gestionar usuarios.
- Realización de pruebas unitarias y de integración para asegurar la funcionalidad de la aplicación.
- Optimización y documentación del código para mejorar el rendimiento y la seguridad de la aplicación.

## Como trabajar con un asistente de IA

- **AGENTS.md** — instrucciones nativas del repo (Cursor, Codex, Copilot, Gemini, Claude Code). Abrí el proyecto y el agente las carga solo.
- **PROMPT_MEJORA.md** — el mismo prompt, para copiar y pegar en un chat (claude.ai, ChatGPT, etc.).

---

*Reto generado automaticamente por Challenge Generator - Pragma*
