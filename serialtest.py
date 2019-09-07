import serial
from time import sleep
import webbrowser
with serial.Serial('/dev/ttyACM0', 57600, timeout=1) as ser:
    while True:
        line = str(ser.readline())
        print(line)
        if  "Theo" and "0" in line:
            print("Pin 0")
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=dQw4w9WgXcQ?autoplay=1")
            sleep(2)