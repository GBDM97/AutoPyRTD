from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def post_req_process(request):
    print(request.body.decode('utf-8'))
    res = JsonResponse({},status=200)
    res['Access-Control-Allow-Origin'] = '*'
    return res