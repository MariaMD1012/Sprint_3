from conftest import *


def wait_el(driver_to_use, locator):
    WebDriverWait(driver_to_use, 3).until(
        expected_conditions.visibility_of_element_located(locator))


def wait_url(driver_to_use, locator):
    WebDriverWait(driver_to_use, 3).until(
        expected_conditions.url_to_be(locator))
