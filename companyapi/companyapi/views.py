from django.http import HttpResponse

def home_page(request):
    print("this is first message")
    return HttpResponse('this is a home page')