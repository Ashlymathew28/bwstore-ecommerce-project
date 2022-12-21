from django.shortcuts import render

# Create your views here.
def home(request):
     return render(request,"user_homepage.html")

#def member_login(request):
 #    return render(request,"member-login.html")
