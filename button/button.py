from gpiozero import Button               # Button 클래스  불러오기
from signal import pause                  #프로세스 대기함수 불러오기
import paho.mqtt.client as mqtt           #mqtt 사용 라이브러리
import json
import time
import pygame                              #음원 재생
pygame.mixer.init()        #pygame 초기 설정 완료 무조건 해야함


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
    client.publish('common', json.dumps({ "success": "ok", "test": "관리실호출!!!"}), 1)        # 한글 깨짐 문제 발생 -> 받을때 json.형태로 받는 코드가 있음
    pygame.mixer.music.load("/home/pi/data/bell.mp3")      #pygame 재생할 음원 로드
    pygame.mixer.music.play()                   # 로드 된 파일 재생
    time.sleep(0.2)                             # 여러번 버튼을 눌렀을때 중복 방지로 타임 슬립 줌.

    print("관리자 호출!!!")

def say_goodbye():              #콜백함수
    time.sleep(0.3)
    print("chi-yong ah!!!!")
    

button = Button(18)              #gpio18번 핀과 연결된 버튼을 통해 button객체 생성

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish                    # 계속 정보를 구독자에게 계속 보냄

client.connect('15.165.153.54', 1883)              # 메인 ec2 주소 포트는 1883 메인  ec2는 공인 아이피기 때문에 문제 없이 정보를 날림
client.loop_start()



button.when_pressed = say_hello    #버튼이 눌렸을 때 실행될 콜백함수 지정
#button.when_released = say_goodbye #버튼이 눌렸다가 놓아졌을 때 실행될 콜백함수 지정

pause()                            # 프로세스 대기
