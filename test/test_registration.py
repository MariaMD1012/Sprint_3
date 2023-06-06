from autorisation_form import *
from pages.helpers import wait_url


class TestRegistration:
    def test_register_new_user_true(self, driver):
        driver.get(link + 'register')
        registration_main_page(driver, fake_login, fake_email, fake_password)
        wait_url(driver, link + 'register')
        current_url = driver.current_url
        assert current_url == link + 'register'

    def test_register_new_user_incorrect_password(self, driver):
        driver.get(link + 'register')
        registration_main_page(driver, fake_login, fake_email, incorrect_password)
        error_tex = driver.find_element(*AuthorizationForm.password_fail).text
        assert error_tex == 'Некорректный пароль'
