from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.template import loader
from logs.models import DataForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .forms import *
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from .models import Profile
from django.contrib.auth.signals import user_logged_in


# Create your views here.
def set_lang(sender, user, request, **kwargs):
    user_language = Profile.objects.get(user_id=request.user).language
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language

user_logged_in.connect(set_lang)

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
            return redirect('account:update_profile')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            user_language = profile_form['language'].value()
            translation.activate(user_language)
            request.session[translation.LANGUAGE_SESSION_KEY] = user_language
            
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('account:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    
    return render(request, 'update_profile.html', context)

def profile(request):
    user = request.user
    user = User.objects.get(pk=user.id)

    context = {
        'user':user,
    }
    return render(request, 'profile_info.html', context)
