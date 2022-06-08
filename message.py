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

def Carousel_Template_1():
    message = TemplateSendMessage(
        alt_text='線上看診',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://static.iyp.tw/27056/products/photooriginal-1637002-YWd2r.jpg?57390',
                    title='世誠耳鼻喉科診所',
                    text='臺北市文山區忠順街1段107號1樓',
                    actions=[
                        MessageTemplateAction(
                            label='世誠診所線上預約看診流程',
                            text='世誠診所線上預約看診流程'
                        ),
                        MessageTemplateAction(
                            label='世誠診所電話號碼',
                            text='世誠診所電話號碼'
                        ),
                        URITemplateAction(
                            label='世誠診所官方帳號',
                            uri='https://lin.ee/NbxAK3L'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://scontent.ftpe8-4.fna.fbcdn.net/v/t1.6435-9/78277530_143442760401038_8007473048829558784_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=iCIYz5lOdqkAX94ZGC3&tn=pRW8_k2nrQQ3jI7P&_nc_ht=scontent.ftpe8-4.fna&oh=00_AT9FySGmomqBaC-onUEwO9-RfoEllVMQBtWNqiheYPt5hA&oe=62C2FF47',
                    title='洪佑承小兒科專科診所',
                    text='臺北市文山區興隆路4段64之2號',
                    actions=[
                        MessageTemplateAction(
                            label='洪佑承診所線上預約看診流程',
                            text='洪佑承診所線上預約看診流程'
                        ),
                        MessageTemplateAction(
                            label='洪佑承診所電話號碼',
                            text='洪佑承診所電話號碼'
                        ),
                        URITemplateAction(
                            label='洪佑承診所官方帳號',
                            uri='https://lin.ee/sfyBi98'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://lh5.googleusercontent.com/-fG_0hYFwwvk/VyTA3crkKgI/AAAAAAAAA50/B_IrZymW8A4b_Tu0_BI-P_c4N6bHYBybgCJkC/s1600-w400/',
                    title='定安診所',
                    text='臺北市文山區景興路165號',
                    actions=[
                        MessageTemplateAction(
                            label='定安診所線上預約看診流程',
                            text='定安診所線上預約看診流程'
                        ),
                        MessageTemplateAction(
                            label='定安診所電話號碼',
                            text='定安診所電話號碼'
                        ),
                        URITemplateAction(
                            label='定安診所官方帳號',
                            uri='https://page.line.me/wxv0899w?openQrModal=true'
                        )
                    ]
                )
            ]
        )
    )
    return message

def Carousel_Template_2():
    message = TemplateSendMessage(
        alt_text='症狀舒緩',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://img.onl/n0XYqZ',
                    title='你的症狀',
                    text='請點選你的症狀',
                    actions=[
                        MessageTemplateAction(
                            label='喉嚨沙啞',
                            text='喉嚨沙啞'
                        ),
                        MessageTemplateAction(
                            label='極度疲勞',
                            text='極度疲勞'
                        )
                    ]
                )
                CarouselColumn(
                    thumbnail_image_url='https://img.onl/n0XYqZ',
                    title='你的症狀',
                    text='請點選你的症狀',
                    actions=[
                        MessageTemplateAction(
                            label='肌肉痠痛',
                            text='肌肉痠痛'
                        ),
                        MessageTemplateAction(
                            label='發燒頭痛',
                            text='發燒頭痛'
                        )
                    ]
                )
            ]
        )
    )
    return message

#關於LINEBOT聊天內容範例
