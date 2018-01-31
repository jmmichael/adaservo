#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import pygame
import sys

from picamera import PiCamera
from time import sleep
from pygame.locals import *

camera = PiCamera()
camera.vflip = True
camera.hflip = True

camera.start_preview()
#camera.preview.alpha = 100 # 1 is completely transparent
sleep (5)
camera.stop_preview()

pygame.init()
pygame.display.set_mode((640, 480))

running = True

# Initialise the PWM device using the default address
pwm = PWM(0x40)

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096
v = 320
h = 320

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  pulseLength /= 4096                     # 12 bits of resolution
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
pwm.setPWM(0, 0, v)
pwm.setPWM(2, 0, h)

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                v = v + 5
                pwm.setPWM(2,30,v)
            elif event.key == K_UP:
                v = v - 5
                pwm.setPWM(2,30,v)
            elif event.key == K_RIGHT:
                h = h + 5
		pwm.setPWM(0,30,h)
            elif event.key == K_LEFT:
                h = h - 5
                pwm.setPWM(0,30,h)
            elif event.key == K_r:
                pwm.setPWM(0,30,320)
                pwm.setPWM(2,30,320)
            elif event.key == K_c:
                camera.capture('test.jpg')
            elif event.key == K_v:
                camera.start_recording('video.h264')
                sleep(5)
                camera.stop_recording()


        if event.type == QUIT:
             running = False
             pwm.setPWM(0,30,320)
             pwm.setPWM(2,30,320)
             print ("bye")

