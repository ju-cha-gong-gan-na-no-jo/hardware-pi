import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)


trig = 23
echo = 24

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

try :
  while True:
    GPIO.output(trig, False)
    time.sleep(0.5)

    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    while GPIO.input(echo) == 0 :
      pulse_start = time.time()

    while GPIO.input(echo) == 1 :
      pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17000
    distance = round(distance, 2)
    
    if distance <= 28:
      subprocess.call("raspistill -t 1500 -o picam.jpg",shell=True)
      print("front object detected!")
      subprocess.call("python ../detect_car/main.py picam.jpg", shell=True)
    print("거리 : ", distance, "cm")

except KeyboardInterrupt :
  GPIO.cleanup()
