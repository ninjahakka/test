#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *


#TemplateSendMessage - ConfirmTemplate(確認介面訊息)
def Confirm_Template():

    message = TemplateSendMessage(
        alt_text='你是學生還是教職員呢？',
        template=ConfirmTemplate(
            text="你是學生還是教職員呢？",
            actions=[
                PostbackTemplateAction(
                    label="學生",
                    text="我是學生啦",
                    data="會員註冊"
                ),
                MessageTemplateAction(
                    label="教職員",
                    text="我是教職員啦"
                )
            ]
        )
    )
    return message

#旋轉木馬按鈕訊息介面

def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='一則旋轉木馬按鈕訊息',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://www.nccu.edu.tw/var/file/0/1000/img/12/1651482462275s.jpg',
                    title='你的身份是？',
                    text='輸入你的身分即可獲得防疫攻略！',
                    actions=[
                        MessageTemplateAction(
                            label='我是確診者',
                            text='我是確診者'
                        ),
                        MessageTemplateAction(
                            label='我是密切接觸者',
                            text='我是密切接觸者'
                        ),
                        MessageTemplateAction(
                            label='我是自我應變者',
                            text='我是自我應變者'
                        
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://www.nccu.edu.tw/var/file/0/1000/img/12/280317299s.jpg',
                    title='你的身份是？',
                    text='輸入你的身分即可獲得防疫攻略！',
                    actions=[
                        MessageTemplateAction(
                            label='我是自主健康管理者',
                            text='我是自主健康管理者'
                        ),
                        MessageTemplateAction(
                            label='不確定定義',
                            text='不確定定義'
                        ),
                        URITemplateAction(
                            label='還不夠清楚？',
                            uri='https://www.nccu.edu.tw/var/file/0/1000/img/12/0511FINAL_NEW.pdf'
                        )
                    ]
                
                )
            ]
        )
    )
    return message


#關於LINEBOT聊天內容範例