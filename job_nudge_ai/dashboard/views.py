from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def dashboard(request):
    context = {
        'user': request.user,
        'credits': 5 # You'll need to implement actual credit tracking
    }
    print(context)
    return render(request,'dashboard/dashboard.html', context)

@login_required 
def generate_email(request):
    if request.method == "POST":
        job_description = request.POST.get('job_description')
        # Add email generation logic here
        return HttpResponse("Email generated!")
    return HttpResponse("Invalid request method")

# Create your views here.
