from gpiozero import Button
import sensor_logger


class SensorWindSpeed(sensor_logger.SensorLogger):
    def __init__(self):
        super().__init__()
        self.button = Button("GPIO5")

    def schema(self):
        return f"""
CREATE TABLE IF NOT EXISTS wind_speed (
	timestamp NUMBER PRIMARY KEY NOT NULL
);"""

    def run(self):
        while True:
            print("waiting")
            self.button.wait_for_press()
            print("pressed!")
            self.button.wait_for_release()
            print("released!")
            self.insert(sql="INSERT INTO wind_speed VALUES (?)",
                        parameters=[self.now()])





"""
from gpiozero import Button

wind_speed_sensor = Button("GPIO5")
wind_count = 0

def spin():
    global wind_count
    wind_count = wind_count + 1
    print("spin" + str(wind_count))

print("connecting button")
wind_speed_sensor.when_pressed = spin
print("disconnecting button")
"""

"""
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
pin = 26
def button_callback(channel):
    print("Button was pushed!")

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

GPIO.add_event_detect(pin,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge
#GPIO.add_event_detect(pin,GPIO.FALLING,callback=button_callback) # Setup event on pin 10 rising edge

message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up
"""

from gpiozero import Button

button = Button("GPIO5")
count = 0
for _ in range(100):
  button.wait_for_press()
  button.wait_for_release()
  print(count)
  count += 1
print("The button was pressed!")
