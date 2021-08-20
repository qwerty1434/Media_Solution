#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 20:05:03 2019

@author: vp
"""
import requests
from bs4 import BeautifulSoup
import re
import random
from itertools import combinations
import numpy as np
import json
import bitly_api
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import urllib.request
LOGIN  = ""
API_KEY = ""
b = bitly_api.Connection(LOGIN, API_KEY)

def VentureSquare(url):#벤처스퀘어#html구조가 매우매우매우 깔끔!bb
    new_response = requests.get(url)
    new_soup = BeautifulSoup(new_response.text,"lxml")
    title = new_soup.find("h1",{"class":"post-title"}).text.replace('\n','').replace('\t','').replace('\r','')
    body = new_soup.find("div",{"class":"post-content"})
    #제거태그
    sharedaddy = new_soup.findAll("div",{"class":"sharedaddy"})
    for i in range(len(sharedaddy)):
        body = str(body).replace(str(sharedaddy[i]),"")
    text = re.sub("<[^>]*>",'',str(body))    
    img = BeautifulSoup(body).findAll("img")
    if len(img) >=2:
        img = [x['src'] for x in random.sample(img,2)]
    elif len(img) == 1:
        img = [x['src'] for x in img]
    elif len(img) == 0:
        img = 'null'
    date = new_soup.find("time").text#.text대신 ['datetime'가능]
    shorten_url = b.shorten(uri = url)['url']
    answer = [{"articleLink":shorten_url,"articleText":text,"articleImage":img,"articleDate":date,'title':title}]
    return answer    

url = "https://www.venturesquare.net/780398" #url = request.POST['url']

answer = VentureSquare(url)


#템플릿
Tem = {
"VN_018":{
    'sentences':1,
    'split_sentence':[[[2,7],[2,17],[4,24]]],
    'sentence_length':[48],
    'keyword':[],
    'image':1, 
    'input_order':[['t','t','t'],['i']]
    },
"VN_017":{
    'sentences':1,
    'split_sentence':[[[2,10],[2,10],[2,16]]],
    'sentence_length':[36],
    'keyword':[],
    'image':1,      
    'input_order':[['t','t','t'],['i']]
    },
"VN_016":{
    'sentences':1,
    'split_sentence':[[[2,11],[2,15]]],
    'sentence_length':[26],
    'keyword':[[1,6],[3,13]],
    'image':1,        
    'input_order':[None]
    },  
"VN_015":{
    'sentences':1,
    'split_sentence':[[[2,12],[2,12],[2,12],[2,12],[2,12]],[[4,18],[4,19]]], #똑같은 문장을 5마디,2마디로 나눔
    'sentence_length':[37],
    'keyword':[],
    'image':1,        
    'input_order':[['t'],['t'],['t'],['t'],['t'],['i','t','t']]
    },  
"VN_014":{
    'sentences':1,
    'split_sentence':[[[2,10],[2,10],[2,11],[8,24]]], #이걸 두번 넣음 #마지막은 sentence
    'sentence_length':[24],
    'keyword':[],
    'image':1,        
    'input_order':[None]
    },  
"VN_013":{
    'sentences':1,
    'split_sentence':[[[1,6],[2,11],[3,14]]],
    'sentence_length':[31],
    'keyword':[[5,17]],
    'image':1,        
    'input_order':[]
    },
"VN_012":{
    'sentences':1,
    'split_sentence':[[[5,17],[3,15]]],
    'sentence_length':[32],
    'keyword':[],
    'image':1,        
    'input_order':[['t','t'],['i']]
    },
"VN_011":{
    'sentences':1,
    'split_sentence':[[[3,12],[3,12],[3,12]]],
    'sentence_length':[36],
    'keyword':[],
    'image':1,        
    'input_order':[['i','t','t','t']]
    },
"VN_010":{
    'sentences':1,
    'split_sentence':[[[5,13],[5,13],[5,13]]],
    'sentence_length':[39],
    'keyword':[],
    'image':1,        
    'input_order':[['i','t','t','t']]
    },
"VN_009":{
    'sentences':1,
    'split_sentence':[[[4,16],[4,10],[4,24]]],
    'sentence_length':[50],
    'keyword':[],
    'image':1,        
    'input_order':[['i','t','t','t']]
    },
"VN_008":{
    'sentences':1,
    'split_sentence':[[[2,16],[2,12]]],
    'sentence_length':[28],
    'keyword':[],
    'image':1,        
    'input_order':[['i','t','t']]
    },
"VN_007":{
    'sentences':1,
    'split_sentence':[[[8,15],[4,13],[4,11]]],
    'sentence_length':[39],
    'keyword':[[1,5],[2,13]],
    'image':1,        
    'input_order':[None]
    },
"VN_006":{
    'sentences':1,
    'split_sentence':[[[5,24],[3,16],[5,30]]],
    'sentence_length':[70],
    'keyword':[],
    'image':1,        
    'input_order':[['i','t','t','t']]
    },
"VN_005":{
    'sentences':1,
    'split_sentence':[[[1,3],[2,9],[2,12]]],
    'sentence_length':[24],
    'keyword':[],
    'image':2,        
    'input_order':[['i','i','t','t','t']]
    },
"VN_004":{
    'sentences':2,
    'split_sentence':[[[5,17],[3,13]],[[10,25],[10,25],[10,25],[10,25]],[[5,17],[3,13]]],
    'sentence_length':[30,100],
    'keyword':[],
    'image':1,    
    'input_order':[['i','t','t','t','t','t','t'],['t','t']]
    },
"VN_003":{
    'sentences':1,
    'split_sentence':[[[[4,14],[4,14]]]],
    'sentence_length':[28],
    'keyword':[[3,16],[2,10],[1,5],[2,10]],
    'image':1,    
    'input_order':['k',['k','k','k'],'t','t']
    },
"VN_002":{
    'sentences':1,
    'split_sentence':[[[2,12],[2,12],[2,11],[2,11],[1,8],[1,6]],[[4,15],[4,16]]], #똑같은 문장을 6,2로 나눔
    'sentence_length':[31],
    'keyword':[],
    'image':1,    
    'input_order':[['i','t'],['t'],['t','t'],['t'],['t'],['t','t']]
    },
"VN_001":{
    'sentences':1,
    'split_sentence':[[[2,10],[2,11],[1,5],[3,11],[1,7]]],
    'sentence_length':[44],
    'keyword':[],
    'image':2,
    'input_order':['t','t','t',['i','i'],['t','t']]
    },       
}

text = answer[0]['title']
img1 = answer[0]['articleImage'][0] #이미지 2개일 때 계산하기
"""
try:
    img2 = answer[0]['articleImage'][1]
except:
    print("No second Image")
"""
url = answer[0]['articleLink']


"""
def Keyword(keyword,Key):
    combination_num = len(Tem[Key]['keyword'][0])-1
    if combination_num == 1:
        for i in combinations(range(len(keyword)-1),1):                
            var1 = ' '.join(keyword[:i[0]+1])
            var2 = ' '.join(keyword[i[0]+1:])
            if (Tem[Key]['keyword'][0][0][0]<len(var1)<Tem[Key]['keyword'][0][0][1]) and (Tem[Key]['keyword'][0][1][0]<len(var2)<Tem[Key]['keyword'][0][1][1]):
                return True
    elif combination_num == 2:
        for i in combinations(range(len(keyword)-1),2):
            var1 = ' '.join(keyword[:i[0]+1])
            var2 = ' '.join(keyword[i[0]+1:i[1]+1])
            var3 = ' '.join(keyword[i[1]+1:])                
            if (Tem[Key]['keyword'][0][0][0]<len(var1)<Tem[Key]['keyword'][0][0][1]) and(Tem[Key]['keyword'][0][1][0]<len(var2)<Tem[Key]['keyword'][0][1][1])and Tem[Key]['keyword'][0][2][0]<len(var3)<Tem[Key]['keyword'][0][2][1]:
                return True
    elif combination_num == 3:
        for i in combinations(range(len(keyword)-1),3):
            var1 = ' '.join(keyword[:i[0]+1])
            var2 = ' '.join(keyword[i[0]+1:i[1]+1])
            var3 = ' '.join(keyword[i[1]+1:i[2]+1])                
            var4 = ' '.join(keyword[i[2]+1:])
            if (Tem[Key]['keyword'][0][0][0]<len(var1)<Tem[Key]['keyword'][0][0][1]) and(Tem[Key]['keyword'][0][1][0]<len(var2)<Tem[Key]['keyword'][0][1][1])and Tem[Key]['keyword'][0][2][0]<len(var3)<Tem[Key]['keyword'][0][2][1] and Tem[Key]['keyword'][0][3][0]<len(var4)<Tem[Key]['keyword'][0][3][1] :
                return True
    elif combination_num == 4:
        for i in combinations(range(len(keyword)-1),4):
            var1 = ' '.join(keyword[:i[0]+1])
            var2 = ' '.join(keyword[i[0]+1:i[1]+1])
            var3 = ' '.join(keyword[i[1]+1:i[2]+1])                
            var4 = ' '.join(keyword[i[2]+1:i[3]+1])
            var5 = ' '.join(keyword[i[3]+1:])
            if (Tem[Key]['keyword'][0][0][0]<len(var1)<Tem[Key]['keyword'][0][0][1]) and(Tem[Key]['keyword'][0][1][0]<len(var2)<Tem[Key]['keyword'][0][1][1])and Tem[Key]['keyword'][0][2][0]<len(var3)<Tem[Key]['keyword'][0][2][1] and Tem[Key]['keyword'][0][3][0]<len(var4)<Tem[Key]['keyword'][0][3][1] and Tem[Key]['keyword'][0][4][0]<len(var5)<Tem[Key]['keyword'][0][4][1]:
                return True

def Text2_Test(text2,Key):
    text2_list = text2.split(' ')
    combination_num = len(Tem[Key]['split_sentence'][0])-1
    if combination_num == 1:
        for i in combinations(range(len(text2_list)-1),1):                
            var1 = ' '.join(text2_list[:i[0]+1])
            var2 = ' '.join(text2_list[i[0]+1:])
            if (Tem[Key]['split_sentence'][1][0][0]<len(var1)<Tem[Key]['split_sentence'][1][0][1]) and (Tem[Key]['split_sentence'][1][1][0]<len(var2)<Tem[Key]['split_sentence'][1][1][1]):
                return True
    elif combination_num == 2:
        for i in combinations(range(len(text2_list)-1),2):
            var1 = ' '.join(text2_list[:i[0]+1])
            var2 = ' '.join(text2_list[i[0]+1:i[1]+1])
            var3 = ' '.join(text2_list[i[1]+1:])                
            if (Tem[Key]['split_sentence'][1][0][0]<len(var1)<Tem[Key]['split_sentence'][1][0][1]) and(Tem[Key]['split_sentence'][1][1][0]<len(var2)<Tem[Key]['split_sentence'][1][1][1])and Tem[Key]['split_sentence'][1][2][0]<len(var3)<Tem[Key]['split_sentence'][1][2][1]:
                return True
    elif combination_num == 3:
        for i in combinations(range(len(text2_list)-1),3):
            var1 = ' '.join(text2_list[:i[0]+1])
            var2 = ' '.join(text2_list[i[0]+1:i[1]+1])
            var3 = ' '.join(text2_list[i[1]+1:i[2]+1])                
            var4 = ' '.join(text2_list[i[2]+1:])
            if (Tem[Key]['split_sentence'][1][0][0]<len(var1)<Tem[Key]['split_sentence'][1][0][1]) and(Tem[Key]['split_sentence'][1][1][0]<len(var2)<Tem[Key]['split_sentence'][1][1][1])and Tem[Key]['split_sentence'][1][2][0]<len(var3)<Tem[Key]['split_sentence'][1][2][1] and Tem[Key]['split_sentence'][1][3][0]<len(var4)<Tem[Key]['split_sentence'][1][3][1] :
                return True
    elif combination_num == 4:
        for i in combinations(range(len(text2_list)-1),4):
            var1 = ' '.join(text2_list[:i[0]+1])
            var2 = ' '.join(text2_list[i[0]+1:i[1]+1])
            var3 = ' '.join(text2_list[i[1]+1:i[2]+1])                
            var4 = ' '.join(text2_list[i[2]+1:i[3]+1])
            var5 = ' '.join(text2_list[i[3]+1:])
            if (Tem[Key]['split_sentence'][1][0][0]<len(var1)<Tem[Key]['split_sentence'][1][0][1]) and(Tem[Key]['split_sentence'][1][1][0]<len(var2)<Tem[Key]['split_sentence'][1][1][1])and Tem[Key]['split_sentence'][1][2][0]<len(var3)<Tem[Key]['split_sentence'][1][2][1] and Tem[Key]['split_sentence'][1][3][0]<len(var4)<Tem[Key]['split_sentence'][1][3][1] and Tem[Key]['split_sentence'][1][4][0]<len(var5)<Tem[Key]['split_sentence'][1][4][1]:
                return True
#textrankr 붙이기(왜 쥬피터에서는 되는데 스파이더에서는 안되는건데 -> 1.스파이더(궁극적으로 aws서버)에서 되게한다 2.google coolab에서 쓰는방안 조사)

if len(answer[0]['articleText'] 를 문장추출한 결과) >= Tem[Key_value]['sentences'] and \
len(answer[0]['articleText']에서 키워드추출한 결과) >= Tem[Key_value]['keyword'] and \
len(answer[0]['articleImage']) >= Tem[Key_value]['image'] : and \
1번문장 조건 (Text1_Test(text1,Key)//2번조건 복붙하기) and 키워드 조건 Keyword(keyword,Key) and 2번문장 조건 (Text2_Test(text2,Key)): score(selected_comb.append({Key:var몇개를 어케쓰지}))
한 문장을 두번쓰면 어카
"""

#Asset확인

def Score(selected_comb):
    score_list = []
    Key_value = list(selected_comb[0].keys())[0]
    for i in range(len(selected_comb)):
        normal = (Tem[Key_value]['sentence_length'][0]-len(text))/len(Tem[Key_value]['split_sentence'][0])
        score = [np.sqrt(len(j)-normal) for j in selected_comb[i][Key_value]]
        score_list.append(sum(score))
    return selected_comb[score_list.index(min(score_list))]


def Matching(text):
    text_list = text.split(' ')
    all_template = []
    while len(set(all_template)) != len(Tem):
        #print(all_template)
        Key,Value = random.choice(list(Tem.items()))
        all_template.append(Key)
        combination_num = len(Tem[Key]['split_sentence'][0])-1
        if combination_num == 1:
            selected_comb = []
            for i in combinations(range(len(text_list)-1),1):                
                var1 = ' '.join(text_list[:i[0]+1])
                var2 = ' '.join(text_list[i[0]+1:])
                if (Tem[Key]['split_sentence'][0][0][0]<len(var1)<Tem[Key]['split_sentence'][0][0][1]) and (Tem[Key]['split_sentence'][0][1][0]<len(var2)<Tem[Key]['split_sentence'][0][1][1]):
                    if (Tem[Key]['sentences'] == 1) and len(Tem[Key]['keyword']) == 0 and Tem[Key]['image'] == 1:#문장1개,키워드0개,이미지1개
                        selected_comb.append({Key:[var1,var2]})
                    """#핵심문장을 2개 쓰는 경우
                    elif Tem[Key]['sentences'] == 2:
                        if Text2_Test(text2,Key):
                            selected_comb.append({Key:[var1,var2]})
                    """
            if len(selected_comb) !=0:
                #print(selected_comb)
                return Score(selected_comb)
        elif combination_num == 2:
            selected_comb = []
            for i in combinations(range(len(text_list)-1),2):
                var1 = ' '.join(text_list[:i[0]+1])
                var2 = ' '.join(text_list[i[0]+1:i[1]+1])
                var3 = ' '.join(text_list[i[1]+1:])                
                if (Tem[Key]['split_sentence'][0][0][0]<len(var1)<Tem[Key]['split_sentence'][0][0][1]) and (Tem[Key]['split_sentence'][0][1][0]<len(var2)<Tem[Key]['split_sentence'][0][1][1])and Tem[Key]['split_sentence'][0][2][0]<len(var3)<Tem[Key]['split_sentence'][0][2][1]:
                    if (Tem[Key]['sentences'] == 1) and len(Tem[Key]['keyword']) == 0 and Tem[Key]['image'] == 1:#문장1개,키워드0개,이미지1개
                        selected_comb.append({Key:[var1,var2,var3]})
                    """#핵심문장을 2개 쓰는 경우
                    elif Tem[Key]['sentences'] == 2:
                        if Text2_Test(text2,Key):
                            selected_comb.append({Key:[var1,var2,var3]})
                    """
            if len(selected_comb) !=0:
                #print(selected_comb)
                return Score(selected_comb)
        elif combination_num == 3:
            selected_comb = []
            for i in combinations(range(len(text_list)-1),3):
                var1 = ' '.join(text_list[:i[0]+1])
                var2 = ' '.join(text_list[i[0]+1:i[1]+1])
                var3 = ' '.join(text_list[i[1]+1:i[2]+1])                
                var4 = ' '.join(text_list[i[2]+1:])
                if (Tem[Key]['split_sentence'][0][0][0]<len(var1)<Tem[Key]['split_sentence'][0][0][1]) and (Tem[Key]['split_sentence'][0][1][0]<len(var2)<Tem[Key]['split_sentence'][0][1][1])and Tem[Key]['split_sentence'][0][2][0]<len(var3)<Tem[Key]['split_sentence'][0][2][1] and Tem[Key]['split_sentence'][0][3][0]<len(var4)<Tem[Key]['split_sentence'][0][3][1] :
                    if (Tem[Key]['sentences'] == 1) and len(Tem[Key]['keyword']) == 0 and Tem[Key]['image'] == 1:#문장1개,키워드0개,이미지1개
                        selected_comb.append({Key:[var1,var2,var3,var4]})
                    """#핵심문장을 2개 쓰는 경우
                    elif Tem[Key]['sentences'] == 2:
                        if Text2_Test(text2,Key):
                            selected_comb.append({Key:[var1,var2,var3,var4]})
                    """
            if len(selected_comb) !=0:
                #print(selected_comb)
                return Score(selected_comb)
        elif combination_num == 4:
            selected_comb = []
            for i in combinations(range(len(text_list)-1),4):
                var1 = ' '.join(text_list[:i[0]+1])
                var2 = ' '.join(text_list[i[0]+1:i[1]+1])
                var3 = ' '.join(text_list[i[1]+1:i[2]+1])                
                var4 = ' '.join(text_list[i[2]+1:i[3]+1])
                var5 = ' '.join(text_list[i[3]+1:])
                if (Tem[Key]['split_sentence'][0][0][0]<len(var1)<Tem[Key]['split_sentence'][0][0][1]) and (Tem[Key]['split_sentence'][0][1][0]<len(var2)<Tem[Key]['split_sentence'][0][1][1])and Tem[Key]['split_sentence'][0][2][0]<len(var3)<Tem[Key]['split_sentence'][0][2][1] and Tem[Key]['split_sentence'][0][3][0]<len(var4)<Tem[Key]['split_sentence'][0][3][1] and Tem[Key]['split_sentence'][0][4][0]<len(var5)<Tem[Key]['split_sentence'][0][4][1]:
                    if (Tem[Key]['sentences'] == 1) and len(Tem[Key]['keyword']) == 0 and Tem[Key]['image'] == 1:#문장1개,키워드0개,이미지1개
                        selected_comb.append({Key:[var1,var2,var3,var4,var5]})
                    """#핵심문장을 2개 쓰는 경우                        
                    elif Tem[Key]['sentences'] == 2:
                        if Text2_Test(text2,Key):
                            selected_comb.append({Key:[var1,var2,var3,var4,var5]})
                    """
            if len(selected_comb) !=0:
                #print(selected_comb)
                return Score(selected_comb)
result = Matching(text)

#Api연결


#템플릿 리스트
headers = {'Content-Type': 'application/json; charset=utf-8'}
res1 = requests.get("http://54.180.2.77:8000/template",headers=headers)
#res1 = requests.get("https://tapi.vplate.io/vvinew",headers=headers, verify=False)


Template_data = res1.json()
def Find_Id(Template_data):
    for i in range(len(Template_data)):
        if(list(result.keys())[0][3:] in Template_data[i]['projectPath']):
            return Template_data[i]['_id']

#사본 템플릿
res3 = requests.post("http://54.180.2.77:8000/subtemplate",{'templateId':Find_Id(Template_data)})
print("템플릿 구매 완료")
#값 채우기(최종전송)
im = [img1]
tx = list(result.values())[0]
skin = Tem[list(result.keys())[0]]['input_order']
def fill_data(skin,im,tx):
    im.reverse()
    tx.reverse()
    for i in range(len(skin)):
        if type(skin[i]) == list:
            for j in range(len(skin[i])):
                if skin[i][j] == 't':
                    skin[i][j] = tx.pop()
                elif skin[i][j] == 'i':
                    skin[i][j] = im.pop()
        else:
            if skin[i] == 't':
                skin[i] = tx.pop()
            elif skin[i] =='i':
                skin[i] = im.pop()
    return skin

data1 = json.dumps(fill_data(skin,im,tx))#깨지면ensure_ascii=False해보기
res5 = requests.patch("http://54.180.2.77:8000/subtemplate/%s"%res3.json()['subtemplate']['_id'],data1,headers=headers)
print("res5:",res5)

#status1 변경
data2 = json.dumps({'status':1})
res6 = requests.patch("http://54.180.2.77:8000/subtemplate/ready/%s"%res3.json()['subtemplate']['_id'],data2,headers=headers)
print("res6:",res6)
"""
#구매한 리스트에서 결과값 찾기
Token = True
while Token:
    time.sleep(60)
    res4 = requests.get("http://54.180.2.77:8000/subtemplate")
    for i in range(len(res4.json())):
        if res4.json()[i]['_id'] == res3.json()['subtemplate']['_id']:
            if type(res4.json()[0]['renderCompleteVideo']) is not type(None):
                Token = False
                video_url = res4.json()[i]['renderCompleteVideo']
                break;
#video_url_download

urllib.request.urlretrieve(video_url,"/home/ubuntu/media_solution/Media_Solution/video/video_name.mp4") 
"""

#업로드

fb_id = ""
fb_pw = ""

#os.chdir("/Users/vp/Downloads")
first_page = "https://www.facebook.com/"
#driver = webdriver.Chrome("/Users/vp/Downloads/chromedriver")
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=options)
#driver = webdriver.PhantomJS('/Users/vp/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs') #모바일로 간다

driver.implicitly_wait(3)
driver.get(first_page)#주소

driver.find_element_by_id("email").send_keys(fb_id)#아이디
driver.find_element_by_name("pass").send_keys(fb_pw)#비밀번호
driver.find_element_by_xpath("//input[@type='submit']").click()


"""
#모바일 버전 ->PhantomJS일 때
driver.find_element_by_id("m_login_email").send_keys(fb_id)#아이디
driver.find_element_by_id("m_login_password").send_keys(fb_pw)#비밀번호
driver.find_element_by_id("u_0_5").click()#클릭
driver.implicitly_wait(2)
"""
#여기부터 동일
driver.get("https://www.facebook.com/Vvinew/videos")#비뉴 페이지로 이동
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
driver.implicitly_wait(3)
#print(driver.find_element_by_id("content_container").text)
"""
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
lst = soup.findAll("input")
"""

driver.find_element_by_xpath("//input[@data-testid='search_input']").send_keys("/home/ubuntu/media_solution/Media_Solution/video/video_name.mp4")
driver.implicitly_wait(3)
driver.find_element_by_css_selector("label._6r02").send_keys(answer[0]['title'])#제목
driver.implicitly_wait(3)
driver.find_element_by_css_selector("div.notranslate").send_keys(answer[0]['title']+'\n'+'▶'+answer[0]['articleLink'])#내용
driver.implicitly_wait(3)
driver.find_element_by_xpath("//a[@data-testid='VIDEO_COMPOSER_NEXT_BUTTON']").click()
driver.implicitly_wait(3)
driver.find_element_by_xpath("//a[@data-testid='VIDEO_COMPOSER_PUBLISH_BUTTON']").click()
driver.implicitly_wait(10)







"""
os.chdir("/Users/vp/Downloads")
first_page = "https://www.facebook.com/"
driver = webdriver.Chrome("/Users/vp/Downloads/chromedriver")
driver.implicitly_wait(3)
driver.get(first_page)#주소
driver.find_element_by_id("email").send_keys(fb_id)#아이디
driver.find_element_by_name("pass").send_keys(fb_pw)#비밀번호
driver.find_element_by_xpath("//input[@type='submit']").click()
driver.implicitly_wait(2)
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
driver.get("https://www.facebook.com/Vvinew/videos")#비뉴 페이지로 이동
#드라이버 확인
print(driver.find_element_by_id("content_container").text)
driver.find_element_by_id("js_19").send_keys(os.getcwd()+"/Tem111.mp4")#영상 넣기
driver.find_element_by_css_selector("label._6r02").send_keys(answer[0]['title'])#제목
driver.find_element_by_css_selector("div.notranslate").send_keys(answer[0]['title']+'\n'+'▶'+answer[0]['articleLink'])#내용
driver.find_element_by_css_selector("div._6elw").click()
driver.quit()#종료
"""
