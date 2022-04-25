import RPi.GPIO as GPIO
import time
import subprocess        #이벤트 드리븐? 여기서의 행동으로 다른 파일을 실행시킴

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
    
    if distance <= 30:             #초음파 센서 위치 확인
      subprocess.call("raspistill -t 1500 -o picam.jpg",shell=True)  # 1500 = 1.5초 후에 촬영
      print("front object detected!")
      subprocess.call("python3 ../detect_car/main.py picam.jpg", shell=True)     # picam.jpg 물어서 main.py를 실행시킴
    print("거리 : ", distance, "cm")

except KeyboardInterrupt :
  GPIO.cleanup()
