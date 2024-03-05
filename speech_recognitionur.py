from urx import Robot
import time
from math import radians as r
import speech_recognition as sr

# 로봇 연결
ip = ''
rob = Robot(ip)

# 초기 셋팅
a = 0.5
v = 1
rob.set_tcp((0, 0, 0.1, 0, 0, 0))
rob.set_payload(2, (0, 0, 0.1))
time.sleep(0.2)

ar = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak!")
    audio = ar.listen(source)  
try:
    text = ar.recognize_google(audio, language='en-US')
    print("You said: {}".format(text))
except sr.UnknownValueError:
    print("Recognition failed")  
except sr.RequestError:
    print("Request failed, network disconnected or API key error")

try:
    if text == "right":
        rob.movej((0, r(-100), 0, r(-90), 0, 0), a, v)
        time.sleep(2)
    elif text == "forward":
        rob.movej((r(55), r(-30), r(-60), r(-68), 0, 0), a, v)
        time.sleep(2)
    elif text == "left":
        rob.movej((0, r(-60), 0, r(-90), 0, 0), a, v)
        time.sleep(2)
    elif text == "backward":
        rob.movej((r(-80), 0, 0, 0, 0, 0), a, v)
        time.sleep(2)
    elif text == "up":
        rob.movej((r(4.4), r(-86), r(-13), r(2.6), r(98.5), r(100)), a, v)
        time.sleep(2)
    elif text == "down":
        rob.movej((r(7), r(-91), r(-12), r(1.5), r(-50), r(100)), a, v)
        time.sleep(2)
finally:
    rob.movej((0, r(-80), 0, r(-90), 0, 0), a, v)
    rob.close()
