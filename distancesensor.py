import time
import board
import adafruit_hcsr04
import neopixel
colorwheel = 0
pixels = neopixel.NeoPixel.pixel_pin, num_pixels, brightness=.03; auto_write=False
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)


while True:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)

    def color_chase(color, wait):
        for i in range(num_pixels):
            pixels[i] = color
            time.sleep(wait)
            pixels.show(1)
        time.sleep(0.5)


    def rainbow_cycle(wait):
        for j in range(255):
            for i in range(num_pixels):
                rc_index = (i * 256 // num_pixels) + j
                pixels[i] = colorwheel(rc_index & 255)
                pixels.show()
                time.sleep(wait)


    RED = (255, 0, 0)
    YELLOW = (255, 150, 0)
    GREEN = (0, 255, 0)
    CYAN = (0, 255, 255)
    BLUE = (0, 0, 255)
    PURPLE = (180, 0, 255)

    while True:
        pixels.fill(RED)
        pixels.show(1)
    # Increase or decrease to change the speed of the solid color change.
        time.sleep(1)
        pixels.fill(GREEN)
        pixels.show(1)
        time.sleep(1)
        pixels.fill(BLUE)
        pixels.show(1)
        time.sleep(1)

        color_chase(RED, 0.1)  # Increase the number to slow down the color chase
        color_chase(YELLOW, 0.1)
        color_chase(GREEN, 0.1)
        color_chase(CYAN, 0.1)
        color_chase(BLUE, 0.1)
        color_chase(PURPLE, 0.1)
    1