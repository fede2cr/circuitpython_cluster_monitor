'''
Circuitpython code for monitoring a set of VMs, and displaying it on a NeoPixel strip
'''

import ipaddress
import ssl
import time
import wifi
import socketpool
import adafruit_requests
import board
import neopixel

pixel_pin = board.NEOPIXEL
NUM_PIXELS = 1
pixels = neopixel.NeoPixel(
    pixel_pin, NUM_PIXELS, brightness=0.2,
)
pixels.fill((0, 0, 0))


pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

ipv4 = ipaddress.ip_address("192.168.42.54")

while True:
    ping_54 = wifi.radio.ping(ipv4)
    if ping_54 is not None and ping_54 < 0.3:
        pixels.fill((0, 255, 0))
    else:
        pixels.fill((255, 0, 0))
    time.sleep(5)
