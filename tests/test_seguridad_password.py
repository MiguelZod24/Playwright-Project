from playwright.sync_api import expect


def test_password_esta_enmascarado(page):
    """
    escenario: Se inspecciona el campo de contraseña para verificar que los caracteres queden ocultos al escribir.
    esperado: El campo de contraseña tiene configurado el tipo password, haciendo que los caracteres se muestren como puntos o asteriscos.
    impacto: Si falla, las contraseñas quedarían visibles en pantalla para cualquier persona cercana, representando un grave riesgo de privacidad y seguridad.
    accion: Corregir el atributo type del campo de contraseña en el formulario de login para que sea type=password.
    """
    page.goto("https://the-internet.herokuapp.com/login")

    expect(page.locator("#password")).to_have_attribute("type", "password")
