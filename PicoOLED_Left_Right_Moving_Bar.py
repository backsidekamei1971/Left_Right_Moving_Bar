from machine import Pin
import ssd1306
import time
i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
button  = Pin(15, Pin.IN, pull=Pin.PULL_UP)
button1 = Pin(14, Pin.IN, pull=Pin.PULL_UP)
j=0
while True:
    oled.fill(0)          
    state = button.value()   
    if state == 0:
        j=j+8
    if j>=48:
        j=48
    state1 = button1.value()   
    if state1 == 0:
        j=j-8
    if j<=-48:
        j=-48   
    oled.fill_rect(58+j,43,8,8,1)
    oled.fill_rect(50+j,50,24,8,1)    
    oled.show()  
    time.sleep_ms(16)
