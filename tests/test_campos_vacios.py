from playwright.sync_api import expect


def test_login_campos_vacios(page):
    """
    escenario: Un usuario presiona el botón de acceso sin completar ningún campo del formulario.
    esperado: El sistema muestra un mensaje de error indicando que los campos son obligatorios y no permite el ingreso.
    impacto: Si falla, el formulario podría no estar validando correctamente los campos vacíos, confundiendo al usuario final.
    accion: Revisar la validación de campos obligatorios en el formulario de login.
    """
    page.goto("https://the-internet.herokuapp.com/login")

    page.click("button[type='submit']")

    expect(page.locator(".flash.error")).to_be_visible()
