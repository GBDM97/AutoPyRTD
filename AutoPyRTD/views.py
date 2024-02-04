from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from .DataGeneration.process import optData
from .DataGeneration.output import returnData
import json
import time

@csrf_exempt
def post_req_view(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        optData(data['options'])
        response_data = {'message': 'Success'}
        status_code = 200
    except json.JSONDecodeError:
        response_data = {'error': 'Invalid JSON format'}
        status_code = 400
    except KeyError:
        response_data = {'error': 'Missing key in JSON'}
        status_code = 400
    response = JsonResponse(response_data, status=status_code)
    if status_code == 200:
        response["Access-Control-Allow-Origin"] = "*"
    return response

def return_options_data(r):
    return JsonResponse({'excerpt':returnData()}, status=200)