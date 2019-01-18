# -*- coding: utf-8 -*-
import sys
import os
import requests
from bs4 import BeautifulSoup
import re


os.system("test&cls")
main_list = {"펌프 잇 업":"https://namu.wiki/w/%ED%8E%8C%ED%94%84%20%EC%9E%87%20%EC%97%85","EZ2DJ":"https://namu.wiki/w/EZ2AC%20%EC%8B%9C%EB%A6%AC%EC%A6%88?from=EZ2DJ","EZ2AC":"https://namu.wiki/w/EZ2AC%20%EC%8B%9C%EB%A6%AC%EC%A6%88?from=EZ2AC","Beatmania IIDX":"https://namu.wiki/w/beatmania%20IIDX","26 Rootage":"https://namu.wiki/w/beatmania%20IIDX%2026%20Rootage","REFLEC BEAT":"https://namu.wiki/w/%EB%A6%AC%ED%94%8C%EB%A0%89%20%EB%B9%84%ED%8A%B8%20%EC%8B%9C%EB%A6%AC%EC%A6%88","유구의 리플레시아":"https://namu.wiki/w/%EB%A6%AC%ED%94%8C%EB%A0%89%20%EB%B9%84%ED%8A%B8%20%EC%9C%A0%EA%B5%AC%EC%9D%98%20%EB%A6%AC%ED%94%8C%EB%A0%88%EC%8B%9C%EC%95%84","Pop'n music":"https://namu.wiki/w/%ED%8C%9D%ED%94%88%EB%AE%A4%EC%A7%81","Peace":"https://namu.wiki/w/%ED%8C%9D%ED%94%88%EB%AE%A4%EC%A7%81%20peace","SOUND VOLTEX":"https://namu.wiki/w/%EC%82%AC%EC%9A%B4%EB%93%9C%20%EB%B3%BC%ED%85%8D%EC%8A%A4%20%EC%8B%9C%EB%A6%AC%EC%A6%88?from=%EC%82%AC%EC%9A%B4%EB%93%9C%20%EB%B3%BC%ED%85%8D%EC%8A%A4","IV HEAVENLY HAVEN":"https://namu.wiki/w/%EC%82%AC%EC%9A%B4%EB%93%9C%20%EB%B3%BC%ED%85%8D%EC%8A%A4%20IV%20%ED%97%A4%EB%B8%90%EB%A6%AC%20%ED%97%A4%EC%9D%B4%EB%B8%90","DanceDanceRevolutionA":"https://namu.wiki/w/DanceDanceRevolution","노스텔지어":"https://namu.wiki/w/%EB%85%B8%EC%8A%A4%ED%85%94%EC%A7%80%EC%96%B4%20%EC%8B%9C%EB%A6%AC%EC%A6%88","노스텔지어 Op.2":"https://namu.wiki/w/%EB%85%B8%EC%8A%A4%ED%85%94%EC%A7%80%EC%96%B4%20Op.2","GITADORA":"https://namu.wiki/w/GITADORA%20%EC%8B%9C%EB%A6%AC%EC%A6%88","EXCHAIN":"https://namu.wiki/w/GITADORA%20EXCHAIN","Dancerush":"https://namu.wiki/w/DANCERUSH%20STARDOM?from=DANCERUSH","Stardom":"https://namu.wiki/w/DANCERUSH%20STARDOM","JUBEAT":"https://namu.wiki/w/%EC%9C%A0%EB%B9%84%ED%8A%B8%20%EC%8B%9C%EB%A6%AC%EC%A6%88","FESTO":"https://namu.wiki/w/%EC%9C%A0%EB%B9%84%ED%8A%B8%20%ED%8E%98%EC%8A%A4%ED%86%A0","태고의 달인":"https://namu.wiki/w/%ED%83%9C%EA%B3%A0%EC%9D%98%20%EB%8B%AC%EC%9D%B8%20%EC%8B%9C%EB%A6%AC%EC%A6%88","싱크로니카":"https://namu.wiki/w/%EC%8B%B1%ED%81%AC%EB%A1%9C%EB%8B%88%EC%B9%B4","아이카츠":"https://namu.wiki/w/%EC%95%84%EC%9D%B4%EC%97%A0%EC%8A%A4%ED%83%80!%20%EA%BF%88%EC%9D%98%20%EC%98%A4%EB%94%94%EC%85%98!(%EC%95%84%EC%BC%80%EC%9D%B4%EB%93%9C%20%EA%B2%8C%EC%9E%84)","그루브코스터":"https://namu.wiki/w/GROOVE%20COASTER?from=%EA%B7%B8%EB%A3%A8%EB%B8%8C%20%EC%BD%94%EC%8A%A4%ED%84%B0","CHUNITHM":"https://namu.wiki/w/CHUNITHM","Maimai":"https://namu.wiki/w/maimai%20%EC%8B%9C%EB%A6%AC%EC%A6%88","프로젝트 디바 시리즈":"https://namu.wiki/w/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%20%EB%94%94%EB%B0%94%20%EC%8B%9C%EB%A6%AC%EC%A6%88","온게키":"https://namu.wiki/w/%EC%98%A8%EA%B2%8C%ED%82%A4","뮤지박스":"https://namu.wiki/w/%EB%AE%A4%EC%A7%80%EB%B0%95%EC%8A%A4","네온fm":"https://namu.wiki/w/%EB%84%A4%EC%98%A8%20FM","Rerave":"https://namu.wiki/w/RERAVE","프리즘 스톤":"https://namu.wiki/w/%EA%BF%88%EC%9D%98%20%EB%B3%B4%EC%84%9D%20%ED%94%84%EB%A6%AC%EC%A6%98%20%EC%8A%A4%ED%86%A4","프리파라":"https://namu.wiki/w/%ED%94%84%EB%A6%AC%ED%8C%8C%EB%9D%BC/%EC%95%84%EC%BC%80%EC%9D%B4%EB%93%9C%20%EA%B2%8C%EC%9E%84","러브라이브! 스쿠페스":"https://namu.wiki/w/%EB%9F%AC%EB%B8%8C%20%EB%9D%BC%EC%9D%B4%EB%B8%8C!%20%EC%8A%A4%EC%BF%A8%20%EC%95%84%EC%9D%B4%EB%8F%8C%20%ED%8E%98%EC%8A%A4%ED%8B%B0%EB%B2%8C%20%E3%80%9Cafter%20school%20ACTIVITY%E3%80%9C?from=%EB%9F%AC%EB%B8%8C%20%EB%9D%BC%EC%9D%B4%EB%B8%8C!%20%EC%8A%A4%EC%BF%A8%20%EC%95%84%EC%9D%B4%EB%8F%8C%20%ED%8E%98%EC%8A%A4%ED%8B%B0%EB%B2%8C%20~after%20school%20ACTIVITY~","러브비트":"https://namu.wiki/w/%EB%9F%AC%EB%B8%8C%EB%B9%84%ED%8A%B8","엠스타":"https://namu.wiki/w/%ED%81%B4%EB%9F%BD%20%EC%97%A0%EC%8A%A4%ED%83%80?from=%EC%97%A0%EC%8A%A4%ED%83%80","터치 온라인":"https://namu.wiki/w/%ED%84%B0%EC%B9%98%20%EC%98%A8%EB%9D%BC%EC%9D%B8","DJMAX 시리즈":"https://namu.wiki/w/DJMAX%20%EC%8B%9C%EB%A6%AC%EC%A6%88","응원단 시리즈":"https://namu.wiki/w/%EC%9D%91%EC%9B%90%EB%8B%A8%20%EC%8B%9C%EB%A6%AC%EC%A6%88","리듬 천국 시리즈":"https://namu.wiki/w/%EB%A6%AC%EB%93%AC%20%EC%84%B8%EC%83%81%20%EC%8B%9C%EB%A6%AC%EC%A6%88","뿌요뿌요 da!":"https://namu.wiki/w/%EB%BF%8C%EC%9A%94%EB%BF%8C%EC%9A%94%20DA!","아이돌 마스터 시리즈":"https://namu.wiki/w/THE%20iDOLM%40STER?from=%EC%95%84%EC%9D%B4%EB%8F%8C%20%EB%A7%88%EC%8A%A4%ED%84%B0%20%EC%8B%9C%EB%A6%AC%EC%A6%88","저스트 댄스":"https://namu.wiki/w/%EC%A0%80%EC%8A%A4%ED%8A%B8%20%EB%8C%84%EC%8A%A4%20%EC%8B%9C%EB%A6%AC%EC%A6%88?from=%EC%A0%80%EC%8A%A4%ED%8A%B8%20%EB%8C%84%EC%8A%A4","Beat Saber":"https://namu.wiki/w/Beat%20Saber?from=%EB%B9%84%ED%8A%B8%20%EC%84%B8%EC%9D%B4%EB%B2%84","Cytus":"https://namu.wiki/w/Cytus","Deemo":"https://namu.wiki/w/Deemo","Crypt of the NecroDancer":"https://namu.wiki/w/Crypt%20of%20the%20NecroDancer","VOEZ":"https://namu.wiki/w/VOEZ","리듬 스타":"https://namu.wiki/w/%EB%A6%AC%EB%93%AC%EC%8A%A4%ED%83%80%20%EC%8B%9C%EB%A6%AC%EC%A6%88","Dynamics":"https://namu.wiki/w/Dynamix"}

def croll(link):
    rq = requests.get(link)
    rqctnt = rq.content
    soup = BeautifulSoup(rqctnt,"html.parser")

    OMG = str(soup.find_all("p"))

    OMG = re.sub('<.+?>', '', OMG, 0).strip()
    print(OMG)



def maintitle():
    title = "자람 리듬게임 위키"
    print("\n\n\n")
    print("%90s"%(title))
    print("\n\n\n")

search = "x"
def mainmenu():
    count = 0
    fir = []
    sec = []
    thi = []
    fou = []
    fif = []

    for i in main_list:
        if count % 5 == 0:
            fir.append(i)
        elif count % 5 ==1:
            sec.append(i)
        elif count % 5 ==2:
            thi.append(i)
        elif count % 5 ==3:
            fou.append(i)
        else:
            fif.append(i)
        count = count+1

    for i in range(len(fif)):
        print("%30s%30s%30s%30s%30s"%(fir[i],sec[i],thi[i],fou[i],fif[i]))

    for i in range(len(fif),len(fou)):
        print("%30s%30s%30s%30s"%(fir[i],sec[i],thi[i],fou[i]))

    for i in range(len(fou),len(thi)):
        print("%30s%30s%30s"%(fir[i],sec[i],thi[i]))

    for i in range(len(thi),len(sec)):
        print("%30s%30s"%(fir[i],sec[i]))

    for i in range(len(sec),len(fir)):
        print("%30s"%(fir[i]))

    print("검색하고 싶은 단어를 입력해주세요! g 검색어를 입력하면 모바일 리듬게임을 확인하실 수 있습니다.")
    search = input("검색> ")

    if(search in main_list):
        croll(main_list[search])
    elif search == 'g':
            rq = requests.get("https://play.google.com/store/apps/category/GAME_MUSIC?hl=ko")
            rqctnt = rq.content
            soup = BeautifulSoup(rqctnt,"html.parser")
            soup = soup.find_all(attrs={'class':'title'})

            blacklsit = ["앱","영화/TV","음악","도서","기기","엔터테인먼트","음악"]

            for link in soup:
                if link.text.strip() in blacklsit:
                    pass
                else:
                    print(link.text.strip())

    else:
        print("해당 검색어는 존재하지 않습니다.")



maintitle()
mainmenu()
