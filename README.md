# Screeny project

This app runs on a [TickerXL](https://www.veeb.ch/store/p/tickerxl), a nice piece of hardware
by [Veeb](https://www.veeb.ch). It's a Raspberry Pi Zero WH that controls an e-paper screen of 1448 x 1072 pixel with 16
levels of gray, driven by the [IT8951](https://www.ite.com.tw/en/product/view?mid=95).

It's inspired by and partially forks the following projects.

1. [veebch/stonks](https://github.com/veebch/stonks) (GPL-3.0) for the code to properly manage the IT8951 controller and
   the button.
2. [speedyg0nz/MagInkCal](https://github.com/speedyg0nz/MagInkCal) (Apache-2.0) for the idea and code to create HTML
   pages, render them in a headless browser and create a screenshot that is finally displayed on the e-paper screen.

Some resources:

* [Updating your TickerXL](https://www.veeb.ch/updatexl).
* [gnzzz/IT8951](https://github.com/gnzzz/IT8951/tree/master). node.js package for e-papers controlled by IT8951.
* [speedyg0nz/MagInkCal](https://github.com/speedyg0nz/MagInkCal). E-Ink Magic Calendar that automatically syncs to
  Google Calendar.
* [Simple e-ink dashboard](https://core-electronics.com.au/projects/simple-e-ink-dashboard).
* [txoof/epd_display](https://github.com/txoof/epd_display). E Paper Display Loop
