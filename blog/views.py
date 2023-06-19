from django.shortcuts import render

# Create your views here.

# craeting view for index html to render
def index(request):
  return render(request,"blog/index.html")

