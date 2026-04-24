from playwright.sync_api import expect

# El "page" viene automaticamente de conftest.py que ya tengo
def test_login_exitoso(page):
    """
    escenario: Un usuario con credenciales válidas intenta ingresar a la plataforma.
    esperado: El sistema acepta las credenciales y muestra un mensaje de bienvenida confirmando el acceso exitoso.
    impacto: Si falla, ningún usuario podría acceder a la plataforma. Impacto crítico en todos los usuarios.
    accion: Verificar que el servicio de autenticación esté operativo y que las credenciales de prueba sean válidas.
    """
    page.goto("https://the-internet.herokuapp.com/login")

    # Assert 1 — Verificar que los campos vienen vacíos al cargar la página
    expect(page.locator("#username")).to_be_empty()
    expect(page.locator("#password")).to_be_empty()

    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")

    # Assert 2 — Verificar que los campos tienen texto antes de hacer clic
    expect(page.locator("#username")).not_to_be_empty()
    expect(page.locator("#password")).not_to_be_empty()


    # Verificar que el botón de login está visible antes de hacer clic
    expect(page.locator("button[type='submit']")).to_be_visible()

    # Hacemos clic en el botón
    page.click("button[type='submit']")

    # 3. Verificar que el login fue exitoso
    expect(page.locator(".flash.success")).to_be_visible()
