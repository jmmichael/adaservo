'''
http://apprize.info/hardware/raspberry/11.html

The first line after the import creates a new instance of PWM using the I2C address specified as it arguments, in this case, 0 x 40.
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
On the Eurgle winch 500/180 gave 7.5 rotations, 500/360 gave about 2.25
500/500 about .5

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
              orient=HORIZONTAL, command=self.updateh)
        scale.grid(row=0)
        
        scale = Scale(frame, from_=0, to=180,
              orient=VERTICAL, command=self.updatev)
        scale.grid(column=0)
    def updateh(self, angle):
        pulse_len = int(float(angle) * 500.0 / 180.0)# + 110
        pwm.setPWM(0, 0, pulse_len)
        #pwm.setPWM(1, 0, pulse_len)
    def updatev(self, angle):
        pulse_len = int(float(angle) * 500.0 / 180.0)# + 110
        pwm.setPWM(2, 0, pulse_len) #change 0 to point wher it becomes active
        #pwm.setPWM(1, 0, pulse_len)

root = Tk()
root.wm_title('Servo Control')
app = App(root)
root.geometry("200x150+100+100")
root.mainloop()
