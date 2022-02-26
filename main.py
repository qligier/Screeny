#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Screeny project, 2022
import time

from IT8951.display import AutoEPDDisplay
from IT8951 import constants
import logging
import yaml
from os import path
from PIL import Image

from modules.flickr import ModuleFlickr
from modules.photo import ModulePhoto
from render import TickerXlHtmlRender
from screenymodule import ScreenyModule


def load_config(config_file: str) -> any:
    logging.debug("Loading config from file {}".format(config_file))
    with open(config_file, 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    logging.info("Read Config File")
    logging.info(config)
    return config


def display_image_8bpp(display: AutoEPDDisplay, img_file: str):
    logging.debug('Displaying picture {}'.format(img_file))
    dims = (display.width, display.height)
    img = Image.open(img_file)
    img.thumbnail(dims)
    paste_coords = [dims[i] - img.size[i] for i in (0, 1)]
    img = img.rotate(180, expand=True)
    display.frame_buf.paste(img, paste_coords)
    display.draw_full(constants.DisplayModes.GC16)


def main():
    logging.basicConfig(level=logging.DEBUG)
    config = load_config(config_file=path.join(path.dirname(__file__), 'config.yaml'))

    display = AutoEPDDisplay(vcom=config['display']['vcom'], spi_hz=24000000)
    html_render = TickerXlHtmlRender()
    # html_render.get_screenshot('page.html', 'page.png')

    modules: list[ScreenyModule] = []

    if config['photos']:
        modules.append(ModulePhoto(config['photos']))

    while True:
        for i in range(0, len(modules)):
            module = modules[i]
            module.update_data()
            picture = module.get_picture()
            display_image_8bpp(display, picture)
            time.sleep(config['display']['delay'])


    # picture = module_photo.get_picture()
    # display_image_8bpp(display, picture)

    # flickr = ModuleFlickr(config)
    # flickr.update_data()
    # flickr.get_picture()


if __name__ == '__main__':
    main()
