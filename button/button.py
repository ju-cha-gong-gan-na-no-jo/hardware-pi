from gpiozero import Button               # Button 믈래스  불러오기
from signal import pause                  #프로세스 대기함수 불러오기
import paho.mqtt.client as mqtt
import json
import time
import pygame
pygame.mixer.init()


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)

def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))

def on_publish(client, userdata, mid):
    time.sleep(0.5)
    print("In on_pub callback mid= ", mid)


def say_hello():                #콜백함수
    client.publish('common', json.dumps({"success": "ok", "test": "한글만보내기"}), 1)
    pygame.mixer.music.load("/home/pi/data/bell.mp3")
    pygame.mixer.music.play()
    time.sleep(0.2)

    print("관리자 호출!!!")

def say_goodbye():              #콜백함수
    time.sleep(0.3)
    print("chi-yong ah!!!!")
    

button = Button(18)              #gpio18번 핀과 연결된 버튼을 통해 button객체 생성

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

client.connect('15.165.153.54', 1883)
client.loop_start()



button.when_pressed = say_hello    #버튼이 눌렸을 때 실행될 콜백함수 지정
button.when_released = say_goodbye #버튼이 눌렸다가 놓아졌을 때 실행될 콜백함수 지정

pause()                            # 프로세스 대기
