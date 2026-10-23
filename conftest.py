import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from data.users import VALID_USER, UI_USER
from api.api_client import ClientAPI
from pages.login import LoginPage
from pages.inventory import InventoryPage
from utils.config.ui_config import BASE_URL


# ------------------------- Fixtures de API -------------------------

@pytest.fixture
def api_client():
    return ClientAPI()


@pytest.fixture
def authenticated_user(api_client):
    response = api_client.auth.login(VALID_USER)

    assert response.status_code == 200
    return api_client


# ------------------------- Fixtures de UI --------------------------

@pytest.fixture
def driver():
    """Crea un navegador nuevo por cada prueba y lo cierra al terminar.

    Al ser de alcance 'function', cada prueba recibe un navegador limpio,
    lo que garantiza que las pruebas UI sean independientes entre sí.
    """
    options = Options()
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture
def login_page(driver):
    """Navega a la página de login y expone el Page Object listo para usar."""
    driver.get(BASE_URL)
    return LoginPage(driver)


@pytest.fixture
def inventory_page(login_page):
    """Hace el login con el usuario válido y devuelve la página de inventario.

    Esta es la pieza clave: la dependencia 'login_page' obliga a que primero
    se abra el navegador y se cargue el login, y aquí se autentica. Las pruebas
    que necesiten estar logueadas solo piden 'inventory_page' y reciben la
    página de inventario ya cargada, sin repetir el login.
    """
    login_page.login(UI_USER["username"], UI_USER["password"])

    # Verificamos que el login realmente funcionó antes de entregar la página.
    assert "/inventory.html" in login_page.driver.current_url, (
        f"El login falló, URL actual: {login_page.driver.current_url}"
    )

    return InventoryPage(login_page.driver)
