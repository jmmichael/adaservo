#!/usr/bin/python


import time
import pygame
import sys

from picamera import PiCamera
from time import sleep
from pygame.locals import *

camera = PiCamera()
camera.vflip = False
camera.hflip = False

camera.start_preview()
camera.preview.alpha = 200 # 1 is completely transparent
sleep (10)
camera.stop_preview()

pygame.init()
pygame.display.set_mode((640, 480))

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if  event.key == K_c:
                camera.capture('test.jpg')
            elif event.key == K_v:
                camera.start_recording('video.h264')
                sleep(15)
                camera.stop_recording()            
            elif event.key == K_s:
                camera.stop_recording()    
            elif event.key == K_p:
                camera.start_preview()
                camera.preview.alpha = 200 # 1 is completely transparent


        if event.type == QUIT:
             running = False
             print ("bye")

