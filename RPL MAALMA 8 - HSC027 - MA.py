from machine import Pin, ADC
import time
import network

ldr_pin = 34
ldr = ADC(Pin(ldr_pin))
ldr.atten(ADC.ATTN_11DB)

lamp_pin = 2
lamp = Pin(lamp_pin, Pin.OUT)


while True:
    ldr_value = ldr.read()
    print("Pencahayaan:", ldr_value)
    
    if ldr_value < 2000:
        lamp.value(1)
    else:
        lamp.value(0)
    
    time.sleep(1)