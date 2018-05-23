from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Profile
from .forms import *
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from django.contrib.auth.signals import user_logged_in

from logs.models import Data
from django.db.models import Sum

from django.utils.timezone import now

# Create your views here.
def set_lang(sender, user, request, **kwargs):
    user_language = Profile.objects.get(user_id=request.user).language
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language

user_logged_in.connect(set_lang)

@login_required
def index(request):
    # CALCULATE TOTAL EARNING
    total_price = Data.objects.filter(data_owner_id=request.user).aggregate(Sum('price'))
    
    # CALCULATE TOTAL DATA
    total_data = Data.objects.filter(data_owner_id=request.user).count()
    
    # TO DO
    next_pay = 0
    
    # CALCULATE DAYS REGISTERED
    days_registered = (now() - request.user.date_joined)
    
    context = {
        'total_price': total_price['price__sum'],
        'next_pay' : next_pay,
        'days_registered': days_registered.days,
        'date_joined': request.user.date_joined,
        'total_data': total_data,
    }
    
    return render(request, 'index.html', context)

def about_us(request):
    return render(request, 'about_us.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home:account_update')
    else:
        form = UserCreationForm()
    return render(request, 'profile_signup.html', {'form': form})

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
            return redirect('home:account_info')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    
    return render(request, 'profile_update.html', context)

def profile(request):
    user = request.user
    user = User.objects.get(pk=user.id)

    context = {
        'user':user,
    }
    return render(request, 'profile_info.html', context)
