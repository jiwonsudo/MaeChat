# MaeChat, An artificial intelligence conversational chatbot for Maecheon High School.
# Produced by Min-Joo Kim, Yeon-Kyung Baek, Do-Hoon Song, and Ji-Won Jeong (Team MaeChat).
# Produced with reference to https://madrabbit7.tistory.com/77 , '(자연어처리/챗봇) 텐서 플로(tensorflow)로 챗봇 만들기'.

# import for chatbot
import random
import json
import pickle
import os

import datetime as datetime

import requests as requests

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from keras.models import load_model
from util import *
import re
from konlpy.tag import Komoran
komoran = Komoran()

# import for STT (Speech-To-Text)
import speech_recognition as sr

# import for TTS (Text-To-Speech)
from gtts import gTTS
import playsound

# import for APIs
import json
import requests
import datetime

# import for Maps
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def speechToText():
    Recognizer = sr.Recognizer()  # 인스턴스 생성
    mic = sr.Microphone()

    print('음성 인식 시작')

    with mic as source:  # 음성 인식
        print('음성 인식 중..')
        inputAudio = Recognizer.listen(source, phrase_time_limit = 3)
    try:
        inputText = Recognizer.recognize_google(inputAudio, language="ko")  # inputText에 음성을 string으로 전환한 정보 저장
    except:
        inputText = ""

    print('음성 인식 끝')
    print('인식 결과:', inputText)
    return inputText


def textToSpeech(outputText : str):
    audioData = gTTS(text=outputText, lang='ko')  # 한국어 입력
    audioData.save('output.mp3')  # audioData를 output.wav로 저장
    playsound.playsound('output.mp3')

def getLunchMenu(dateToday : str):
    lunchMenuURL = "https://open.neis.go.kr/hub/mealServiceDietInfo"
    lunchParams = dict(
        Type='json',
        ATPT_OFCDC_SC_CODE='D10',
        SD_SCHUL_CODE='7240272',
        MMEAL_SC_CODE='2',
        MLSV_YMD=dateToday
    )
    try:
        res = requests.get(url=lunchMenuURL, params=lunchParams)
        resJSON = res.json()
        lunchMenu: str = resJSON['mealServiceDietInfo'][1]['row'][0]['DDISH_NM']
    except KeyError: # if dateToday is not the day with lunch:
        return 'noLunch'
    transTable = lunchMenu.maketrans({
        '(': ' ', # 왼쪽은 치환하고 싶은 문자, 오른쪽은 새로운 문자
        ')': ' ',
        '1': ' ',
        '2': ' ',
        '3': ' ',
        '4': ' ',
        '5': ' ',
        '6': ' ',
        '7': ' ',
        '8': ' ',
        '9': ' ',
        '0': ' ',
        '.': ' ',
    })
    lunchMenu = lunchMenu.replace('<br/>', '')
    lunchMenu = lunchMenu.translate(transTable)

    return lunchMenu

def showMap(outputTag : str):

    global path

    # 1층
    if outputTag == "1_Cafeteria":
        path = '../Maps/1_Cafeteria.png'
    if outputTag == "1_CookingClass":
        path = '../Maps/1_CookingClass.png'
    if outputTag == "1_AdminOffice":
        path = '../Maps/1_AdminOffice.png'
    if outputTag == "1_PrincipalOffice":
        path = '../Maps/1_PrincipalOffice.png'
    if outputTag == "1_ServiceRoom":
        path = '../Maps/1_ServiceRoom.pn'
    if outputTag == "1_GuardOffice":
        path = '../Maps/1_GuardOffice.png'
    if outputTag == "1_HealthRoom":
        path = '../Maps/1_HealthRoom.png'
    if outputTag == "1_SpecialClasses":
        path = '../Maps/1_SpecialClasses.png'

    # 2층
    if outputTag == "2_ComputerClasses":
        path = '../Maps/2_ComputerClasses.png'
    if outputTag == "2_SWClass":
        path = '../Maps/2_SWClass.png'
    if outputTag == "2_EduInfoOffice":
        path = '../Maps/2_EduInfoOffice.png'
    if outputTag == "2_StarStarClass":
        path = '../Maps/2_StarStarClass.png'
    if outputTag == "2_1GradeOffice":
        path = '../Maps/2_1GradeOffice.png'
    if outputTag == "2_1stOffice":
        path = '../Maps/2_1stOffice.png'
    if outputTag == "2_ElectronicsRoom":
        path = '../Maps/2_ElectronicsRoom.png'
    if outputTag == "2_BroadCastRoom":
        path = '../Maps/2_BroadCastRoom.png'
    if outputTag == "2_ConferenceRoom":
        path = '../Maps/2_ConferenceRoom.png'
    if outputTag == "2_YoutubeRoom":
        path = '../Maps/2_YoutubeRoom.png'
    if outputTag == "2_Darak":
        path = '../Maps/2_Darak.png'
    if outputTag == "2_Library":
        path = '../Maps/2_Library.png'
    if outputTag == "2_Theater":
        path = '../Maps/2_Theater.png'

    # 3층
    if outputTag == "3_2GradeOffice":
        path = '../Maps/3_2GradeOffice.png'
    if outputTag == "3_Hanmae":
        path = '../Maps/3_Hanmae.png'
    if outputTag == "3_DesignRoom2":
        path = '../Maps/3_DesignRoom2.png'
    if outputTag == "3_DreamNarae3":
        path = '../Maps/3_DreamNarae3.png'
    if outputTag == "3_CouncilRoom":
        path = '../Maps/3_CouncilRoom.png'
    if outputTag == "3_DebateRoom":
        path = '../Maps/3_DebateRoom.png'
    if outputTag == "3_EduFileRoom":
        path = '../Maps/3_EduFileRoom.png'
    if outputTag == "3_2ndOffice":
        path = '../Maps/3_2ndOffice.png'
    if outputTag == "3_MathStudyClass":
        path = '../Maps/3_MathStudyClass.png'
    if outputTag == "3_GroupStudyClass":
        path = '../Maps/3_GroupStudyClass.png'
    if outputTag == "3_Gym":
        path = '../Maps/3_Gym.png'

    # 4층
    if outputTag == "4_Bizo":
        path = '../Maps/4_Bizo.png'
    if outputTag == "4_3GradeOffice":
        path = '../Maps/4_3GradeOffice.png'
    if outputTag == "4_PhysicsClass":
        path = '../Maps/4_PhysicsClass.png'
    if outputTag == "4_EarthScienceClass":
        path = '../Maps/4_EarthScienceClass.png'
    if outputTag == "4_DreamNarae4":
        path = '../Maps/4_DreamNarae4.png'
    if outputTag == "4_PaintingClass2":
        path = '../Maps/4_PaintingClass2.png'
    if outputTag == "4_RelaxRoom":
        path = '../Maps/4_RelaxRoom.png'
    if outputTag == "4_Storage":
        path = '../Maps/4_Storage.png'
    if outputTag == "4_SocietyClass":
        path = '../Maps/4_SocietyClass.png'

    # 5층
    if outputTag == "5_MusicClass":
        path = '../Maps/5_MusicClass.png'
    if outputTag == "5_ArtClass":
        path = '../Maps/5_ArtClass.png'
    if outputTag == "5_WeClass":
        path = '../Maps/5_WeClass.png'
    if outputTag == "5_PaintingClass3":
        path = '../Maps/5_PaintingClass3.png'
    if outputTag == "5_DesignRoom3":
        path = '../Maps/5_DesignRoom3.png'
    if outputTag == "5_DesignRoom1":
        path = '../Maps/5_DesignRoom1.png'
    if outputTag == "5_ChemicsClass":
        path = '../Maps/5_ChemicsClass.png'
    if outputTag == "5_BiologyClass":
        path = '../Maps/5_BiologyClass.png'
    if outputTag == "5_DreamJiRak":
        path = '../Maps/5_DreamJiRak.png'
    if outputTag == "5_ArtOffice":
        path = '../Maps/5_ArtOffice.png'
    if outputTag == "5_SmallGroupClass":
        path = '../Maps/5_SmallGroupClass.png'
    if outputTag == "5_MiniGym":
        path = '../Maps/5_MiniGym.png'
    if outputTag == "5_EnglishClass2":
        path = '../Maps/5_EnglishClass2.png'
    if outputTag == "5_EnglishClass1":
        path = '../Maps/5_EnglishClass1.png'
    if outputTag == "5_EnglishBookCafe":
        path = '../Maps/5_EnglishBookCafe.png'
    if outputTag == "5_PaintingClass1":
        path = '../Maps/5_PaintingClass1.png'

    image_pil = Image.open(path)
    image = np.array(image_pil)
    plt.imshow(image)
    plt.show()


def cleanUpSentence(sentence):
    sentence = re.sub(r'[^\w\s]', '', sentence)  # 모든 구두점 제거
    morpheme = komoran.pos(sentence)  # 형태소 분석
    morpheme = custom_morphs(morpheme)  # 품사를 따져 불필요한 것은 버림

    return morpheme


def predictClass(sentence):
    tokenized_sentence = cleanUpSentence(sentence)
    bow = bag_of_words(tokenized_sentence, all_words)
    bow = np.array(bow).reshape(1, -1)
    res = model.predict(bow)

    # 지나치게 확률이 낮은 항목은 제외
    threshold = 0.1
    results = [[i, r] for i, r in enumerate(res[0]) if r > threshold]

    # 확률이 높은 순으로 정렬
    results.sort(key=lambda x: x[1], reverse=True)

    predictList = {}
    for r in results:
        predictList[classes[r[0]]] = r[1]

    return predictList


def getResponse(predictList, intents_json):
    for key, value in predictList.items():
        tag = key
        prob = value
        break

    if prob < 0.2:
        return "죄송합니다. 무슨 말씀이신지 알아듣지 못했어요."

    list_of_intents = intents_json['intents']
    for item in list_of_intents:
        if item['tag'] == tag:
            result = random.choice(item['responses'])
            break
    return result, tag

##########################################################################
# Main starts here...
##########################################################################

with open('intents.json', 'r') as f:
    intents = json.load(f)

with open('words.pkl', 'rb') as f:
    all_words = pickle.load(f)

with open('classes.pkl', 'rb') as f:
    classes = pickle.load(f)

model = load_model('chatbot_model.h5')

bot_name = "MaeChat"
listen_error_message = '죄송해요, 잘 알아듣지 못했어요.'
# textToSpeech('대화를 시작하려면, "t"키를 입력하세요.')

# start_message = '안녕하세요, 저는 매천고등학교의 AI 음성 로봇, 매챗이예요.'
# print(start_message)
# textToSpeech(start_message)

textLog = open('./log.txt', 'w') # make new file 'log.txt' to save dialogs
logLineCounter : int = 1 # set line counter for log.txt

while True:
    keypress = input(str('대화를 시작하려면, "t"키를 입력하세요: '))

    if keypress == 't':
        inputText : str = speechToText()

        pred_list = predictClass(inputText)
        outputList = getResponse(pred_list, intents)  # intents: json contents
        outputText = outputList[0]
        outputTag = outputList[1]

        showMap(outputTag)

        if inputText == '장비를 정지합니다':
            textToSpeech('프로그램을 종료합니다.')
            break

        if inputText == '점심' or inputText == '급식':
            lunchData = getLunchMenu(datetime.datetime.today().strftime('%Y%m%d'))
            if lunchData == 'noLunch':
                lunchData = '아쉽지만 오늘은 점심이 없는 날이예요.'
            else:
                lunchData: str = '오늘 점심 메뉴는 {} 이예요.'.format(lunchData)
            outputText = lunchData

        if inputText.strip() == "":
            print(listen_error_message)
            textToSpeech(listen_error_message)
            continue

        print(bot_name, ": ", outputText)
        textToSpeech(outputText)

        with open('./log.txt', 'a') as textLog: # save log in every chat
            textLog.write('{0} Input: {1}, Output: {2}\n'.format(logLineCounter, inputText, outputText))
        logLineCounter += 1

textLog.close()
