from playwright.sync_api import expect


def test_logout_exitoso(page):
    """
    escenario: Un usuario autenticado cierra su sesión haciendo clic en el botón de salida.
    esperado: El sistema cierra la sesión, redirige al formulario de login y muestra un mensaje de confirmación de cierre exitoso.
    impacto: Si falla, los usuarios no podrían cerrar su sesión correctamente, representando un riesgo de seguridad en dispositivos compartidos.
    accion: Verificar que el endpoint de logout funcione correctamente y que la sesión se invalide en el servidor.
    """
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")

    expect(page.locator(".flash.success")).to_be_visible()

    page.click("a[href='/logout']")

    expect(page).to_have_url("https://the-internet.herokuapp.com/login")
    expect(page.locator(".flash.success")).to_be_visible()
