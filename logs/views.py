from django.shortcuts import render

from .models import Data
from .forms import SearchForm, DataForm
from django.middleware.csrf import get_token
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

#For backup database
from django.http import HttpResponse
import csv
from django.utils.encoding import smart_str
from django.utils.timezone import now


# Create your views here.
def check_owner(request, data):
    if data.data_owner == request.user:
        return True
    else:
        return False

@login_required
def new_log(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data = form.save(commit=False)
            data.data_owner = request.user
            data = data.save()
            return render(request, 'log_submited.html')
    else:
        form = DataForm()
    context = {
    'form':form,
    }
    return render(request, 'log_new.html', context)

# View for Logs Index
@login_required
def list_logs(request):
    return render(request, 'logs_index.html')

# VIEW FOR SINGLE LOG
@login_required
def single_log(request, log_id):
    try:
        data = Data.objects.get(pk=log_id)
    except:
        return render(request, 'log_error_not_found.html')

    if check_owner(request, data):
        context = {
            'data': data,
        }
        return render(request, 'log_single.html', context)
    else:
        return render(request, 'log_error_owner.html')

# DELETE SINGLE LOG
@login_required
def delete(request, log_id):
    if request.method == 'POST':
        password = request.POST["userPassword"]

        try:
            data = Data.objects.get(pk=log_id)
        except:
            return render(request, 'log_error_not_found.html')

        if request.user.check_password(password):
            if check_owner(request, data):
                Data.objects.filter(pk=log_id).delete()
                return render(request, 'log_deleted.html')
            else:
                return render(request, 'log_error_owner.html')
        else:
            return render(request, 'profile_wrong_password.html')
    else:
        return render(request, 'log_delete_authentication.html')

@login_required
def modify(request, log_id):
    try:
        current_log = Data.objects.get(pk=log_id)
    except:
        return render(request, 'log_error_not_found.html')

    if check_owner(request, current_log):
        if request.method == 'POST':
            form = DataForm(request.POST, instance=current_log)
            if form.is_valid():
                data = form.cleaned_data
                data = form.save(commit=False)
                data.data_owner = request.user
                data = data.save()
                return render(request, 'log_modified.html')
        else:
            form = DataForm(instance=current_log)

        context = {
            'form':form,
        }

        return render(request, 'log_modify.html', context)
    else:
        return render(request, 'log_error_owner.html')

# SEARCH
@login_required
def search(request):
    data = Data.objects.filter(data_owner_id=request.user).order_by('-timestamp')
    #data_total = Data.objects.filter(data_owner_id=request.user).count()
    def countData(data):
        counter = data.count()
        return counter

    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''

    data = Data.objects.filter(data_owner_id=request.user, name__icontains=search_text).order_by('-timestamp')

    if countData(data) == 0:
        data = Data.objects.filter(data_owner_id=request.user, contact__icontains=search_text).order_by('-timestamp')
    context = {
        'data': data,
        'counter': countData(data)
    }

    return render(request, 'logs_ajax_search.html', context)

def backup(request):
    response = HttpResponse(content_type='text/csv')
    
    fileName=request.user.username + "-backup-" + str(now().strftime("%d-%m-%Y"))
    response['Content-Disposition'] = 'attachment; filename="%s.csv"' %fileName

    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))

    writer.writerow([
        smart_str(u"Date and Time"),
        smart_str(u"Name"),
        smart_str(u"Contact Phone"),
        smart_str(u"Manufacturer"),
        smart_str(u"Model"),
        smart_str(u"Price"),
        smart_str(u"Description"),
    ])

    data = Data.objects.filter(data_owner_id=request.user).order_by('-timestamp')
    
    for event in data:
        writer.writerow([
            smart_str(event.timestamp.strftime("%d/%m/%Y %H:%M")),
            smart_str(event.name),
            smart_str(event.contact),
            smart_str(event.manufacturer),
            smart_str(event.model),
            smart_str(event.price),
            smart_str(event.description),
        ])
    
    return response
