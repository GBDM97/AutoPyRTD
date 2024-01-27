from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ConsoleRTD import process
import json

@csrf_exempt
def post_req_view(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        process.optData(data['options'])  # Assuming 'options' is the key in your JSON

        response_data = {'message': 'Success'}
        status_code = 200

    except json.JSONDecodeError:
        response_data = {'error': 'Invalid JSON format'}
        status_code = 400

    except KeyError:
        response_data = {'error': 'Missing key in JSON'}
        status_code = 400

    response = JsonResponse(response_data, status=status_code)

    # Include Access-Control-Allow-Origin header if the status code is 200
    if status_code == 200:
        response["Access-Control-Allow-Origin"] = "*"

    return response