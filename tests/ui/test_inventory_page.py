import pytest

from pages.inventory import InventoryPage


@pytest.mark.ui
class TestInventoryPage:
    """Cada prueba pide la fixture 'inventory_page', que ya entrega el
    navegador logueado en /inventory.html. Así no repetimos el login en
    cada prueba y cada una sigue siendo independiente."""

    def test_add_backpack_to_cart(self, driver, inventory_page):
        inventory_page.click_backpack_add_to_cart()

        assert inventory_page.get_cart_badge_text() == "1"
        assert inventory_page.is_remove_backpack_displayed()

    def test_remove_backpack_from_cart(self, driver, inventory_page):
        inventory_page.click_backpack_add_to_cart()
        inventory_page.click_remove_backpack_add_to_cart()

        assert inventory_page.is_cart_badge_displayed() is False

    def test_inventory_url_after_login(self, driver, inventory_page):
        assert "/inventory.html" in driver.current_url
