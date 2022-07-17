from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from Task.models import UserTask
from django.contrib import messages

def homepage(request):
  if request.user:
    queryset = UserTask.objects.all()
    context= {'d': queryset}
    return render(request, 'home.html',context)
  return render(request, 'home.html')



def login_request(request):
  if request.method == "POST":
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        messages.info(request, f"You are now logged in as {username}.")
        return redirect("homepage")
      else:
        messages.error(request,"Invalid username or password.")
    else:
      messages.error(request,"Invalid username or password.")
  form = AuthenticationForm()
  return render(request=request, template_name="login.html", context={"login_form":form})



def register_request(request):
  if request.method == "POST":
    form = NewUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      messages.success(request, "Registration successful." )
      return redirect("login")
    messages.error(request, "Unsuccessful registration. Invalid information.")
  form = NewUserForm()
  return render (request=request, template_name="register.html", context={"register_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("homepage")