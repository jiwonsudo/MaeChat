from gtts import gTTS
import playsound

text = 'ㅋㅋ루삥뽕'

audioData = gTTS(text = text, lang='ko')  # 한국어 입력
audioData.save('ttsTest.mp3')  # audioData를 output.wav로 저장
playsound.playsound('ttsTest.mp3')