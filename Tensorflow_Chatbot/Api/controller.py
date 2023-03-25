from django.http import JsonResponse
from django.template import loader
import json
from Bot import ChatBot as bot
from time import gmtime, strftime
import requests


def index(request):
    if request.method == 'POST':
        print('hello')
        try:
            jsonData = json.loads(request.body)
            # print(json_data)
        except:
            jsonData = json.loads(request.body.decode('utf-8'))
        print(request.body)
        print(jsonData)
        msg = jsonData["msg"]
        res = bot.ChatBot.getBot().response(msg)
        time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        print(res)
        return JsonResponse({
            "desc": "Success",
            "ques": msg,
            "res": res,
            "time": time
        }, status=200)
    else:
        return JsonResponse({"desc": "Bad request"}, status=400)

def news(request):
    if request.method == 'GET':
        url = f"https://newsapi.org/v2/everything?q=depression&apiKey=85f9b07a8b1d4fc4b1005b6adc77a9bb"
        response = requests.get(url)
        print(response)
        data = response.json()
        print(data)
        article = data['articles']
        j = {}
        k = {}
        for i in article:
            j['source'] = i['source']['name']
            j['author'] = i['author']
            j['title'] = i['title']
            j['image_url'] = i['urlToImage']
            j['post_url'] = i['url']
            j['description'] = i['description']

            k[i['title']] = j
        print(k)
        return JsonResponse({"articles": k}, status=200)
    else:
        return JsonResponse({"desc": "Bad request"}, status=400)