from django.shortcuts import render
from .models import *
# Create your views here.

# ------------------------------------------------
# def home (request,msg=None):
    # e_msg = {}
    # if msg:
        # e_msg = {'e_msg':msg}
    # return render(request,'app_name/login.html',e_msg)

# def index(request):
#     return render(request,'app_name/index.html')
# ------------------------------------------------

def home (request):
    return render(request,'app_name/login.html')

def login (request):
    if request.POST:
        try:
            p_email = request.POST["email"]
            print("------------------>>>>  Email :",p_email)
            p_password = request.POST["password"]
            print("------------------>>>>  Password :",p_password)
            uid = user.objects.get(email = p_email,password = p_password)
            print("------------------>>>>  Uid :",uid)
            cid = Chairman.objects.get(userid = uid)
            print("------------------>>>>  FirstName :",cid.firstname)
            print("------------------>>>>  LastName :",cid.lasttname)
            return render(request,'app_name/index.html')
            # return index(request)
        except Exception as e:
            print("------------->>>> Exception ",e)
            msg = "Invalid Email Or Password"
            return render(request,'app_name/login.html',{'e_msg':msg})
            # return home(request,msg=msg)
    else:
        print("------------------>>>>  Page Loaded")
        return render(request,'app_name/login.html')
