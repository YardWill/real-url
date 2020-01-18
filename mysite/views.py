from django.http import HttpResponse
from . import douyu


def index(request):
  number = request.GET.get('no')
  url = douyu.get_real_url(number)
  print(number, url)
  return HttpResponse(url)
