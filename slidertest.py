from Tkinter import *
import RPi.GPIO as GPIO
import time

from Adafruit_PWM_Servo_Driver import PWM

# Initialise the PWM device using the default address
pwm = PWM(0x40)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

class App:
	
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		Label(frame, text='Horizontal').grid(row=0, column=0)
		Label(frame, text='Vertical').grid(row=1, column=0)
        
		scaleHorizontal = Scale(frame, from_=175, to=675,
		orient=HORIZONTAL, command=self.hpos)
		scaleHorizontal.grid(row=0, column=1)

  #      scaleVertical = Scale(frame, from_=175, to=675,
 #             orient=VERTICAL, command=self.vpos)
#        scaleVertical.grid(row=1, column=1)

	def hpos(self, lr):
		pwm.setPWM(1,30,(lr))

#    def vpos(self, ud):
 #       pwm.setPWM(0,30,(ud))

root = Tk()
root.wm_title('Camera Position')
app = App(root)
root.geometry("400x300+0+0")
root.mainloop()
