from django.http import JsonResponse
from django.template import loader
import json
from Bot import ChatBot as bot
from time import gmtime, strftime


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
        })
    else:
        return JsonResponse({"desc": "Bad request"}, status=400)


def api_index(request):
    json_data = json.loads(request.body)
    print(json_data)