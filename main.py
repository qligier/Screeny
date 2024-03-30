#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Screeny project, 2024
import logging
from os import path

import yaml

from modules.airthings import ModuleAirthings
from modules.flickr import ModuleFlickr
from modules.photo import ModulePhoto
from screenymodule import ScreenyModule


# from IT8951.display import AutoEPDDisplay


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

    # display = AutoEPDDisplay(vcom=config['display']['vcom'], spi_hz=24000000)
    # get_screenshot_for_page('page.html', 'page.png')

    modules: list[ScreenyModule] = []

    if config['photos']:
        modules.append(ModulePhoto(photo_files=config['photos']))

    if config['flickr']:
        modules.append(ModuleFlickr(api_key=config['flickr']['api_key'], api_secret=config['flickr']['api_secret'],
                                    user_id=config['flickr']['user_id']))

    if config['airthings']:
        modules.append(
            ModuleAirthings(api_id=config['airthings']['api_id'], api_secret=config['airthings']['api_secret'],
                            device_id=config['airthings']['device_id']))

    # while True:
    #     for i in range(0, len(modules)):
    #         module = modules[i]
    #         module.update_data()
    #         picture = module.get_picture()
    #         if picture:
    #             display_image_8bpp(display, picture)
    #             time.sleep(config['display']['delay'])

    airthings = ModuleAirthings(api_id=config['airthings']['api_id'], api_secret=config['airthings']['api_secret'],
                                device_id=config['airthings']['device_id'])
    airthings.update_data()
    airthings.get_picture()

    # picture = module_photo.get_picture()
    # display_image_8bpp(display, picture)

    # flickr = ModuleFlickr(config)
    # flickr.update_data()
    # flickr.get_picture()


if __name__ == '__main__':
    main()
