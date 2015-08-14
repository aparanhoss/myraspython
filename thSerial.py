import serial
import sys
import time
import threading
import Queue
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)