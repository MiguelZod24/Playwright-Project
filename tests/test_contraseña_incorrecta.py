from playwright.sync_api import expect

# El "page" viene automaticamente de conftest.py que ya tengo
def test_login_exitoso(page):
    """
    escenario: Un usuario existente intenta ingresar con una contraseña incorrecta.
    esperado: El sistema rechaza el acceso y muestra un mensaje de error indicando que la contraseña no es válida.
    impacto: Si falla, el sistema podría estar permitiendo accesos con contraseñas incorrectas, representando un grave riesgo de seguridad.
    accion: Revisar el módulo de validación de contraseñas en el servicio de autenticación.
    """
    page.goto("https://the-internet.herokuapp.com/login")

    # Assert 1 — Verificar que los campos vienen vacíos al cargar la página
    expect(page.locator("#username")).to_be_empty()
    expect(page.locator("#password")).to_be_empty()

    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSuperSecretPassword!")

    # Assert 2 — Verificar que los campos tienen texto antes de hacer clic
    expect(page.locator("#username")).not_to_be_empty()
    expect(page.locator("#password")).not_to_be_empty()


    # Verificar que el botón de login está visible antes de hacer clic
    expect(page.locator("button[type='submit']")).to_be_visible()

    # Hacemos clic en el botón
    page.click("button[type='submit']")

    # Verificar que aparece el mensaje de error por contraseña incorrecta
    expect(page.locator(".flash.error")).to_be_visible()
