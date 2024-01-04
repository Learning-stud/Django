#APPLICATION

from django.shortcuts import render
# APPLICATION
def home(request):
 return render(request,"practice_1_app/index.html")
