# UR Mini Project: Speech to Text for Robot Control
이 프로젝트는 음성 명령을 통해 UR 로봇을 제어하는 프로그램을 구현합니다. 사용자가 특정 방향에 대한 음성 명령을 내리면, 로봇은 그에 따라 움직입니다.
![image](https://github.com/jiloKIm/-.-GitHub-README-.-UR-Mini-Project-Speech-to-Text-for-Robot-Control/assets/96615422/a1d91126-c755-4dc0-8a16-5f169a4037ea)
![image](https://github.com/jiloKIm/-.-GitHub-README-.-UR-Mini-Project-Speech-to-Text-for-Robot-Control/assets/96615422/c56844dc-a5ec-4cb8-a99c-5fbb7b71607c)

---



이 프로젝트는 음성 명령을 통해 UR 로봇을 제어하는 프로그램을 구현합니다. 사용자가 특정 방향에 대한 음성 명령을 내리면, 로봇은 그에 따라 움직입니다.

## 사용 모듈 소개

음성 인식 기능을 구현하기 위해 필요한 주요 모듈은 다음과 같습니다:

- **speechrecognition**: 음성 데이터를 텍스트로 변환합니다. PyAudio에 의존하며, `pip install SpeechRecognition`으로 설치할 수 있습니다.

    ```python
    import speech_recognition as sr
    ```

- **math 모듈**: UR 로봇 프로그래밍에서 라디안 좌표체계를 사용하기 위해 필요합니다.

- **urx 모듈**: UR 로봇과의 통신을 위해 필요합니다. `pip install urx`로 설치할 수 있습니다.

    ```python
    from urx import Robot
    ```

## 사전 작업

로봇을 연결하고 초기 설정을 진행하는 방법은 다음과 같습니다:

```python
ip = 'your robot ip'
rob = Robot(ip)

# 초기 세팅
a = 0.5
v = 1
rob.set_tcp((0, 0, 0.1, 0, 0, 0))
rob.set_payload(2, (0, 0, 0.1))
time.sleep(0.2)
```

## STT(Speech to Text) 설정

음성 인식을 위한 코드는 다음과 같습니다:

```python
ar = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak now!")
    audio = ar.listen(source)

try:
    text = ar.recognize_google(audio, language='ko-KR')
    print("You said: {}".format(text))
except sr.UnknownValueError:
    print("Recognition failed")
except sr.RequestError:
    print("Request failed, network disconnected or API key error")
```

## 로봇 제어

입력받은 텍스트에 따라 로봇을 움직이는 코드 예시입니다:

```python
try:
    if text == "right":
        rob.movej((0, r(-100), 0, r(-90), 0, 0), a, v)
        time.sleep(2)
    # 추가 명령...
finally:
    rob.movej((0, r(-80), 0, r(-90), 0, 0), a, v)
    rob.close()
```

## 구현 결과

구현 결과를 보여주는 비디오: [Demo Video](https://youtu.be/lsvaCj_xDxI)

