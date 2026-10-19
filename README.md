 UI Automation Framework

Framework de automatización de pruebas **reutilizable**, pensado como proyecto base para
validar tanto **APIs REST** como **interfaces web**. Está construido con **Python + pytest**
y sigue patrones que facilitan extenderlo a nuevos servicios sin reescribir la lógica común.

El proyecto se apoya en dos aplicaciones públicas de práctica:

- **API:** [DummyJSON](https://dummyjson.com) — API REST de prueba (productos, usuarios, autenticación JWT).
- **UI:** [SauceDemo](https://www.saucedemo.com) — tienda de ejemplo para automatizar flujos web con Selenium.

---

## Objetivo del proyecto

Construir un framework de automatización que sirva como **plantilla profesional reutilizable**,
demostrando buenas prácticas de QA Automation:

- **Separación por capas:** los tests describen *qué* se valida; la lógica de interacción vive en
  wrappers y Page Objects.
- **Pruebas independientes:** cada caso se ejecuta de forma aislada. Las pruebas de UI no dependen
  del orden ni del estado dejado por otra prueba, porque un *fixture* prepara el login automáticamente.
- **Reutilización:** datos de prueba centralizados, validadores de contrato reutilizables,
  clientes HTTP y Page Objects compartidos.
- **Trazabilidad:** marcadores (`markers`) por módulo y reporte HTML automático.

El resultado es un esqueleto que se puede apuntar a otra API o a otro sitio web cambiando
únicamente la configuración y los Page Objects.

---

## Stack tecnológico

| Área | Herramienta |
|---|---|
| Lenguaje | Python 3.9+ |
| Framework de pruebas | pytest |
| Pruebas de API | requests |
| Pruebas de UI | Selenium WebDriver |
| Gestión del driver | webdriver-manager |
| Reportes | pytest-html |
| IDE recomendado | PyCharm |

---

## Requisitos

- Python 3.9 o superior.
- pip.
- **Google Chrome** instalado (necesario para las pruebas de UI).

---

## Instalación

```bash
# 1. Crear y activar el entorno virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/macOS

# 2. Instalar dependencias
pip install -r requirements.txt
```

---

## Cómo ejecutar las pruebas

```bash
# Toda la suite (API + UI)
pytest

# Solo pruebas de API
pytest tests/api

# Solo pruebas de UI
pytest tests/ui

# Un módulo específico
pytest tests/api/test_products.py
pytest tests/ui/test_inventory_page.py

# Un caso específico
pytest tests/api/test_auth.py::test_success_login

# Por marcador
pytest -m ui
pytest -m smoke
```

Marcadores disponibles (definidos en `pytest.ini`):

| Marcador | Descripción |
|---|---|
| `smoke` | Pruebas de humo para verificar que el sistema responde. |
| `auth` | Pruebas del módulo de autenticación. |
| `products` | Pruebas del módulo de productos. |
| `users` | Pruebas del módulo de usuarios. |
| `ui` | Pruebas de interfaz web con Selenium. |

> **Reporte HTML:** al finalizar cualquier ejecución se genera `reports/report.html`
> (autocontenido). Ábrelo en el navegador para ver el detalle de resultados.

---

## Estructura del proyecto

```
API-UI-AUTOMATION-master/
├── api/                          # Capa de acceso a la API
│   ├── api_base.py               # Métodos HTTP genéricos (GET/POST/PUT/PATCH/DELETE)
│   ├── api_client.py             # Ensambla la sesión y expone los recursos
│   ├── api_auth.py               # Login/logout/current_user y manejo del JWT
│   ├── api_products.py           # Endpoints de /products
│   └── api_users.py              # Endpoints de /users
├── data/                         # Datos de prueba centralizados
│   └── users.py                  # Credenciales y payloads (API y UI)
├── pages/                        # Page Objects (patrón Page Object Model)
│   ├── login.py                  # Página de login de SauceDemo
│   └── inventory.py              # Página de inventario/productos de SauceDemo
├── tests/                        # Casos de prueba
│   ├── api/                      # Pruebas de API
│   │   ├── test_auth.py
│   │   ├── test_products.py
│   │   └── test_users.py
│   └── ui/                       # Pruebas de UI (Selenium)
│       ├── test_login_page.py
│       └── test_inventory_page.py
├── utils/
│   ├── config.py                 # Configuración (URLs, headers, tiempos)
│   └── validators.py             # Validaciones de contrato reutilizables
├── reports/                      # Reportes HTML generados
├── conftest.py                   # Fixtures compartidas (API y UI)
├── pytest.ini                    # Configuración de pytest y marcadores
├── requirements.txt
└── README.md
```

---

## Arquitectura

El framework separa tres responsabilidades:

1. **Capa de interacción** (`api/` y `pages/`): sabe *cómo* hablar con la aplicación.
   No contiene aserciones.
2. **Capa de datos** (`data/`): centraliza credenciales y payloads reutilizables.
3. **Capa de pruebas** (`tests/`): describe *qué* se espera. Usa fixtures y validadores.

```
tests/  ──usa──>  conftest.py (fixtures)  ──construye──>  api/  ó  pages/
   │                                                             │
   └──────────────usa──>  utils/validators.py  <──config──  utils/config.py
```

### Capa de API

- `BaseAPI` (`api/api_base.py`): métodos HTTP genéricos. Cada recurso hereda de ella.
- `ClientAPI` (`api/api_client.py`): crea una `requests.Session` reutilizable, carga los headers
  por defecto y expone los recursos como atributos: `client.auth`, `client.users`, `client.products`.
- `AuthAPI` guarda el token JWT automáticamente en la sesión tras un login exitoso, de modo que
  las siguientes peticiones ya van autenticadas.

### Capa de UI — Page Object Model

Cada página de la web se representa con una **clase Page Object** que:

- Declara los **localizadores** como atributos de clase (tuplas `By`).
- Expone **acciones** (métodos) con nombres legibles: `click_login_button`, `set_username`, etc.
- **No contiene `assert`**: las aserciones viven en los tests.

Los Page Objects reciben el `driver` en el constructor (`__init__(self, driver)`), por lo que son
totalmente reutilizables y no crean el navegador por su cuenta.

---

## Fixtures (`conftest.py`)

Las fixtures son la columna vertebral del framework: preparan el estado antes de cada prueba y
lo limpian después. Están definidas en `conftest.py` y disponibles para todos los tests.

### Fixtures de API

| Fixture | Depende de | Descripción |
|---|---|---|
| `api_client` | — | Devuelve una instancia de `ClientAPI` con sesión HTTP lista para usar. |
| `authenticated_user` | `api_client` | Hace login con `VALID_USER` y devuelve el cliente **con el token JWT ya cargado**. |

### Fixtures de UI

| Fixture | Depende de | Descripción |
|---|---|---|
| `driver` | — | Crea un navegador Chrome nuevo y lo cierra al terminar. Es de **alcance `function`**: cada prueba recibe un Chrome limpio. |
| `login_page` | `driver` | Navega a `BASE_URL_UI` y devuelve un `LoginPage` listo para usar. |
| `inventory_page` | `login_page` | Realiza el login con `UI_USER`, verifica que se llegó a `/inventory.html` y devuelve un `InventoryPage` **ya autenticado**. |

### La clave: pruebas UI independientes

El problema que resuelve `inventory_page` es que la página de inventario **solo es accesible tras
haber iniciado sesión**. En lugar de repetir el login en cada test (o de depender del orden de
ejecución), la fixture encadena el flujo completo:

```
driver  →  login_page  →  inventory_page
(Chrome)   (abre /)       (hace login → devuelve /inventory.html)
```

Cuando un test pide `inventory_page`, pytest construye automáticamente toda la cadena y le entrega
el Page Object listo. Como el `driver` es de alcance `function`, **cada prueba obtiene su propio
navegador y su propio login**, garantizando independencia total:

```python
def test_add_backpack_to_cart(self, driver, inventory_page):
    inventory_page.click_backpack_add_to_cart()
    assert inventory_page.get_cart_badge_text() == "1"
```

> Si más adelante necesitas acelerar la suite, se puede cambiar el `driver` a
> `scope="session"` (un solo navegador para toda la ejecución) manteniendo el login por prueba.
> El trade-off es velocidad vs. aislamiento.

---

## Funciones de UI (Page Objects)

### `pages/login.py` — `LoginPage`

Representa la página de inicio de sesión de SauceDemo (`https://www.saucedemo.com/`).

**Localizadores**

| Atributo | Selector |
|---|---|
| `username_field` | `By.ID, 'user-name'` |
| `password_field` | `By.ID, 'password'` |
| `login_button` | `By.ID, 'login-button'` |

**Métodos**

| Método | Parámetros | Descripción |
|---|---|---|
| `__init__(driver)` | `driver` | Guarda el navegador. No crea el driver. |
| `set_username(username)` | `username: str` | Espera el campo de usuario y escribe el valor. |
| `set_password(password)` | `password: str` | Espera el campo de contraseña y escribe el valor. |
| `get_username()` | — | Devuelve el texto actual del campo de usuario (útil para verificar el ingreso). |
| `click_login_button()` | — | Espera el botón de login y hace clic. |
| `login(username, password)` | `username: str, password: str` | **Acción completa**: usuario + contraseña + clic. Reutilizada por la fixture `inventory_page` para autenticar antes de cada prueba. |

**Ejemplo de uso**

```python
login_page.set_username("standard_user")
login_page.set_password("secret_sauce")
login_page.click_login_button()

# O en una sola línea:
login_page.login("standard_user", "secret_sauce")
```

---

### `pages/inventory.py` — `InventoryPage`

Representa la página de inventario de SauceDemo (`/inventory.html`), accesible **solo después
del login**. Gestiona el catálogo de productos y el botón de añadir/quitar del carrito.

**Localizadores**

| Atributo | Selector | Elemento |
|---|---|---|
| `backpack_add_to_cart` | `By.ID, 'add-to-cart-sauce-labs-backpack'` | Botón "Add to cart" de la mochila. |
| `backpack_remove` | `By.ID, 'remove-sauce-labs-backpack'` | Botón "Remove" de la mochila. |
| `burger_menu` | `By.ID, 'react-burger-menu-btn'` | Menú lateral. |
| `shopping_cart` | `By.CLASS_NAME, 'shopping_cart_link'` | Ícono del carrito. |
| `shopping_cart_badge` | `By.CLASS_NAME, 'shopping_cart_badge'` | Contador de ítems del carrito. |

**Métodos**

| Método | Parámetros | Descripción |
|---|---|---|
| `__init__(driver)` | `driver` | Guarda el navegador y crea un `WebDriverWait` de 10 s reutilizable. |
| `click_backpack_add_to_cart()` | — | Espera a que el botón "Add to cart" sea clickeable y lo pulsa. |
| `click_remove_backpack_add_to_cart()` | — | Espera a que el botón "Remove" sea clickeable y lo pulsa. |
| `get_cart_badge_text()` | — | Devuelve el texto del contador del carrito (p. ej. `"1"`). Espera a que sea visible. |
| `is_cart_badge_displayed()` | — | `True` si el contador existe, `False` si no. Usa `find_elements` para no lanzar excepción cuando el carrito está vacío. |
| `is_remove_backpack_displayed()` | — | `True` si el botón "Remove" es visible (el producto fue añadido). |

**Ejemplo de uso**

```python
# La fixture ya entrega la página logueada
inventory_page.click_backpack_add_to_cart()
assert inventory_page.get_cart_badge_text() == "1"
assert inventory_page.is_remove_backpack_displayed()

inventory_page.click_remove_backpack_add_to_cart()
assert inventory_page.is_cart_badge_displayed() is False
```

**Esperas explícitas:** todos los métodos usan `WebDriverWait` + `expected_conditions`, por lo que
no dependen de `sleep()` y toleran la carga dinámica de la página.

---

## Validadores de API (`utils/validators.py`)

Funciones reutilizables que verifican la **forma** (contrato) de las respuestas, evitando repetir
aserciones en cada test:

| Función | Qué verifica |
|---|---|
| `assert_response_time(response)` | Que la respuesta llegó dentro de `MAX_RESPONSE_TIME_SECONDS`. |
| `assert_product_structure(product)` | Claves y tipos de un producto. |
| `assert_product_list_structure(data)` | Estructura de un listado paginado de productos. |
| `assert_category_structure(category)` | Claves y tipos de una categoría. |
| `assert_empty_response(data)` | Respuesta de búsqueda de productos sin resultados. |
| `assert_user_structure(data)` | Claves y tipos de un usuario. |
| `assert_users_list_structure(data)` | Estructura de un listado paginado de usuarios. |
| `assert_empty_user_response(data)` | Respuesta de búsqueda de usuarios sin resultados. |
| `assert_carts_structure(data)` | Estructura de los carritos de un usuario. |

---

## Configuración

La configuración vive en `utils/config.py` y puede sobrescribirse con variables de entorno:

| Variable | Descripción | Valor por defecto |
|---|---|---|
| `BASE_URL` | URL base de la API. | `https://dummyjson.com` |
| `MAX_RESPONSE_TIME_SECONDS` | Tiempo máximo de respuesta aceptado. | `3` |

Valores fijos de UI:

| Constante | Valor |
|---|---|
| `BASE_URL_UI` | `https://www.saucedemo.com/` |

---

## Datos de prueba (`data/users.py`)

| Constante | Uso |
|---|---|
| `VALID_USER` | Usuario válido para login de la API (DummyJSON). |
| `INVALID_USER` | Usuario inválido para probar login fallido. |
| `ADD_USER` | Payload para crear un usuario. |
| `UPDATE_USER_PAYLOAD` | Payload para actualizar un usuario. |
| `UI_USER` | Credenciales del usuario de SauceDemo para las pruebas de UI. |

---

## Cómo agregar un nuevo recurso de API

Ejemplo con el recurso `cart`:

1. **Crear el wrapper** en `api/api_carts.py` heredando de `BaseAPI`:

   ```python
   from api.api_base import BaseAPI

   class CartsAPI(BaseAPI):
       def get_all_carts(self, params=None):
           return self.GET('/carts', params=params)

       def get_cart_by_id(self, cart_id):
           return self.GET(f'/carts/{cart_id}')
   ```

2. **Registrarlo** en `api/api_client.py`:

   ```python
   self.carts = CartsAPI(self.session, self.base_url)
   ```

3. **Agregar datos de prueba** en `data/` si hacen falta.

4. **Crear los tests** en `tests/api/test_carts.py` usando la fixture `api_client`.

5. **Agregar un marcador** en `pytest.ini` si quieres filtrarlos por módulo.

---

## Cómo agregar una nueva página de UI

1. **Crear el Page Object** en `pages/` con los localizadores y acciones de la vista:

   ```python
   from selenium.webdriver.common.by import By
   from selenium.webdriver.support import expected_conditions as EC
   from selenium.webdriver.support.wait import WebDriverWait


   class CartPage:
       checkout_button = (By.ID, 'checkout')

       def __init__(self, driver):
           self.driver = driver
           self.wait = WebDriverWait(driver, 10)

       def click_checkout(self):
           self.wait.until(EC.element_to_be_clickable(self.checkout_button)).click()
   ```

2. **Exponerla con una fixture** en `conftest.py` si necesita preparación (login, navegación):

   ```python
   @pytest.fixture
   def cart_page(inventory_page):
       inventory_page.driver.get("https://www.saucedemo.com/cart.html")
       return CartPage(inventory_page.driver)
   ```

3. **Escribir el test** en `tests/ui/`, marcándolo con `@pytest.mark.ui`.

---

## Notas y buenas prácticas

- Las credenciales de `data/users.py` son de las aplicaciones de demostración
  (DummyJSON y SauceDemo). En un entorno real, muévelas a variables de entorno o a un
  gestor de secretos.
- Las pruebas de UI requieren Chrome instalado; `webdriver-manager` descarga el driver
  compatible automáticamente.
- Los Page Objects **nunca** deben contener `assert`; las validaciones pertenecen a los tests.
- Prefiere esperas explícitas (`WebDriverWait`) sobre `time.sleep()`.
- Ejecuta `pytest -m ui` o `pytest tests/ui` cuando solo quieras validar la interfaz y ahorrar tiempo.
