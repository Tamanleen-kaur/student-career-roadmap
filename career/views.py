from django.shortcuts import render,redirect,get_object_or_404
from .models import Career,ContactMessage,RoadmapStep
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth import logout



def welcome(request):
    return render(request,'welcome.html')

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def career_details(request,id):
   career=get_object_or_404(Career,id=id)
   return render(request,"career_details.html",{"career":career})
def career_list(request):
    print("Career List View Running")
    careers=Career.objects.all()
    print(careers)
    return render(request,"career_list.html",{"careers":careers})
def contact(request):
    return render(request,'contact.html')
def dashboard(request):
    return render(request,'dashboard.html')
def login(request):
    return render(request,'login.html')
def profile(request):
    return render(request,'profile.html')
def quiz(request):
    return render(request,'quiz.html')
def register(request):
    return render(request,'register.html')
def resources(request):
    return render(request,'resources.html')
def roadmap(request):
    return render(request,'roadmap.html')
def career(request):
    careers=Career.objects.all()
    return render(request,'career_list.html',{'careers':careers})
def dashboard(request):
    return render(request,"dashboard.html")
def quiz(request):
    return render(request,"quiz.html")
def resources(request):
    return render(request,"resources.html")
def profile(request):
    return render(request,"profile.html")
def progress(request):
    return render(request,"progress.html")
def contact(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),

        )
        messages.success(request,"Your message has been sent successfully!")
        return redirect("contact")
    return render(request,"contact.html")


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match")

        elif User.objects.filter(username=username).exists():
            messages.error(request, "User already exists")

        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")

        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            messages.success(request, "Registration Successful")
            return redirect("login")

    return render(request, "register.html")
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

def logout_view(request):
    logout(request)
    return redirect("welcome")


def roadmap(request, career_id):
    career = get_object_or_404(Career, id=career_id)

    roadmap_steps = RoadmapStep.objects.filter(
        career=career
    ).order_by("step_number")

    return render(request, "roadmap.html", {
        "career": career,
        "roadmap_steps": roadmap_steps,
    })


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user_obj = User.objects.get(email=email)

            user = authenticate(
                request,
                username=user_obj.username,
                password=password
            )

            if user is not None:
                login(request, user)
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid password")

        except User.DoesNotExist:
            messages.error(request, "Email not registered")

    return render(request, "login.html")