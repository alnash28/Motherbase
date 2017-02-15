import RPi.GPIO as GPIO
import time
import wit 
import json
import subprocess 
GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False) 
GPIO.setup(11,GPIO.OUT)

access_token = 'Reva'
wit.init()

while(True):
    resp = wit.voice_query_auto(access_token)
    if not access_token:
      continue 
      
    else
      subprocess.call(['home/pi/motherbase/lightup','on'])
      
wit.close()

