import logging
import os

import pytest
from selenium import webdriver

from src.factory.file_factory import FileFactory
from src.pages.base_page import BasePage
from src.utilities.config_setup import ConfigSetup


class BrowserFactory:

    __config = ConfigSetup()

    resources_path = os.path.join(FileFactory.root_dir, 'utilities/resources/')
    chrome_driver_path = resources_path + "chromedriver"
    url = __config.get_base_url()

    with_docker = pytest.config.getoption("withdocker")

    if (eval(with_docker)):


        capabilities = {
            "browserName": "chrome",
            "version": "61.0",
            "enableVNC": True,
            "enableVideo": True
        }

        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities=capabilities)

    else:
        options = webdriver.ChromeOptions()
        options.add_argument('disable-infobars')
        driver = webdriver.Chrome(chrome_driver_path, chrome_options=options)
    base_page = BasePage(url, driver)
