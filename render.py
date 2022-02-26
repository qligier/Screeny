#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Screeny project, 2022
import logging
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TickerXlHtmlRender:

    def __init__(self):
        self.windowWidth = 1448
        self.windowHeight = 1072

    def get_screenshot(self, html_file: str, dest_screenshot_file: str):
        opts = Options()
        opts.add_argument("--headless")
        opts.add_argument("--hide-scrollbars")
        opts.add_argument('--force-device-scale-factor=1')

        driver = webdriver.Chrome(options=opts)
        driver.set_window_rect(width=self.windowWidth, height=self.windowHeight)
        driver.get(html_file)
        sleep(1)
        driver.get_screenshot_as_file(dest_screenshot_file)
        driver.quit()

        logging.debug('Screenshot captured and saved to {}'.format(dest_screenshot_file))
