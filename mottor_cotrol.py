
import board
import analogio
from digitalio import DigitalInOut
import time 
import pwmio 
turner = analogio.AnalogIn(board.A1)
motor = pwmio.PWMOut(board.D9)

while True:
    print(turner.value) #show value 
    #print("yuijk") #show value
    time.sleep(0.25)
    motor.duty_cycle = turner.value 
    


   


    