import pytest


def pytest_addoption(parser):
    parser.addoption("--selenium-host", action="store", default="localhost")

@pytest.fixture
def driver(request):
    selenium_host = request.config.getoption("--selenium-host")
    
    if selenium_host != "localhost":  # Mode Docker
        from selenium.webdriver.remote.webdriver import WebDriver
        capabilities = {
            "browserName": "chrome",
            "platformName": "Linux"
        }
        driver = WebDriver(
            command_executor=f"http://{selenium_host}:4444/wd/hub",
            desired_capabilities=capabilities
        )
    else:  # Mode local
        from selenium import webdriver
        from webdriver_manager.chrome import ChromeDriverManager
        driver = webdriver.Chrome(ChromeDriverManager().install())
    
    yield driver
    driver.quit()