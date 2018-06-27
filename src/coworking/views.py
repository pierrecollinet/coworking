from django.shortcuts import render

def welcome(request):
  c = {}
  return render(request, 'welcome.html', c)

