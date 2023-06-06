from autorisation_form import *
from pages.helpers import wait_el
from utils import *


class TestLogin:
    def test_authorization_main_page_true(self, driver):
        driver.get(link)
        driver.find_element(*MainPage.button_login_acc).click()
        authorization_main_page(driver, email, password)
        wait_el(driver, MainPage.title_main_page)
        checkout_button = driver.find_element(*MainPage.button_checkout).text
        assert checkout_button == 'Оформить заказ'

    def test_authorization_personal_account_true(self, driver):
        driver.get(link)
        driver.find_element(*AppHeader.link_acc).click()
        authorization_main_page(driver, email, password)
        wait_el(driver, MainPage.title_main_page)
        checkout_button = driver.find_element(*MainPage.button_checkout).text
        assert checkout_button == 'Оформить заказ'

    def test_authorization_button_registration_form_true(self, driver):
        driver.get(link + 'register')
        driver.find_element(*AuthorizationForm.button_login_reg_form).click()
        authorization_main_page(driver, email, password)
        wait_el(driver, MainPage.title_main_page)
        checkout_button = driver.find_element(*MainPage.button_checkout).text
        assert checkout_button == 'Оформить заказ'

    def test_authorization_by_the_password_setting_button_true(self, driver):
        driver.get(link + 'login')
        driver.find_element(*AuthorizationForm.button_password_setting).click()
        driver.find_element(*AuthorizationForm.button_login_reg_form).click()
        authorization_main_page(driver, email, password)
        wait_el(driver, MainPage.title_main_page)
        checkout_button = driver.find_element(*MainPage.button_checkout).text
        assert checkout_button == 'Оформить заказ'
