#ライブラリのインポート
import requests
from bs4 import BeautifulSoup


def getWeather():
    #tenki.jpの目的の地域のページのURL
    url = 'https://tenki.jp/forecast/3/15/4510/12220/'
    #HTTPリクエスト
    r = requests.get(url)

    #プロキシ環境下の場合は以下を記述
    """
    proxies = {
        "http":"http://proxy.xxx.xxx.xxx:8080",
        "https":"http://proxy.xxx.xxx.xxx:8080"
    }
    r = requests.get(url, proxies=proxies)
    """

    #HTMLの解析(初期化)
    bsObj = BeautifulSoup(r.text, "html.parser")

    #今日の天気を取得
    today = bsObj.find(class_="today-weather")
    weather = today.p.string

    #気温情報のまとまり
    temp_info = today.div.find(class_="date-value-wrap")

    #気温の取得
    temp = temp_info.find_all("dd")
    temp_max = temp[0].span.string #最高気温
    temp_max_diff = temp[1].string #最高気温の前日比
    temp_min = temp[2].span.string
    temp_min_diff = temp[3].string #最低気温の前日比

    return weather + temp_max + temp_min
    
    