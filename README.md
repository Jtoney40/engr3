# CircuitPython
This repository will actually serve as an aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [circuitpython_neopixle_with_distancesensor](#circuitpython_neopixle_sensor)
* [circuitpython_motor_control](#circuitpython_motor_control)
* [The Hanger onshape](#The_Hanger_onshape)
* [ Multi-Part Design](#Multi-Part_Design)
* [Single_part](#Single_Part)
* [Plate](#Plate_part)
* [Mic_Holder](#Mic_Holder)
* [Rotary Encoder & LCD](#Rotary_Encoder)
* [Stepper_Motors_and_Limit_Switches](#Stepper_Motors_and_Limit_Switches)
* [Robot Gripper Design](#Robot_Gripper_Design)
* [IR Sensors](#IR_Sensors)
* [Photointerrupters](#Photointerrupters)
* [Many parts ](#Many_parts) 
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

### Part Link
https://cvilleschools.onshape.com/documents/dcc44cd528f0be2d80269aa4/w/623021fde205304d14279cf2/e/4ccd2c9385fb16f246f0adb3?renderMode=0&uiState=66140e85bed4e1394c2aa3e2 

### Reflection
Every thing I did was very easy to do. The only hard part was making sure that I did the right material. 






## Rotary Encoder & LCD


### Description & Code Snippets
You had to use a joy stick to change the words on the lcd screen and make it say go, cotion, and stop and make the neopixle change colors when those words are printed.


```python
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
The assignment was really easy to do and over all no problems. But make sure your wiring is right so you don't break anything. The menu was hard because you have to make sure that it fits on your screen. Plus knowing what numbers make the color what you need it to be.

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


## Stepper_Motors_&_Limit_Switches


### Description & Code Snippets
I had to make the motor move backwards and forwards with a press of a button.

```python
import asyncio
import board
import keypad
import time
import digitalio
from adafruit_motor import stepper


DELAY = 0.01   # Sets the delay time for in-between each step of the stepper motor.
STEPS = 100    # Sets the number of steps. 100 is half a full rotation for the motor we're using. 

# Set up the digital pins used for the four wires of the stepper motor. 
coils = (
    digitalio.DigitalInOut(board.D9),   # A1
    digitalio.DigitalInOut(board.D10),  # A2
    digitalio.DigitalInOut(board.D11),  # B1
    digitalio.DigitalInOut(board.D12),  # B2
)

# Sets each of the digital pins as an output.
for coil in coils:
    coil.direction = digitalio.Direction.OUTPUT

# Creates an instance of the stepper motor so you can send commands to it (using the Adafruit Motor library). 
motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)

motor.onestep()

motor.onestep(direction=stepper.BACKWARD) # tells the motor to go backwards

style=stepper.DOUBLE #how much it does it.

for step in range(STEPS): # tells the motor how to work
    motor.onestep(style=stepper.DOUBLE)
    time.sleep(DELAY)


for step in range(STEPS): 
    motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    time.sleep(DELAY)

async def catch_pin_transitions(pin):
    # Print a message when pin goes low and when it goes high.
    with keypad.Keys((pin,), value_when_pressed=False) as keys:
        while True:
            event = keys.events.get()
            if event:
                if event.pressed:
                    print("Limit Switch was pressed.")
                    motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)

                elif event.released:
                    print("Limit Switch was released.")
                    motor.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
                await asyncio.sleep(0)

async def run_motor():
    while(True):
        motor.onestep(style= stepper.DOUBLE)
        time.sleep(DELAY) 
        motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(DELAY)

        await asyncio.sleep(0)

async def main():
    while(True):
        interrupt_task = asyncio.create_task(catch_pin_transitions(board.D2))
        asyncio.create_task(run_motor())
        motor.onestep(style-stepper.DOUBLE)
        time.sleep(DELAY)
        motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        time.sleep(DELAY)
        await asyncio.gather(interrupt_task, 
                            catch_pin_transitions(board.D2))
        

asyncio.run(main())
 
```

### Evidence
![WIN_20240311_10_55_50_Pro-ezgif com-video-to-gif-converter](https://github.com/Jtoney40/engr3/assets/143732462/19c34b4d-aa89-45e4-ad47-804e5befbf3d)



### Wiring
![image](https://github.com/Jtoney40/engr3/assets/143732462/7b9b2fd4-1e4f-4525-b119-53ddabb0b12f)

### Reflection
The Assigment was very hard I didn't know how to do a lot of it so it was a lot of learning. Also the code was hard to make sense of the code. I got help from the teacher which helped. Make sure you spell every thing right and the same way.


## Robot_Gripper_Design

### Assignment Description
1. I had to make a robot arm that can pick up a deck of cards.

2. It has to fully close.

3. parts must be laser cut or 3D printed.

4. must be fully essembly in onshape.
### Evidence
![image](https://github.com/Jtoney40/engr3/assets/143732462/28455c9e-2f02-49a3-bedc-229bbd5ebe80)
![image](https://github.com/Jtoney40/engr3/assets/143732462/94b893ec-3483-43e3-b3fe-0a4c0097b99c)

### PART LINK 
https://cvilleschools.onshape.com/documents/9518bf8fe9f621e00694a314/w/c32f8507d13e886b0da60a8d/e/ee21a647c8ad5231ddf940a7?renderMode=0&uiState=66140d2cbed4e1394c2a9b89 

### Reflection
The first time i made it it didn't work because I made it too big. Then I did it for a seconde time and it work because I reflected on how I messed up the first time. The first time it was too thick.

## IR_Sensors

### Description & Code Snippets
 I had to light up a led with a ir sensor and have it cut off when you get to close.

```python
import board
import neopixel
import digitalio
# Allows for the code to work with these.

ir_sensor = digitalio.DigitalInOut(board.D2) #tells you what the pin is for the ir sensor.
ir_sensor.direction = digitalio.Direction.INPUT# gives it a input
ir_sensor.pull = digitalio.Pull.UP

led = neopixel.NeoPixel(board.NEOPIXEL, 1)#the code for the neopixle
led.brightness = 0.3
led[0] = (255,0,0)

while True:
    if ir_sensor.value == 1: # what runs the ir sensor
        print("Sensor is LOW")
        led[0] = (255, 0, 0)

    if ir_sensor.value == 0:
        print("Sensor is HIGH")
        led[0] = (0, 255, 0)
```

### Evidence
 ![WIN_20240312_12_24_38_Pro-ezgif com-video-to-gif-converter (1)](https://github.com/Jtoney40/engr3/assets/143732462/cea4c8a2-83ce-4658-862f-70d8a654269b)



### Wiring
![image](https://github.com/Jtoney40/engr3/assets/143732462/edcc74b1-8974-4314-a692-5e8af4d9bb48)

### Reflection
 The hard part was having the right vaules and the right pins. Also finding how to code it all and having to wire it with out breaking.



## Photointerrupters

### Description & Code Snippets
I had to code a photointerrupter to send a messege to a lcd screen saying how many times it got interrupted.

```python
import time 
import digitalio
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

photointerrupter = digitalio.DigitalInOut(board.D2)
photointerrupter.direction = digitalio.Direction.INPUT
photointerrupter.pull = digitalio.Pull.UP
photointerrupter_state = None

interrupt_counter = 0
lcd = LCD(I2CPCF8574Interface(board.I2C(), 0x3f), num_rows=2, num_cols=16)
lcd.set_cursor_pos(0,0)
lcd.print("Interrupt count:") 
now = time.monotonic()

while True: 
    print(interrupt_counter)
    #print(photointerrupter_state)
    #print(photointerrupter.value)
    if not photointerrupter.value and photointerrupter_state is None:
        photointerrupter_state = "Interrupted"
       
    if (photointerrupter.value == True) and (photointerrupter_state == "Interrupted"):
        photointerrupter_state = None
        print("Interrupted")
        interrupt_counter = interrupt_counter +1
    if (now + 0.003) < time.monotonic(): 
        now = time.monotonic()
        lcd.set_cursor_pos(1,0)
        lcd.print(str(interrupt_counter))


  +-
```


### Evidence
![WIN_20240325_11_18_18_Pro-ezgif com-video-to-gif-converter (1)](https://github.com/Jtoney40/engr3/assets/143732462/6fecfcb0-394c-4c73-b7d2-8c21778c7bfe)


### Wiring
![image](https://github.com/Jtoney40/engr3/assets/143732462/983731ca-b158-4733-b8db-aed1aa077f47)



### Reflection
The hard part of this was making sure what my lcd pin was and having to use the code to check it.


## Many_parts 

### Description 
I had to make a tool and put it all togather and make sure that it works.

### Evidence
![image](https://github.com/Jtoney40/engr3/assets/143732462/8487b2a4-2978-47cc-9a97-567810dfc31c)
![image](https://github.com/Jtoney40/engr3/assets/143732462/1805a133-2f26-40b8-98a2-ab20949b3110)

### Part Link
https://cvilleschools.onshape.com/documents/c95bdc9704b46a0ba9cfb4a9/w/65abfacdff51609a2f476c2f/e/84ef229f518be073f67198bb?renderMode=0&uiState=66140e0fd90cf033e0d20982 

### Reflection
The only part I found hard was making the part equal to each other because they made the parts look weird when you try to do so.
 


