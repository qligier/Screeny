# Screeny project

This app runs on a [TickerXL](https://www.veeb.ch/store/p/tickerxl), a nice piece of hardware
by [Veeb](https://www.veeb.ch). It's a Raspberry Pi Zero WH that controls an e-paper screen of 1448 x 1072 pixel with 16
levels of gray, driven by the [IT8951](https://www.ite.com.tw/en/product/view?mid=95).

It's inspired by and partially forks the following projects.

1. [veebch/stonks](https://web.archive.org/web/20230126164631/https://github.com/veebch/stonks) (GPL-3.0) for the code
   to properly manage the IT8951 controller and the button. It seems to have moved to
   [veebch/btcticker](https://github.com/veebch/btcticker).
2. [speedyg0nz/MagInkCal](https://github.com/speedyg0nz/MagInkCal) (Apache-2.0) for the idea and code to create HTML
   pages, render them in a headless browser and create a screenshot that is finally displayed on the e-paper screen.

Some resources:

* [Updating your TickerXL](https://www.veeb.ch/updatexl).
* [gnzzz/IT8951](https://github.com/gnzzz/IT8951/tree/master). node.js package for e-papers controlled by IT8951.
* [speedyg0nz/MagInkCal](https://github.com/speedyg0nz/MagInkCal). E-Ink Magic Calendar that automatically syncs to
  Google Calendar.
* [Simple e-ink dashboard](https://core-electronics.com.au/projects/simple-e-ink-dashboard).
* [txoof/epd_display](https://github.com/txoof/epd_display). E Paper Display Loop

## How to set up

Install [Raspberry Pi OS](https://www.raspberrypi.com/software/) on the microsd card.
Pre-configure it to connect to the WiFi network and allow SSH connections.

Once it is running:

```bash
# Update the OS
sudo apt-get update
sudo apt-get upgrade
sudo apt install git python3-pip chromium-chromedriver
sudo apt remove python3-rpi.gpio

# Install the screen library
sudo raspi-config nonint do_spi 0
git clone https://github.com/GregDMeyer/IT8951.git
cd IT8951
sudo pip3.10 install ./[rpi] --break-system-packages
cd ..

# Clone and install dependencies
git clone https://github.com/qligier/Screeny
cd ~/screeny
pip install -r requirements.txt --break-system-packages
cp config_example.yaml config.yaml

# We can now run Screeny!
python main.py
```

Add autostart:

```bash
cat <<EOF | sudo tee /etc/systemd/system/screeny.service
[Unit]
Description=screeny
After=network.target

[Service]
ExecStart=/usr/bin/python -u /home/quentin/screeny/main.py
WorkingDirectory=/home/quentin/screeny/
StandardOutput=inherit
StandardError=inherit
Restart=always
User=quentin

[Install]
WantedBy=multi-user.target
EOF
```

Start the service

```bash
sudo systemctl enable screeny.service
sudo systemctl start screeny.service
```