import requests
from bs4 import BeautifulSoup


def crawler():
    info = []
    r = requests.get("https://www.nccu.edu.tw/p/426-1000-54.php?Lang=zh-tw")
    # print(r.text)

    soup = BeautifulSoup(r.text, "html.parser")
    case_num = soup.select("div.mtitle a")
    # print(case_num)

    case = case_num[0].text.lstrip()  # 去掉頭尾空格
    case = case.replace('\n', '')  
    case = case.rstrip('\t')  # 去掉結尾的tab和換行
    info.append(case)
    # print(case)  # 確診數

    url = soup.select("span a")
    # print(url)
    # 未處理
    url = url[0].text+":"+url[0]["href"]
    # print(url)
    info.append(url)
    return info
# 通報系統網址


# print(crawler())
