from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from account.decorators import ad_required, teacher_required
from .forms import AddUserForm
# Create your views here.
@login_required
def index(request):
    return render(request, 'pages/base.html')

@login_required
def showProfile(request, id):
    u = User.objects.get(id=id)
    return  render(request, 'pages/profile.html', {'u':u, 'id': id})

@login_required
@ad_required
def userm(request):
    u = User.objects.all()
    return render(request, 'pages/userm.html', {'u':u})

@login_required
@ad_required
def adduser(request):
    form = AddUserForm()
    if request.method == 'POST':
        form = AddUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/userm')
    return render(request, 'pages/adduser.html', {'form': form})
