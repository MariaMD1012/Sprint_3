from conftest import *


def authorization_main_page(driver_to_use, email_user, password_user):
    driver_to_use.find_element(*AuthorizationForm.email).send_keys(email_user)
    driver_to_use.find_element(*AuthorizationForm.password).send_keys(password_user)
    driver_to_use.find_element(*AuthorizationForm.button_login).click()


def registration_main_page(driver_to_use, login_user, email_user, password_user):
    driver_to_use.find_element(*AuthorizationForm.login).send_keys(login_user)
    driver_to_use.find_element(*AuthorizationForm.email).send_keys(email_user)
    driver_to_use.find_element(*AuthorizationForm.password).send_keys(password_user)
    driver_to_use.find_element(*AuthorizationForm.register_button).click()
