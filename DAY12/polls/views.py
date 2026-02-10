# from django.shortcuts import render
# from django.http import HttpResponse
# def index(request):
#     return HttpResponse("Hello world !! you have done it")
# # Create your views here.

from django.http import HttpResponse
from django.shortcuts import render 
from django.template import loader
from .models import users


def index(request):
    myusers = users.objects.all().values()
    template = loader.get_template('user_list.html')
    context = {
        'myusers' : myusers,
    }
    return HttpResponse(template.render(context, request))


from django.shortcuts import render
from .forms import InputForm
def home_view(request):
    context = {}
    context['form'] = InputForm()
    return render(request, "home.html", context)





# from django.shortcuts import render
# def form_view(request):
#     if request.method == "POST":
#         print(request.POST) #prints the POSTed data as a QueryDict
#         name = request.POST.get('your_name')
#     return render(request, "form.html")


# from django.shortcuts import render
# def form_view(request):
#     if request.method == "POST":
#         print(request.POST)
#         email = request.POST.get('your_email')
#     return render(request, "form.html")


from django.shortcuts import render
from polls.models import FormModel
def form_view(request):
    if request.method == "POST":
       # print(request.POST) #prints the POSTed data as a QueryDict
        title = request.POST.get('title')
        Description = request.POST.get('Description')
        X = FormModel(title=title,Description=Description)
        X.save()
    return render(request, "form.html")

from django.template import loader
from django.contrib import messages
from django.shortcuts import redirect, render
from polls.models import LoginUser,SignupUser
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = None
        try:
            user = SignupUser.objects.get(username=username, is_active=True)
        except SignupUser.DoesNotExist:
            try:
                user = LoginUser.objects.get(username=username, is_active=True)
            except LoginUser.DoesNotExist:
                user = None
        else:
            if user and user.check_password(password):
                messages.success(request, f"Welcome, {username}!")
                return redirect("home")
            messages.error(request, "Invalid username or password")
    return render(request, "login.html")


from django.template import loader
from django.shortcuts import render,redirect
from django.contrib import messages
from polls.models import SignupUser
def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not username or not email or not password:
            messages.error(request, "All fields are required.")
        elif SignupUser.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
        elif SignupUser.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
        else:
            new_user = SignupUser(username=username, email=email)
            new_user.set_password(password)
            new_user.save()
            messages.success(request, "Signup successful. You can log in now.")
            return redirect("login")
    return render(request, "signup.html")





