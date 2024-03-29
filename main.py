from time import sleep
from Adafruit_CharLCD import Adafruit_CharLCD

# instantiate lcd and specify pins
lcd = Adafruit_CharLCD(rs=4, en=17,
                       d4=21, d5=22, d6=10, d7=9,
                       cols=16, lines=2)
lcd.clear()
# display text on LCD display \n = new line
lcd.message('Adafruit CharLCD\n  Raspberry Pi')
sleep(3)
# scroll text off display
for x in range(0, 16):
    lcd.move_right()
    sleep(.1)
sleep(3)
# scroll text on display
for x in range(0, 16):
    lcd.move_left()
    sleep(.1)