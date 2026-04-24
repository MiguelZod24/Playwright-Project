from playwright.sync_api import expect


def test_login_solo_usuario(page):
    """
    escenario: Un usuario completa solo el campo de nombre de usuario y deja la contraseña vacía antes de intentar ingresar.
    esperado: El sistema muestra un mensaje de error indicando que la contraseña es requerida.
    impacto: Si falla, el formulario podría no estar validando correctamente cada campo por separado, causando comportamientos inesperados.
    accion: Revisar la validación individual de campos en el formulario de login.
    """
    page.goto("https://the-internet.herokuapp.com/login")

    page.fill("#username", "tomsmith")
    page.click("button[type='submit']")

    expect(page.locator(".flash.error")).to_be_visible()
