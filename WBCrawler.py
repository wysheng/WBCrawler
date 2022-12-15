# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 21:25:51 2022

@author: lzh
"""
from selenium import webdriver
import time
from selenium.webdriver import Chrome

#from selenium.webdriver.common.by import By

from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from urllib.parse import urlencode


browser = webdriver.Chrome()

browser.set_window_size(1400, 1000)


url ='https://weibo.com/'

browser.get(url)

browser.implicitly_wait(10)

su_button=browser.find_element(By.CLASS_NAME,'LoginCard_btn_Jp_u1')#查找登录按钮

time.sleep(10)
su_button.click()

time.sleep(10)

search_word='共同富裕'#搜索词
page_count=50;#翻页

content="";
for page in range(1,page_count+1):
    params={"q":search_word,"page":page}
    url='https://s.weibo.com/weibo?'+urlencode(params)
    browser.execute_script('window.location="'+url+'"');#搜索路径
    time.sleep(5)
    #card-wrap
    cards=browser.find_elements(By.CLASS_NAME,'card-wrap')#查找结果列表
    for card in cards:
        aType=card.get_attribute('action-type')
        if aType=='feed_list_item':
            name=card.find_element(By.CLASS_NAME,'name').text;#账号
            from_a=card.find_element(By.CLASS_NAME,'from').text;#来源日期
            text=card.find_element(By.CLASS_NAME,'txt').text;#内容
            content=content+"\n"+"===========================================================================================================================================================";
            #print('===========================================================================================================================================================')
            #print(name)
            content=content+"\n"+name;
            content=content+"\n"+'+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++';
            #print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            #print(from_a)
            content=content+"\n"+from_a
            content=content+"\n"+'+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++';
            #print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            #print(text)
            content=content+"\n"+text+'\n'
            #print('===========================================================================================================================================================')
            content=content+"\n"+'==========================================================================================================================================================='
            print(content);
        
file=open(search_word+".txt",'w',encoding='utf-8');
file.write(content)
file.close()
           







    








