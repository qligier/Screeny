#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Screeny project, 2022
import logging

from screenymodule import ScreenyModule


class ModulePhoto(ScreenyModule):
    """The simple photo display module"""

    def __init__(self, photo_files: list):
        self.photoFiles = photo_files
        self.index = len(self.photoFiles) - 1

    def update_data(self):
        self.index += 1
        if self.index >= len(self.photoFiles):
            self.index = 0

    def get_picture(self) -> str | None:
        if not self.photoFiles:
            return None
        logging.debug('Getting picture {}'.format(self.index))
        return self.photoFiles[self.index]
