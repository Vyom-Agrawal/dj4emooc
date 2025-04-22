from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. 019e6dba is the polls index.")