# CircuitPython
This repository will actually serve as an aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [circuitpython_neopixle_with_distancesensor](#circuitpython_neopixle_sensor)
* [circuitpython_motor_control](#circuitpython_motor_control)
* [The Hanger onshape](#The_Hanger_onshape)
* [ Multi-Part Design](#Multi-Part_Design).
*[Single_part](#Single_Part).
*[Plate](#Plate_part).
*[Mic_Holder](#Mic_Holder).
*[Rotary Encoder & LCD](#Rotary_Encoder).
---


## CircuitPython_Servo

### Description & Code Snippets
The goal of the assignment was to get a servo to move 180 in two diffrent directions with a button. I accomplished the goal by working on the button part first so I could get it to work then I did the servo part then added it all togather.

```python

"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_motor import servo


# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

btn1 = DigitalInOut(board.D5)
btn1.direction = Direction.INPUT
btn1.pull = Pull.DOWN

prev_state = btn1.value

btn2 = DigitalInOut(board.D2)
btn2.direction = Direction.INPUT
btn2.pull = Pull.DOWN

prev_state = btn2.value
# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    if btn1.value:
        print("BTN1  is down")  
        for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
            my_servo.angle = angle
      
    if btn2.value:
        print("BTN2  is down") 
        for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
            my_servo.angle = angle
    
    time.sleep(0.35) 
  +-
```


### Evidence
https://github.com/Jtoney40/engr3/blob/main/media/ezgif.com-gif-maker.gif?raw=true


### Wiring
![servo_wiring ](https://github.com/Jtoney40/engr3/assets/143732462/61ea9228-1ee2-4f96-9e82-f2762854cec5)



### Reflection
So what I made it do was the button would tell the servo to move in a direction and the other would do the oppiste.


## circuitpython_neopixle_with_distancesensor

### Description & Code Snippets
The work you had to do was make a neopixle work with a distancesensor so it would change. Make sure that you try to make all your indents right.


```python
import time
import board
import adafruit_hcsr04  
from rainbowio import colorwheel
import neopixel 
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

pixel_pin = board.NEOPIXEL
num_pixels = 1

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
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
    try:

        print((sonar.distance,))
        if (sonar.distance <= 5.0):
            blue = 0
            green = 0
            red = 255

        if (sonar.distance >= 5.0) and (sonar.distance < 20.0):
            green = 0
            blue = simpleio.map_range(sonar.distance,5.0,20.0,0.0,255.0)
            red = simpleio.map_range(sonar.distance,5.0,20.0,255.0,0.0)

        if (sonar.distance >= 20) and (sonar.distance <35):
            red = 0
            green = simpleio.map_range(sonar.distance,20.0,35.0,0.0,255.0)
            blue = simpleio.map_range(sonar.distance,20.0,35.0,255.0,0.0)
        if (sonar.distance >=35):
            red = 0
            blue = 0
            green = 255
        print("red =",red," green = ",green," blue = ",blue)    
        pixels[0] = (red,green,blue)
        pixels.show()
    
    except RuntimeError:
        print("Retrying!")

    time.sleep(0.1)
```

### Evidence

![ezgif com-video-to-gif (2)](https://github.com/Jtoney40/engr3/assets/143732462/64b36e47-595c-4031-9092-c2933ba70bb2)

### Wiring
![image](https://github.com/Jtoney40/engr3/assets/143732462/08d1da58-7f3e-42d6-9870-f8c24e359d14)

### Reflection
Parts that were hard was finding out how to code the color. The things that helped was the link the teacher gave us which is here. https://docs.google.com/spreadsheets/d/e/2PACX-1vRzoIejkQqugrDoWHBw14qTI0HifXba92WiyQ24whEnzWcCUaCDYu6ifMQKK5O5Ilkxrd7UKIxPLBCW/pubhtml. Make sure that your if statements make sense and work with what you want it to do. The distentsensor would change what color the neopixle is and the colser or farther it is the color would change.

## circuitpython_motor_contro

### Description & Code Snippets
I had to control a motor with a turner.

```python
import board
import analogio
from digitalio import DigitalInOut
import time 
import pwmio 
turner = analogio.AnalogIn(board.A1)
motor = pwmio.PWMOut(board.D9)

while True:
    print(turner.value) #show value 
    time.sleep(0.25)
    motor.duty_cycle = turner.value 
```

### evidences
https://github.com/Jtoney40/engr3/blob/main/media/ezgif.com-gif-maker%20(1).gif?raw=true 

### Wiring 
![Screenshot 2023-10-10 105200](https://github.com/Jtoney40/engr3/assets/143732462/4021a862-a48a-49f4-8bc4-4c12d31d34b1)

### reflection 
I learned that code for mottors can be very easy to do and you can make it very short. I also learned that if statements only work ifr there is a variable for it.

## The Hanger onshape

### Assignment Description
We had to make a hanger part using only drawings but it's a pretty simple part build.
Open this workspaceLinks to an external site., make a copy for yourself, and replace the word "copy" in the title with your name.  
The first two tabs contain instructions, and the last four contain the drawings you will use to create the part. 
Create a new part studio and rename it "swing arm."
Design the part using the four drawings as a guide. Notice that three dimensions are not defined directly. These dimensions will change values, so it is a good idea to define them as variables so that you can easily change them later.
Update the model based on the dimensions and materials listed in the instructions step 2 tab of the your Swing Arm -- Just Drawings document.
### Evidence
![image](https://github.com/Jtoney40/engr3/assets/143732462/6f4b9826-74c5-4444-8d5f-6cf4148ed00a)

![image](https://github.com/Jtoney40/engr3/assets/143732462/e5415ee9-a57e-4860-a8f3-4d0d5b1b54c5)





### Part Link 

https://cvilleschools.onshape.com/documents/8d6cb4f1f23619488b541efa/w/61bd722aa3dfbb6791e754d1/e/c8c72d273cdbf485a49033ca 

### Reflection
The parts that went wrong was I made it the wrong width so the cut didn't work so make sure you read the drawing right. I made a hanger part using only drawings and it was hard. 


## The swing arm 

### Assignment Description
We had to make a swing arm using only drawings which is harder to do than the hanger part. The part is also more complex to do.

### Evidence
![image](https://github.com/Jtoney40/engr3/assets/143732462/8ab8ae0d-c4e2-48db-a8db-44d760687b54)

![image](https://github.com/Jtoney40/engr3/assets/143732462/677100d7-badb-40f5-90c7-f6e7dc8dc8a0)

![image](https://github.com/Jtoney40/engr3/assets/143732462/268ee9ee-c38b-4436-83dd-664bf44efac8)

![image](https://github.com/Jtoney40/engr3/assets/143732462/5dbe58b4-2042-4be6-96f1-7ecdd7d2e0da)





### Part Link 

https://cvilleschools.onshape.com/documents/8d6cb4f1f23619488b541efa/w/61bd722aa3dfbb6791e754d1/e/c8c72d273cdbf485a49033ca 

### Reflection
The parts that went wrong was I made it the wrong width so the cut didn't work so make sure you read the drawing right. The work was very hard to do when I haven't done it for a while. Make sure that you make all of your lines defined.
****


## Multi-Part Design

### Assignment Description
I had to make a multi parts using drawings. There are mutiple parts to this asignment that you have to build.

### Evidence

![multipart](https://github.com/Jtoney40/engr3/assets/143732462/ff45efed-374e-467b-b762-938a84b5cb4b)
![multpart](https://github.com/Jtoney40/engr3/assets/143732462/bf424360-da5c-439c-8166-7235c7d15cbc)
![parts mulit](https://github.com/Jtoney40/engr3/assets/143732462/c443c3f2-4b9f-47d6-8f82-9db88bee1d57)





### Part Link 

https://cvilleschools.onshape.com/documents/8d6cb4f1f23619488b541efa/w/61bd722aa3dfbb6791e754d1/e/c8c72d273cdbf485a49033ca 

### Reflection
The parts that went wrong was I made it the wrong width so the cut didn't work so make sure you read the drawing right. The work was very hard to do when I haven't done it for a while. Make sure that you make all of your lines defined.



## Single Part

### Assignment Description
I had to make a single part which is easier than a muti-part.


### Evidence
![image](https://github.com/Jtoney40/engr3/assets/143732462/b7278dce-5660-44c1-a5e3-9c87d14b65ae)
![image](https://github.com/Jtoney40/engr3/assets/143732462/85d10841-a31d-4e13-8e75-378ee9f5781c)
![image](https://github.com/Jtoney40/engr3/assets/143732462/edbc4fe7-cc75-41e6-92f7-096fc9d8bd3e)


### Part Link 
https://cvilleschools.onshape.com/documents/578652328b3f23eaa1d991cf/w/9f6af31d704990f048e88151/e/f79ee10d4dde4b1147e4c7f8?renderMode=0&uiState=6543c13ae2bd97659ed49d7b

### Reflection
The part was overall very easy to do and you can do one half then just mirror it all.

****

## Plate

### Assignment Description
I had to make a part that was very simple and only had one part.


### Evidence
![image](https://github.com/Jtoney40/engr3/assets/143732462/547c9dca-217a-4fb1-adae-1e6f064b2099)
![image](https://github.com/Jtoney40/engr3/assets/143732462/1e84ec7e-dd5a-4517-947f-58956affd239)


### Reflection
The part was overall very easy to do and there was no problems at all. The part that was little tricky was reading the drawings that they gave us. Other than that it was very easy to do.


## Mic_Holder

### Assignment Description
The part had to be made using only using a blue print. the part was very simple to do and was very easy for having a lot of parts. This part was very easy to do all of it.

### Evidence
![image](https://github.com/Jtoney40/engr3/assets/143732462/52e23803-f26a-4b1d-ae24-3941b8c4a166)
![image](https://github.com/Jtoney40/engr3/assets/143732462/cf4909fd-60b2-4015-811b-f264dfcc8c21)
![image](https://github.com/Jtoney40/engr3/assets/143732462/91b0853a-0d9d-4ba1-9508-8a0534cdc018)

### Reflection
Every thing I did was very easy to do. The only hard part was making sure that I did the right material. 






## Rotary Encoder & LCD


### Description & Code Snippets
import rotaryio #takes code from files.
import board #takes code from files.
import neopixel #takes code from files.
import digitalio #takes code from files.
from lcd.lcd import LCD #tells you what file it takes the code from.
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface #tells you what file it takes the code from.

enc = rotaryio.IncrementalEncoder(board.D4, board.D3, divisor = 2) #tells you what pins it use and where to

lcd = LCD(I2CPCF8574Interface(board.I2C(), 0x27), num_rows = 2, num_cols = 16)

led = neopixel.NeoPixel(board.NEOPIXEL, 1)# allows for you to use the led/neopixel
led.brightness = 0.3
led[0] = (255, 0, 0)

button = digitalio.DigitalInOut(board.D2)# the code for the button 
button.direction = digitalio.Direction.INPUT# says that you can use the button as a input
button.pull = digitalio.Pull.UP
button_state = None  

menu_index = 0


while True:
    menu_index = enc.position
    menu = ["stop", "caution", "go"]# the states that the buttion can be in.
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
    if button.value and button_state == "pressed":# the state the button is in.
        print("Button is pressed")
        button_state = None
    if menu_index_lcd == 0:
        led[0] = (255, 0, 0)
    if menu_index_lcd == 1:
        led[0] = (255, 255,0)
    if menu_index_lcd == 2:
        led[0] = (0, 255, 0) # makes the led color.
    ```



### Evidence
![ezgif com-cut](https://github.com/Jtoney40/engr3/assets/143732462/831b6171-2d30-473a-97ba-f26f110c41eb)

### Wiring 
![image](https://github.com/Jtoney40/engr3/assets/143732462/5d1d6bba-cdf5-4377-b1e9-29f7a6068e17)

### Reflection 

