
import pytest
from selenium import webdriver



@pytest.fixture(scope="function")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    request.cls.driver = driver
    yield
    driver.quit()
