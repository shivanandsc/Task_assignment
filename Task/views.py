from django.shortcuts import  render, redirect
from .forms import TaskForm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from django.contrib.auth.models import User
from django.core.mail import send_mail

  
def add_task(request):  
    task = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        form.save()
      
        send_mail(request.POST['task_name'], request.POST['task_description'], 'useremailid@gmail.com', [ User.objects.get(id=request.POST['assign_to']).email], fail_silently=False)
        return redirect("homepage")

        
    return render(request,"addtask.html",{'form':task}) 

  


