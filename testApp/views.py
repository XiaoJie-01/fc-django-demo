from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse, JsonResponse


def PostDemoViews(request):
    data = [1, 2, 3, 4, 5]
    return JsonResponse({
        'data': data,
        'total': len(data),
        'msg': "ok"
    }, status=200, safe=False)