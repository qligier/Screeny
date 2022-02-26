#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Screeny project, 2022
import logging
import time
from os import path

import yaml
from IT8951.display import AutoEPDDisplay

from modules.flickr import ModuleFlickr
from modules.photo import ModulePhoto
from render import display_image_8bpp
from screenymodule import ScreenyModule


def load_config(config_file: str) -> any:
    logging.debug("Loading config from file {}".format(config_file))
    with open(config_file, 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
    logging.info("Read Config File")
    logging.info(config)
    return config


def main():
    logging.basicConfig(level=logging.DEBUG)
    config = load_config(config_file=path.join(path.dirname(__file__), 'config.yaml'))

    display = AutoEPDDisplay(vcom=config['display']['vcom'], spi_hz=24000000)
    # get_screenshot_for_page('page.html', 'page.png')

    modules: list[ScreenyModule] = []

    if config['photos']:
        modules.append(ModulePhoto(photo_files=config['photos']))

    if config['flickr']:
        modules.append(ModuleFlickr(api_key=config['flickr']['api_key'], api_secret=config['flickr']['api_secret'],
                                    user_id=config['flickr']['user_id']))

    while True:
        for i in range(0, len(modules)):
            module = modules[i]
            module.update_data()
            picture = module.get_picture()
            if picture:
                display_image_8bpp(display, picture)
                time.sleep(config['display']['delay'])

    # picture = module_photo.get_picture()
    # display_image_8bpp(display, picture)

    # flickr = ModuleFlickr(config)
    # flickr.update_data()
    # flickr.get_picture()


if __name__ == '__main__':
    main()
