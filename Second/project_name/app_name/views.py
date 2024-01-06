from django.shortcuts import render

# Create your views here.
def loginHtml(request):
 return render(request,'app_name/login.html')