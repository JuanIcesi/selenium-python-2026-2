import os
import time
from pathlib import Path

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service


DRIVER_PATH = Path(__file__).resolve().parents[1] / "chromedriver.exe"
os.environ["PATH"] = f"{DRIVER_PATH.parent}{os.pathsep}{os.environ.get('PATH', '')}"

FEATURES_WITH_OWN_DRIVER = {
    "lobby_login.feature",
    "login.feature",
    "shopping_cart.feature",
}


def create_chrome_driver(options):
    last_error = None
    for _ in range(3):
        try:
            service = Service(str(DRIVER_PATH))
            return webdriver.Chrome(service=service, options=options)
        except WebDriverException as error:
            last_error = error
            time.sleep(1)
    raise last_error


def before_scenario(context, scenario):
    feature_name = Path(context.feature.filename).name
    if feature_name in FEATURES_WITH_OWN_DRIVER:
        return

    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-first-run")
    options.add_argument("--lang=en-US")
    options.add_argument("--window-size=1440,1000")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/141.0.0.0 Safari/537.36"
    )

    context.driver = create_chrome_driver(options)
    context.driver.maximize_window()


def after_scenario(context, scenario):
    if Path(context.feature.filename).name == "shopping_cart.feature":
        return

    driver = getattr(context, "driver", None)
    if driver is not None:
        driver.quit()
