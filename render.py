#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Screeny project, 2022
import logging
from time import sleep

from IT8951 import constants
from IT8951.display import AutoEPDDisplay
from PIL import Image, ImageFilter
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from constants import Constants


def get_screenshot_from_page(html_file: str, dest_screenshot_file: str):
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--hide-scrollbars")
    opts.add_argument('--force-device-scale-factor=1')

    service = Service(executable_path='/usr/bin/chromedriver')

    driver = webdriver.Chrome(service=service, options=opts)
    driver.set_window_rect(width=Constants.SCREEN_WIDTH, height=Constants.SCREEN_HEIGHT)
    logging.info('Driver: getting {}'.format(html_file))
    driver.get('file://' + html_file)
    sleep(1)
    driver.get_screenshot_as_file(dest_screenshot_file)
    driver.quit()

    logging.debug('Screenshot captured and saved to {}'.format(dest_screenshot_file))


def display_image_8bpp(display: AutoEPDDisplay, img_file: str):
    logging.debug('Displaying picture {}'.format(img_file))
    dims = (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT)
    img = Image.open(img_file)
    if img.size[0] > Constants.SCREEN_WIDTH or img.size[1] > Constants.SCREEN_HEIGHT:
        img.thumbnail(dims, resample=Image.LANCZOS)
    paste_coords = [dims[i] - img.size[i] for i in (0, 1)]
    img = img.filter(ImageFilter.DETAIL)
    img = img.rotate(180, expand=True)
    display.frame_buf.paste(img, paste_coords)
    display.draw_full(constants.DisplayModes.GC16)
