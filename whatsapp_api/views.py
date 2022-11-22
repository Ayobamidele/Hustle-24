from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt




@csrf_exempt
def webhook(request):
	token = "Testing12345"
	if request.method == 'POST':
		print("Here i am", dir(request.POST), request.GET, "POST")
		if request.POST.get("hub.mode") == "subscribe":
			print("Got Past subscribe !!! GET")
			if request.POST.get("hub.verify_token") != "wormhole":
				return HttpResponse("Verification token missmatch")
			return HttpResponse(request.POST.get("hub.challenge"), content_type="text/plain")
		return HttpResponse("Hello world", status=200)
		# return HttpResponse(request.body, status=200)
	elif request.method == 'GET':
		print("Here i am", dir(request.POST), request.GET,"GET")
		if request.GET.get("hub.mode") == "subscribe":
			print("Got Past subscribe !!! POST")
			if request.GET.get("hub.verify_token") != "wormhole":
				return HttpResponse("Verification token missmatch")
			return HttpResponse(request.GET.get("hub.challenge"), content_type="text/plain")
		return HttpResponse("Hello world", status=200)
	