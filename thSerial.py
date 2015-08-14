import serial
import sys
import time
import threading
import queue
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)


ser = serial.Serial("/dev/ttyAMA0", baudrate = 9600, timeout = 2)

#this object will contain data received from serial input
data_rcv=queue.Queue()
