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

app = Flask(__name__)
 
# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('gLV0oCQgizV2XRMPDBARn0K5g0P4oMh1FA1qcdYq2XyISLkAaDEeOuEwOUxtLISlIn/5frMaI7NFcKFTNn61N9PB72P0Vc30eaFikUer24mFkb3ucnaMQmFBNvNk6nQvDJ4MbeezPOuht8kdt6pdoQdB04t89/1O/w1cDnyilFU=')
 
# 必須放上自己的Channel Secret
handler = WebhookHandler('254fba9cca783bc9c96dff144ef5bd4a')

line_bot_api.push_message('Ud5516708abb79e53d540e3a9d15e1a0a', TextSendMessage(text='你可以開始了'))

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
import re
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if "旋轉木馬" in msg:
        buttons_template_message = TemplateSendMessage(
        alt_text = "旋轉木馬",
        template=CarouselTemplate( 
            columns=[ 
                    CarouselColumn( 
                        thumbnail_image_url ="https://upload.wikimedia.org/wikipedia/zh/thumb/3/33/National_Chengchi_University_logo.svg/1200px-National_Chengchi_University_logo.svg.png",
                        title = "我的身分是...", 
                        text ="請點選符合的身分了解因應方式", 
                        actions =[
                            MessageAction( 
                                label= "確診者",
                                text= "確診者應該..."),
                            MessageAction( 
                                label= "密切接觸者",
                                text= "密切接觸者應該..."),
                            MessageAction( 
                                label= "不清楚",
                                text= "OK"),
				
                        ]
                    ),
                    CarouselColumn( 
                        thumbnail_image_url ="https://upload.wikimedia.org/wikipedia/zh/thumb/3/33/National_Chengchi_University_logo.svg/1200px-National_Chengchi_University_logo.svg.png",
                        title = "症狀緩解方式", 
                        text ="請點選症狀了解緩解方式", 
                        actions =[
                            MessageAction( 
                                label= "A",
                                text= "AAAA"),
                            MessageAction( 
                                label= "B",
                                text= "BBBB"),
                            MessageAction( 
                                label= "C",
                                text= "CCCC"),
				
                        ]
                    ),
                ]
            )
         )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    elif "防疫23" in msg:
        buttons_template_message = TemplateSendMessage(
        alt_text = "防疫攻略",
        template=CarouselTemplate( 
            columns=[ 
                    CarouselColumn( 
                        thumbnail_image_url ="https://www.nccu.edu.tw/var/file/0/1000/img/12/1651482462275s.jpg",
                        title = "我的身分是...", 
                        text ="請點選符合的身分了解因應方式", 
                        actions =[
                            MessageAction( 
                                label= "確診者",
                                text= "確診者應該..."),
                            MessageAction( 
                                label= "密切接觸者",
                                text= "密切接觸者應該..."),
                            MessageAction( 
                                label= "不清楚",
                                text= "OK"),
				
                        ]
                    ),
                    CarouselColumn( 
                        thumbnail_image_url ="https://www.nccu.edu.tw/var/file/0/1000/img/12/1651482462275s.jpg",
                        title = "症狀緩解方式", 
                        text ="請點選症狀了解緩解方式", 
                        actions =[
                            MessageAction( 
                                label= "A",
                                text= "AAAA"),
                            MessageAction( 
                                label= "B",
                                text= "BBBB"),
                            MessageAction( 
                                label= "C",
                                text= "CCCC"),
				
                        ]
                    ),
                ]
            )
         )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
	

    elif '我是確診者' in msg:
        message = Confirm_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '防疫攻略' in msg:
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '功能列表' in msg:
        message = function_list()
        line_bot_api.reply_message(event.reply_token, message)
    elif '我是學生啦' in msg:
        message = TextSendMessage(text='1️⃣自主回報在校密切接觸者\n學校將聯絡衛生局開立居家隔離單\n☎️ 回報專線：02-29393091 \n\n（平日/上班時間）\n身健中心分機：77424 or 77425 \n（假日/非上班時間）\n學安中心分機：66119 or 0919099119 \n\n2️⃣ 請進行居家照護7天＋自主健康管理7天\n（自主健康管理期間做好個人防護可入校）\n3⃣️ 至台灣社交距離APP回報足跡')
        line_bot_api.reply_message(event.reply_token, message)
    elif '我是教職員啦' in msg:
        message = TextSendMessage(text='1. 自主回報在校密切接觸者\n學校將聯絡衛生局開立居家隔離單\n☎️ 回報專線：02-29393091\n\n（平日/上班時間）\n環安組分機：62823 \n（假日/非上班時間）\n學安中心分機：66119 or 0919099119\n\n2️⃣ 請進行居家照護7天＋自主健康管理7天\n（自主健康管理期間做好個人防護可入校）\n3⃣️ 至台灣社交距離APP回報足跡')
        line_bot_api.reply_message(event.reply_token, message)
    elif '我是密切接觸者' in msg:
        message = TextSendMessage(text='您有以下選擇：\n 1️⃣ 居家隔離3天＋自主防疫4天（不可入校、在宿舍不可外出）\n 2️⃣  如果您是疫苗打滿三劑且快篩陰性者 可直接自主防疫七天（不可入校、在宿舍不可外出）')
        line_bot_api.reply_message(event.reply_token, message)
    elif '我是自我應變者' in msg:
        message = TextSendMessage(text='請自主監測3天 期間內不可入校，暫停實體上課、上班')
        line_bot_api.reply_message(event.reply_token, message)
    elif '我是自主健康管理者' in msg:
        message = TextSendMessage(text='1️⃣  如果無任何症狀可正常生活，但外出請佩戴醫用口罩 \n2️⃣ 避免出入無法保持社交距離，或容易近距離接觸不特定人之場所 \n3⃣️ 禁止與他人進行近距離或群聚行之活動（例如：聚餐、聚會、公眾集會等）\n4⃣️ 禁止前往醫院陪病，亦應延後非急迫性需求之醫療或檢查')
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
        message = TextSendMessage(text='1.加入世誠診所官方帳號\n2.在對話欄寫上看診需求\n a.已 PCR 確診(日期)，想看診開藥\n b.剛快篩陽性，想確認並上傳疾管局及看診開藥\n3.初診者，可先提供健保卡及聯絡電話，加快掛號速度。')
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
        message = TextSendMessage(text='1.於 LINE 線上諮詢，安排看診時間。\n2.醫師於約定時間致電\n3.使用 LINE 視訊看診\n4.請親友攜帶健保卡來繳費領藥')
        line_bot_api.reply_message(event.reply_token, message)
    elif '定安診所電話號碼' in msg:
        message = TextSendMessage(text='02-29323755')
        line_bot_api.reply_message(event.reply_token, message)
    else:
        message = TextSendMessage(text='講這個我聽不懂啦！\n請你點選單才能叫出功能呦～')
        line_bot_api.reply_message(event.reply_token, message)
	
    
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
