from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.template import loader
from logs.models import DataForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
@login_required
def index(request):
    template = loader.get_template('index.html')
    user = request.user
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data = form.save(commit=False)
            data.data_owner = request.user
            data = data.save()
            return render(request, 'submited.html')
    else:
        form = DataForm()
    context = {
	'form':form,
    }
    return HttpResponse(template.render(context, request))

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
