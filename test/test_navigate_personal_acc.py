from autorisation_form import *
from pages.helpers import wait_el


class TestNavigateToPersonalAccount:
    def test_navigate_to_pesronal_account_true(self, driver):
        driver.get(link)
        driver.find_element(*AppHeader.link_acc).click()
        wait_el(driver, AuthorizationForm.title_login_page)
        authorization_main_page(driver, email, password)
        wait_el(driver, MainPage.title_main_page)
        driver.find_element(*AppHeader.link_acc).click()
        current_url = driver.current_url
        assert current_url == link + 'account'
