#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Screeny project, 2022
import abc


class ScreenyModule(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def update_data(self):
        pass

    @abc.abstractmethod
    def get_picture(self) -> str | None:
        pass
