#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Screeny project, 2024
import logging
import os
import tempfile
from typing import TextIO

import requests
from requests import HTTPError

import render
from screenymodule import ScreenyModule


def make_photo_url(photo: any):
    return "https://live.staticflickr.com/{server}/{id}_{secret}_h.jpg".format(
        server=photo['server'], id=photo['id'], secret=photo['originalsecret'])


class ModuleAirthings(ScreenyModule):
    """The Airthings measure display module"""

    authorisation_url = "https://accounts-api.airthings.com/v1/token"

    token_req_payload = {
        "grant_type": "client_credentials",
        "scope": "read:device:current_values",
    }

    co2_level = -1
    radon_level = -1
    pm1_level = -1
    pm2_5_level = -1
    voc_level = -1
    humidity = -1
    temperature = -1.0

    def __init__(self, api_id: str, api_secret: str, device_id: str):
        self.api_id = api_id
        self.api_secret = api_secret
        self.device_id = device_id
        self.device_url = f"https://ext-api.airthings.com/v1/devices/{device_id}/latest-samples"

    def update_data(self):
        self.co2_level = -1
        self.radon_level = -1
        self.pm1_level = -1
        self.pm2_5_level = -1
        self.voc_level = -1
        self.humidity = -1
        self.temperature = -1.0

        # Access Token
        try:
            token_response = requests.post(
                self.authorisation_url,
                data=self.token_req_payload,
                allow_redirects=False,
                auth=(self.api_id, self.api_secret),
            )
        except HTTPError as e:
            logging.error(e)
            return
        token = token_response.json()["access_token"]

        # Get the latest data for the device
        try:
            response = requests.get(url=self.device_url, headers={"Authorization": f"Bearer {token}"})
        except HTTPError as e:
            logging.error(e)
            return

        data = response.json()['date']
        # print(response.text)
        self.co2_level = data['co2']
        self.radon_level = data['radonShortTermAvg']
        self.pm1_level = data['pm1']
        self.pm2_5_level = data['pm25']
        self.voc_level = data['voc']
        self.humidity = data['humidity']
        # Pressure: data['pressure']
        self.temperature = data['temp']
        # Update time: data['time']

    def get_picture(self) -> str | None:
        html_file, html_path = tempfile.mkstemp(suffix=".html", text=True)
        png_file, png_path = tempfile.mkstemp(suffix=".png", text=False)
        with os.open(html_file) as tmp:
            self.create_html_page(tmp)
            render.get_screenshot_from_page(html_path, png_path)
        return png_path

    def create_html_page(self, output: TextIO) -> None:
        split_num = str(self.temperature).split('.')
        temp_int = split_num[0]
        temp_dec = split_num[1]
        with open("views/template_airthings.html") as template_file:
            html = (template_file.read()
                    .replace('{$CO2}', str(self.co2_level))
                    .replace('{$VOC}', str(self.voc_level))
                    .replace('{$PM1}', str(self.pm1_level))
                    .replace('{$PM25}', str(self.pm2_5_level))
                    .replace('{$RADON}', str(self.radon_level))
                    .replace('{$HUM}', str(self.humidity))
                    .replace('{$TEMP_INT}', temp_int)
                    .replace('{$TEMP_DEC}', temp_dec)
                    )
            output.write(html)
            return
