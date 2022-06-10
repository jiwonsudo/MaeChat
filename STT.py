import speech_recognition as sr

Recognizer = sr.Recognizer()  # 인스턴스 생성
mic = sr.Microphone()

with mic as source: # 음성 인식
    inputAudio = Recognizer.listen(source, phrase_time_limit = 3)
try:
    inputText = Recognizer.recognize_google(inputAudio, language="ko") # inputText에 음성을 string으로 전환한 정보 저장
except:
    print("이해하지 못했어요. 다시 말씀해 주세요.")

print(inputText)