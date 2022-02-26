#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Screeny project, 2022
from screenymodule import ScreenyModule
from os import popen
from PIL import Image, ImageDraw, ImageFont,  ImageOps


class ModuleWelcome(ScreenyModule):
    """The welcome module"""

    def __init__(self, config: any):
        pass
    
    def update_data(self):
        self.ssid = popen("sudo iwgetid -r").read()
    
    def get_picture(self) -> str:
        img = Image.new("RGB", (1448, 1072), color=(255, 255, 255))
        # img.thumbnail((display.width, display.height))
        # paste_coords = [dims[i] - img.size[i] for i in (0, 1)]
        return ''
        