from django.http import HttpResponse

def test_message(request):
	return HttpResponse('Test django work')