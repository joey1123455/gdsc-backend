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
        data = response.json()
        articles = data['articles']
        j = {}
        x = 0
        for i in articles:
            source = i['source']['name']
            article_title = i['title']
            article_key= "".join(article_title.split())
            j[x] = {'source': source,
            'author': i['author'],
            'title': article_title,
            'image_url': i['urlToImage'],
            'post_url': i['url'],
            'description': i['description']}
            x += 1
            
        return JsonResponse({"article_list": j}, status=200)
    else:
        return JsonResponse({"desc": "Bad request"}, status=400)