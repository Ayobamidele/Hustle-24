from django.http import HttpResponse



def webhook(request):
	token = "Testing12345"
	if request.method == 'GET':
		if request.GET.get("hub.mode") == "subscribe" and request.GET.get("hub.challenge"):
			if not request.GET.get("hub.verify_token")== token:
				return HttpResponse("Verification token missmatch", status=403)
			return HttpResponse(request.GET['hub.challenge'], status=200)
		print(request.GET)
		return HttpResponse("Hello world", status=200)
		# return HttpResponse(request.body, status=200)
	elif request.method == 'POST':
		print(request.POST)
		return HttpResponse(request.body, status=200)
	