# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 17:57:17 2022

@author: sool0108
"""

#載入LineBot所需要的模組
from flask import Flask, request, abort
 
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

#======這裡是呼叫的檔案內容=====
from message import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========
import re
from spider import crawler

app = Flask(__name__)
 
# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('NVA8b6jsubntv8W2N9htB5ehD/o3i8mCYSo064V6dy4jQayt2PjW1OTrgI9U3iiVEIrHllOOB+ijah/SiBmxefHquaQcwnJFooCGneE/GDG+I9GJYzunzAoeG4T0FMVg3KQ9D2r+JiA6jSJabNSFdgdB04t89/1O/w1cDnyilFU=')
 
# 必須放上自己的Channel Secret
handler = WebhookHandler('b8cc6f8d42de0c27fb007e12eba363f7')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
 
  
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
 
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
 
    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    info_list = crawler()
    if '我是確診者' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '防疫攻略' in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '功能列表' in msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)
    elif '我是學生啦' in msg:
        message = TextSendMessage(text='1️⃣ 自主回報在校密切接觸者\n學校將聯絡衛生局開立居家隔離單\n☎️ 回報專線：02-29393091 \n\n（平日/上班時間）\n身健中心分機：77424 or 77425 \n（假日/非上班時間）\n學安中心分機：66119 or 0919099119 \n\n2️⃣ 請進行居家照護7天＋自主健康管理7天\n（自主健康管理期間做好個人防護可入校）\n3⃣️ 至台灣社交距離APP回報足跡')
        line_bot_api.reply_message(event.reply_token, message)
    elif '我是教職員啦' in msg:
        message = TextSendMessage(text='1️⃣ 自主回報在校密切接觸者\n學校將聯絡衛生局開立居家隔離單\n☎️ 回報專線：02-29393091\n\n（平日/上班時間）\n環安組分機：62823 \n（假日/非上班時間）\n學安中心分機：66119 or 0919099119\n\n2️⃣ 請進行居家照護7天＋自主健康管理7天\n（自主健康管理期間做好個人防護可入校）\n3⃣️ 至台灣社交距離APP回報足跡')
        line_bot_api.reply_message(event.reply_token, message)
    elif '我是密切接觸者' in msg:
        message = TextSendMessage(text='您有以下選擇：\n 1️⃣ 居家隔離3天＋自主防疫4天（不可入校、在宿舍不可外出）\n 2️⃣ 如果您是疫苗打滿三劑且快篩陰性者 可直接自主防疫七天（不可入校、在宿舍不可外出）')
        line_bot_api.reply_message(event.reply_token, message)
    elif '我是自我應變者' in msg:
        message = TextSendMessage(text='請自主監測3天 期間內不可入校，暫停實體上課、上班')
        line_bot_api.reply_message(event.reply_token, message)
    elif '我是自主健康管理者' in msg:
        message = TextSendMessage(text='1️⃣ 如果無任何症狀可正常生活，但外出請佩戴醫用口罩 \n2️⃣ 避免出入無法保持社交距離，或容易近距離接觸不特定人之場所 \n3⃣️ 禁止與他人進行近距離或群聚行之活動（例如：聚餐、聚會、公眾集會等）\n4⃣️ 禁止前往醫院陪病，亦應延後非急迫性需求之醫療或檢查')
        line_bot_api.reply_message(event.reply_token, message)
    elif '不確定定義' in msg:
        message = TextSendMessage(text='1️⃣ 確診者：PCR陽性 or 經醫師視訊評估快篩陽性 \n2️⃣ 密切接觸者：確診者的同住親友 or 同寢室友\n3⃣️ 自主應變者：與確診者前2日有任一方摘下口罩進行15分鐘以上接觸 \n4⃣️ 自主健康管理者：確診者進行居家照護7日後的7日為自主健康管理期間')
        line_bot_api.reply_message(event.reply_token, message)
    elif '哈' in msg:
        message = StickerSendMessage(package_id=1,sticker_id=1)
        line_bot_api.reply_message(event.reply_token, message)
    elif '線上看診' in msg:
        message = Carousel_Template_1()
        line_bot_api.reply_message(event.reply_token, message)
    elif '世誠診所線上預約看診流程' in msg:
        message = TextSendMessage(text='1️⃣ 加入世誠診所官方帳號\n2️⃣ 在對話欄寫上看診需求\n a.已 PCR 確診(日期)，想看診開藥\n b.剛快篩陽性，想確認並上傳疾管局及看診開藥\n3⃣️ 初診者，可先提供健保卡及聯絡電話，加快掛號速度。')
        line_bot_api.reply_message(event.reply_token, message)
    elif '世誠診所電話號碼' in msg:
        message = TextSendMessage(text='02-22343618')
        line_bot_api.reply_message(event.reply_token, message)
    elif '洪佑承診所線上預約看診流程' in msg:
        message = TextSendMessage(text='視訊門診前，可以先LINE先行知會，拍健保卡，說明初診，方便掛號。\n視訊看診時間為每週四五六的上午9:00-11:30及下午15:00-21:00')
        line_bot_api.reply_message(event.reply_token, message)
    elif '洪佑承診所電話號碼' in msg:
        message = TextSendMessage(text='02-29364708')
        line_bot_api.reply_message(event.reply_token, message)  
    elif '定安診所線上預約看診流程' in msg:
        message = TextSendMessage(text='1️⃣ 於 LINE 線上諮詢，安排看診時間。\n2️⃣ 醫師於約定時間致電\n3⃣️ 使用 LINE 視訊看診\n4.請親友攜帶健保卡來繳費領藥')
        line_bot_api.reply_message(event.reply_token, message)
    elif '定安診所電話號碼' in msg:
        message = TextSendMessage(text='02-29323755')
        line_bot_api.reply_message(event.reply_token, message)
    elif re.match('今日確診人數', msg):  # 點下今日確診人數的按鈕
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(info_list[0]))
        #print('Success:', info[0])
    elif '通報' in msg:  # 輸入通報兩個字
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(info_list[1]))
    elif '症狀緩解' in msg:
        message = Carousel_Template_2() #原本誤植為Confirm_Template
        line_bot_api.reply_message(event.reply_token, message)
    elif '喉嚨沙啞' in msg:
        message = TextSendMessage(text='建議您可以食用下列食品，來紓緩喉嚨沙啞的症狀喔！\n1️⃣ 蜂蜜水\n2️⃣ 喝水\n3️⃣ 喉嚨噴劑\n4️⃣ 含喉片\n5️⃣ 清冠一號')
        line_bot_api.reply_message(event.reply_token, message)
    elif '極度疲勞' in msg:
        message = TextSendMessage(text='建議您可以嘗試以下方式，來紓緩極度疲勞的症狀喔！\n1.充足的睡眠和休息，提升自身免疫力。\n2.維生素A以及維生素D以強化黏膜健康，幫助提升免疫功能。\n3.喝電解水。')
        line_bot_api.reply_message(event.reply_token, message)
    elif '肌肉痠痛' in msg:
        message = TextSendMessage(text='建議您可以嘗試以下方式，來紓緩極度疲勞的症狀喔！\n1.自我恢復：用靜態伸展減輕痠痛。\n2.按摩：讓酸痛部位得到直接的舒緩。')
        line_bot_api.reply_message(event.reply_token, message)
    elif '發燒頭痛' in msg:
        message = TextSendMessage(text='建議您可以嘗試以下方式，來紓解發燒的症狀喔！\n1.喝微溫的開水\n2.服用普拿疼\n3.貼退熱片\n4.溫毛巾擦拭')
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text='講這個我聽不懂啦！\n請你點選單才能叫出功能呦～')
        line_bot_api.reply_message(event.reply_token, message)
	
    
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
