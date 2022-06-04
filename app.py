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
    message = event.message.text
    if "股票 " in message:
        buttons_template_message = TemplateSendMessage(
        alt_text = "股票資訊",
        template=CarouselTemplate( 
            columns=[ 
                    CarouselColumn( 
                        thumbnail_image_url ="https://chenchenhouse.com//wp-content/uploads/2020/10/%E5%9C%96%E7%89%871-2.png",
                        title = message + " 股票資訊", 
                        text ="請點選想查詢的股票資訊", 
                        actions =[
                            MessageAction( 
                                label= message[3:] + " 個股資訊",
                                text= "個股資訊 " + message[3:]),
                            MessageAction( 
                                label= message[3:] + " 個股新聞",
                                text= "個股新聞 " + message[3:])
                        ]
                    )
                ]
            )
         )
        line_bot_api.reply_message(event.reply_token, buttons_template_message)
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))
	
    
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
