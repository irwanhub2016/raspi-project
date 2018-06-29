from gpiozero import LightSensor, Buzzer
from time import sleep

ldr = LightSensor(4)  # alter if using a different pin

while True:
    print(ldr.value)
    if ldr.value >= 0.8:
	print("Terang") 
    elif ldr.value < 0.8:
	print("Gelap")

    sleep(1)
