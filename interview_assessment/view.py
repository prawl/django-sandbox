from django.shortcuts import render

#  the method name is the view
def hello_world(request):
  return render(request, 'home.html')