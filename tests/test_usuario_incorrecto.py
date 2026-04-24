from playwright.sync_api import expect

def test_login_exitoso(page):
    """
    escenario: Un usuario intenta ingresar con un nombre de usuario que no existe en el sistema.
    esperado: El sistema rechaza el acceso y muestra un mensaje de error indicando que el usuario es inválido.
    impacto: Si falla, el sistema podría estar permitiendo accesos con usuarios inexistentes, representando un riesgo de seguridad.
    accion: Revisar el módulo de validación de usuarios en el servicio de autenticación.
    """
    page.goto("https://the-internet.herokuapp.com/login")

    # Assert 1 — Verificar que los campos vienen vacíos al cargar la página
    expect(page.locator("#username")).to_be_empty()
    expect(page.locator("#password")).to_be_empty()

    page.fill("#username", "tomsmithttt")
    page.fill("#password", "SuperSecretPassword!")

    # Assert 2 — Verificar que los campos tienen texto antes de hacer clic
    expect(page.locator("#username")).not_to_be_empty()
    expect(page.locator("#password")).not_to_be_empty()

    # Verificar que el botón de login está visible antes de hacer clic
    expect(page.locator("button[type='submit']")).to_be_visible()

    # Hacemos clic en el botón
    page.click("button[type='submit']")

    # Verificar que aparece el mensaje de error por usuario incorrecto
    expect(page.locator(".flash.error")).to_be_visible()