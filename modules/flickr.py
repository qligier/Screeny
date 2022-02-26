#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Screeny project, 2022
import logging
import random

from flickrapi import FlickrAPI

from screenymodule import ScreenyModule


def make_photo_url(photo: any):
    return "https://live.staticflickr.com/{server}/{id}_{secret}_h.jpg".format(
        server=photo['server'], id=photo['id'], secret=photo['originalsecret'])


class ModuleFlickr(ScreenyModule):
    """The Flickr photo display module"""

    pictures = []

    def __init__(self, api_key: str, api_secret: str, user_id: str):
        self.api = FlickrAPI(api_key, api_secret, format='parsed-json')
        self.user_id = user_id

    def update_data(self):
        response = self.api.photos_search(user_id=self.user_id, per_page='100', extras='original_format')
        self.pictures = response['photos']['photo']
        logging.debug('Got {} photos'.format(len(self.pictures)))

    def get_picture(self) -> str | None:
        if not self.pictures:
            return None
        photo_url = make_photo_url(random.choice(self.pictures))
        logging.debug('Downloading photo')
        return ''
