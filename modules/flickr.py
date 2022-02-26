#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Screeny project, 2022
import logging
from flickrapi import FlickrAPI
from screenymodule import ScreenyModule
import random


class ModuleFlickr(ScreenyModule):
    """The Flickr photo display module"""

    pictures = []

    def __init__(self, config: any):
        logging.debug('Initializing Flickr with {}'.format(config['flickr']))
        self.api = FlickrAPI(config['flickr']['api_key'], config['flickr']['api_secret'], format='parsed-json')
        self.user_id = config['flickr']['user_id']

    def update_data(self):
        response = self.api.photos_search(user_id=self.user_id, per_page='100', extras='original_format')
        self.pictures = response['photos']['photo']
        logging.debug('Got {} photos'.format(len(self.pictures)))

    def get_picture(self) -> str:
        photo_url = self.make_photo_url(random.choice(self.pictures))
        logging.debug('Downloading photo {}'.format(photo_url))
        return ''

    def make_photo_url(self, photo: any):
        return "https://live.staticflickr.com/{server}/{id}_{secret}_h.jpg".format(
            server=photo['server'], id=photo['id'], secret=photo['originalsecret'])
