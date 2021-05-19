# latest news reader
import os
# WE made a function named speak which will be used directly
def speak(str):
    # we r now importing the data
    from win32com.client import Dispatch
    # we r now importing the audio we want to listen
    speak = Dispatch("SAPI.spVoice")
    # this will made the str to speak
    speak.Speak(str)


if __name__ == '__main__':
    # request modules are used to request data from the internet
    import requests
    # json module is used to convert the internet data into something useful to use in the code
    import json

    speak("Hello there amigo ")
    speak("Hope you are doing good ")
    speak("and todays news headlines are")
    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=dc9955d735b24e2fb1353e536980feda"

    # here we are taking the url and extracting data from there
    news = requests.get(url)

    # note...we also have to get the data in the format of text hence last mein .text
    news = news.text

    # still now if i want to read text not possible cauz extraction wont be possible yet so...
    # i have to convert it into python format using json.loads
    # here extracting data means if you check on the website it gives status, headlines...
    # and articles which carry different data...we want the article part only for news
    # hence we use load to extract that particular data cauz it is string and we can not
    # access it without the loads by simply calling
    news_json = json.loads(news)

    # this will print everything in the articles.
    # print(news_json["articles"])

    # we made arts becauz we dont want everything in the articles we just want the title headlines
    # so for just title we r going to run a loop in the articles LIST after this
    arts = news_json['articles']
    for article in arts:
        print(article['title'])
        speak(article['title'])
        speak("next we have")

    print("\\t\t\t\t\t*******Thank you*******")
    speak("Thank you")
