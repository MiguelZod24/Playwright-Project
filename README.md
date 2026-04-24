# Playwright-Project

Suite de tests automatizados para validación de autenticación web, con pipeline CI/CD integrado y reporte HTML con envío automático por correo.

---

## Descripción

Este proyecto implementa una suite completa de tests de UI automation sobre el módulo de **Form Authentication** de [The Internet](https://the-internet.herokuapp.com), una aplicación de práctica para QA.

Los tests validan flujos críticos de login desde múltiples ángulos: casos exitosos, casos negativos y casos límite. El pipeline corre automáticamente en cada push y entrega el reporte directamente al correo.

---

## Stack tecnológico

| Herramienta | Versión | Uso |
|---|---|---|
| Python | 3.11 | Lenguaje base |
| Playwright | latest | Automatización de UI |
| Pytest | 9.x | Framework de testing |
| Pytest-HTML | 4.x | Generación de reportes |
| GitHub Actions | — | Pipeline CI/CD |

---

## Estructura del proyecto

```
Playwright-Project/
│
├── .github/
│   └── workflows/
│       └── tests.yml          # Pipeline CI/CD
│
├── tests/
│   ├── test_login_exitoso.py
│   ├── test_contraseña_incorrecta.py
│   ├── test_usuario_incorrecto.py
│   ├── test_campos_vacios.py
│   ├── test_logout.py
│   ├── test_seguridad_password.py
│   ├── test_solo_password.py
│   ├── test_solo_usuario.py
│   └── test_submit_con_enter.py
│
├── conftest.py                # Fixtures + captura de pantalla automática en fallos
├── pytest.ini                 # Configuración de Pytest
└── README.md
```

---

## Casos de prueba

| # | Test | Tipo | Descripción |
|---|---|---|---|
| 1 | `test_login_exitoso` | Happy path | Login con credenciales válidas |
| 2 | `test_contraseña_incorrecta` | Negativo | Login con password incorrecto |
| 3 | `test_usuario_incorrecto` | Negativo | Login con usuario inexistente |
| 4 | `test_campos_vacios` | Límite | Submit sin completar ningún campo |
| 5 | `test_solo_usuario` | Límite | Submit solo con usuario, sin password |
| 6 | `test_solo_password` | Límite | Submit solo con password, sin usuario |
| 7 | `test_logout` | Happy path | Cierre de sesión exitoso |
| 8 | `test_seguridad_password` | Seguridad | Verificar que el campo password está enmascarado |
| 9 | `test_submit_con_enter` | UX | Login usando tecla Enter en lugar del botón |

---

## Cómo ejecutar los tests localmente

### 1. Clonar el repositorio

```bash
git clone https://github.com/MiguelZod24/Playwright-Project.git
cd Playwright-Project
```

### 2. Instalar dependencias

```bash
pip install pytest playwright pytest-html
playwright install chromium
```

### 3. Ejecutar todos los tests

```bash
pytest --html=reporte.html --self-contained-html -v
```

### 4. Ver el reporte

Abre el archivo `reporte.html` generado en la raíz del proyecto con cualquier navegador.

---

## Pipeline CI/CD

El workflow de GitHub Actions se dispara automáticamente en cada `push` o `pull request` a `main`.

### Pasos del pipeline

```
1. Checkout del código
2. Configurar Python 3.11
3. Instalar dependencias
4. Instalar navegadores Playwright
5. Ejecutar los 9 tests
6. Subir reporte HTML como artefacto
7. Enviar reporte por correo automáticamente
```

### Artefactos

El reporte HTML queda disponible para descarga directamente desde la pestaña **Actions** de GitHub, en cada ejecución del pipeline.

---

## Captura de pantalla automática en fallos

El `conftest.py` está configurado para capturar automáticamente una screenshot cuando cualquier test falla. La captura se adjunta al reporte HTML junto con la URL del momento del fallo, facilitando el diagnóstico sin necesidad de reproducir el error manualmente.

---

## Reporte HTML

El reporte está diseñado con dos perspectivas:

- **Columna técnica** → para el equipo de QA: locator, error exacto, captura de pantalla
- **Columna de negocio** → para el Product Owner: descripción en lenguaje natural, impacto y acción recomendada

---

## Flujo de trabajo con IA

Este proyecto integra IA (Claude de Anthropic) como herramienta activa dentro del proceso de QA, no como reemplazo del criterio profesional sino como copiloto que acelera y enriquece el trabajo.

### ¿Qué rol tuvo la IA?

**Generación de casos de prueba**
A partir de la descripción del módulo a testear, la IA propuso casos de prueba cubriendo happy path, casos negativos y casos límite. El QA Engineer evaluó cada propuesta, descartó lo que no aplicaba y aprobó lo que sí tenía sentido para el contexto real.

**Análisis de fallos**
Cuando un test falló durante el desarrollo (por ejemplo, un locator incorrecto apuntando a `.flash.success` en lugar de `.flash.error`), la IA analizó el log de error, identificó la causa raíz y propuso la corrección. El QA Engineer validó el diagnóstico antes de aplicar el fix.

**Asistencia en configuración del pipeline**
El workflow de GitHub Actions y la configuración del envío de reportes por correo fueron construidos con asistencia de IA, iterando en base a los errores reales que devolvió el pipeline en cada ejecución.

### ¿Qué no hizo la IA?

- No tomó decisiones sobre qué casos de prueba eran relevantes para el negocio
- No definió la estrategia de testing ni la cobertura esperada
- No validó si los resultados eran correctos desde el punto de vista funcional
- No reemplazó el criterio del QA Engineer en ningún momento

### Por qué esto importa

Integrar IA en el flujo de QA es una habilidad emergente en la industria. Este proyecto documenta un flujo real donde la IA actúa como herramienta de productividad, mientras el profesional de QA mantiene el control, el criterio y la responsabilidad sobre la calidad del producto.

---

## Autor

**Miguel** — QA Automation Engineer  
Stack: Python · Playwright · Pytest · SQL · Postman · Swagger · JMeter · SonarQube · GitHub Actions

---

