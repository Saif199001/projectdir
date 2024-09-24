from django.http import HttpResponse
from django.shortcuts import render
from .models import courses, workshop, contacts
from django.core.mail import send_mail

# Create your views here.

def index(request):
    courses_data = courses.objects.all()
    workshop_data = workshop.objects.all()
    return render(request, "mainsite/index.html",{"courses":courses_data, "workshop":workshop_data})

def about(request):
    return render(request, "mainsite/about.html")

def privacy(request):
    return render(request, "mainsite/privacyandpolicy.html")

def terms(request):
    return render(request, "mainsite/termsandconditions.html")

def contact(request):    
    return render(request, "mainsite/contact.html")

def addcontact(request):
        if request.method == "POST":
            Name = request.POST.get('userName')
            Email = request.POST.get('userEmail')
            course = request.POST.get('courseName')
            phone = request.POST.get('userPhone')
            Detail = request.POST.get('userMassage')

        newcontct = contacts(studentname=Name, studentemail=Email,
                             coursename=course, mobileno=phone, massage=Detail)
        newcontct.save()

        subject = "A new contact recieve"
        massage = f"A contact for course {course} with {Name} and email {Email} and mobile no {phone}"
        send_from = "info.edcept@gmail.com"
        send_mail(subject, massage, send_from, ['info@edcept.com'], fail_silently=True)

        return render(request, "mainsite/contact.html")

