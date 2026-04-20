# conftest.py
import json
from datetime import datetime

import pytest
import yaml
from playwright.sync_api import Playwright
import os
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="sit2", help="environment to run: sit1, sit2, dev, usccstg")

"""json data extractor"""
# def config_loader(env_name):
#     filepath = os.path.join("data", f"{env_name}.json")
#     with open(filepath, "r") as f:
#         return json.load(f)

""" YAML data extractor """
def config_loader(env_name):
    filepath = os.path.join("data", f"{env_name}.yaml")
    with open(filepath, "r") as f:
        return yaml.safe_load(f)

@pytest.fixture(scope="session", autouse=True)
def create_screenshort_folder(request):
    # Create a unique folder for this test run
    env_name = request.config.getoption("--env")
    screenshot_path = os.path.join("reports", f"run_{env_name}_{timestamp}")

    os.makedirs(screenshot_path, exist_ok=True)
    # Make the path available globally  to all tests via request.config
    request.config.run_dir = screenshot_path
    return screenshot_path


@pytest.fixture(scope="session")
def test_authenticate(playwright: Playwright, request):
    # auth = Authentication("SIT2")   # choose environment
    env_name = request.config.getoption("--env")
    conf = config_loader(env_name)
    browser = playwright.chromium.launch(headless=conf["headless"])
    context = browser.new_context()
    page = context.new_page()

    # login
    page.goto(conf["url"])
    page.get_by_label("Username or email *").fill(conf["username"])
    page.get_by_label("Password *").fill(conf["password"])
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_url("**/dashboard")  # waits for url with given pattern

    yield page

    # logout
    page.get_by_role("button", name=conf["username"]).click()
    page.get_by_role("menuitem", name="Logout").click()
    context.close()
    browser.close()













