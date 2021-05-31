# News Reading sunao by Elderny
import json
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)
if __name__ == '__main__':
    import requests
    import json
    print("Welcome to automatic news reader")
    url = input("Please Type you newsapi url: ")
    news = requests.get(url)
    text = news.text
    speak_json = json.loads(text)
    no = 0
    for i in range(0,1):
        no += 1
        print("Reading Line no:-", no)
        speak(speak_json['articles'][i]['title'])
    else:
        print("Reading Done :)")