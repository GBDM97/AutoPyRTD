from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from .DataGeneration.process import optData
from .DataGeneration.output import returnData
import json

dryOrLock = input('Select "DRY" or "LOCK" : ')
None if dryOrLock == 'DRY' or dryOrLock == 'LOCK' else exit()

@csrf_exempt
def post_req_view(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        optData(data['options'], dryOrLock)  # Assuming 'options' is the key in your JSON

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

def return_options_data(r):
    print(str(returnData()))
    return HttpResponse(
        f"""
        <html><body>
            <h1 style=\"color: green;\">
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            {returnData()}</h1>
        </body>
        </html>
        """
    , status=200)