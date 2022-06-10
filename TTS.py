from gtts import gTTS
from IPython.display import Audio, display

text = '안녕하세요안녕하세요'

tts = gTTS(text = text, lang='ko') #lang='ko' -> 한국어 입력
tts.save('output.wav') #kor_wav를 wav파일로 저장
display(Audio('output.wav', autoplay = True))