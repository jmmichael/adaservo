'''
http://apprize.info/hardware/raspberry/11.html

The first line after the import creates a new instance of PWM using the I2C address specified as its argument—in this case, 0 × 40.
The next line sets the PWM frequency to 50 Hz, which will provide an update pulse every 20 milliseconds.
The line that sets the PWM for a particular channel is:
pwm.setPWM(0, 0, pulse_len)
The first argument is the PWM channel whose duty cycle is to be changed.
Each cycle of PWM is divided into 4,096 ticks, and the second argument is the tick at which the pulse should start.
This will always be 0.
The third argument is the tick at which the pulse should end.
The constants of 500.0 and 110 in the following line were tweaked with a little trial and error to provide a standard
servo with as close to 180 degrees of movement as possible:
pulse_len = int(float(angle) * 500.0 / 180.0) + 110
'''
from Tkinter import *
from Adafruit_PWM_Servo_Driver import PWM
import time

pwm = PWM(0x40)
pwm.setPWMFreq(50)

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        scale = Scale(frame, from_=0, to=180,
              orient=HORIZONTAL, command=self.update)
        scale.grid(row=0)
    def update(self, angle):
        pulse_len = int(float(angle) * 500.0 / 180.0) + 110
        pwm.setPWM(0, 0, pulse_len)
        pwm.setPWM(1, 0, pulse_len)

root = Tk()
root.wm_title('Servo Control')
app = App(root)
root.geometry("200x50+0+0")
root.mainloop()-
