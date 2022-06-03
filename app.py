# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 16:45:14 2022

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
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token,message)
    
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
   
message = TemplateSendMessage(
    alt_text='旋轉木馬',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://upload.wikimedia.org/wikipedia/zh/thumb/3/33/National_Chengchi_University_logo.svg/1200px-National_Chengchi_University_logo.svg.png',
                title='我的身份是......',
                text='副標題1',
                actions=[
                    URITemplateAction(
                        label='連結點這邊',
                        uri='URL連結放此'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://upload.wikimedia.org/wikipedia/zh/thumb/3/33/National_Chengchi_University_logo.svg/1200px-National_Chengchi_University_logo.svg.png',
                title='症狀緩解',
                text='副標題2',
                actions=[
                    URITemplateAction(
                        label='連結點這邊',
                        uri='URL連結放此'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://upload.wikimedia.org/wikipedia/zh/thumb/3/33/National_Chengchi_University_logo.svg/1200px-National_Chengchi_University_logo.svg.png',
                title='查詢線上看診診所',
                text='副標題',
                actions=[
                    URITemplateAction(
                        label='連結點這邊',
                        uri='URL連結放此'
        ]
    )
)
