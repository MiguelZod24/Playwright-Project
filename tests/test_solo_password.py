from playwright.sync_api import expect


def test_login_solo_password(page):
    """
    escenario: Un usuario completa solo el campo de contraseña y deja el nombre de usuario vacío antes de intentar ingresar.
    esperado: El sistema muestra un mensaje de error indicando que el nombre de usuario es requerido.
    impacto: Si falla, el formulario podría no estar validando correctamente cada campo por separado, causando errores inesperados.
    accion: Revisar la validación individual de campos en el formulario de login.
    """
    page.goto("https://the-internet.herokuapp.com/login")

    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")

    expect(page.locator(".flash.error")).to_be_visible()
