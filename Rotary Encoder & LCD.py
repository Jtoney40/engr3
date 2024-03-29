import rotaryio #takes code from files.
import board #takes code from files.
import neopixel #takes code from files.
import digitalio #takes code from files.
from lcd.lcd import LCD #tells you what file it takes the code from.
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface #tells you what file it takes the code from.

enc = rotaryio.IncrementalEncoder(board.D4, board.D3, divisor = 2) #tells you what pins it use and where to

lcd = LCD(I2CPCF8574Interface(board.I2C(), 0x27), num_rows = 2, num_cols = 16)

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.3
led[0] = (255, 0, 0)

button = digitalio.DigitalInOut(board.D2)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
button_state = None  

menu_index = 0


while True:
    menu_index = enc.position
    menu = ["stop", "caution", "go"]
    last_index = None
    menu[0] = "stop"
    menu[1] = "caution"
    menu[2] = "go"  
    menu_index_lcd = menu_index % 3
    lcd.set_cursor_pos(0,0)
    lcd.print("Push for: ")
    lcd.set_cursor_pos(1,0)
    lcd.print ("           ")
    lcd.set_cursor_pos(1,0)
    lcd.print(menu[menu_index_lcd])
    print(menu_index_lcd)
    if not button.value and button_state is None:
        button_state = "pressed"
    if button.value and button_state == "pressed":
        print("Button is pressed")
        button_state = None
    if menu_index_lcd == 0:
        led[0] = (255, 0, 0)
    if menu_index_lcd == 1:
        led[0] = (0, 255, 0)
    if menu_index_lcd == 2:
        led[0] = (255, 0, 255)

