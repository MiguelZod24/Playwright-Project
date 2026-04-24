from playwright.sync_api import expect


def test_login_con_enter(page):
    """
    escenario: Un usuario completa sus credenciales y presiona la tecla Enter en lugar de hacer clic en el botón de acceso.
    esperado: El sistema procesa el login correctamente al presionar Enter, igual que si se hubiera hecho clic en el botón.
    impacto: Si falla, los usuarios que prefieren el teclado no podrían iniciar sesión cómodamente, afectando la usabilidad y accesibilidad de la plataforma.
    accion: Asegurarse de que el formulario responda correctamente a la tecla Enter mediante el atributo o evento correspondiente.
    """
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.press("#password", "Enter")

    expect(page.locator(".flash.success")).to_be_visible()
