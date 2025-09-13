from django.shortcuts import render
# from django.http import HttpResponse


def index(request):
    question_list = [
        "なまこ",
        "なめこ",
        "なるこ",
    ]
    context = {
        "question_list": question_list,
        "is_polled": True,
        "polled_msg": "貝柱",
        "not_polled_msg": "だれえ？",
    } 
    return render(request, "main/index.html",context)