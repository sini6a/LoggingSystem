from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from .models import Data
from .forms import SearchForm, DataForm
from django.middleware.csrf import get_token
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def new_log(request):
    user = request.user
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
def single_log(request, log_id):
    data = Data.objects.get(pk=log_id)

    context = {
        'data': data,
    }

    return render(request, 'log_single.html', context)
    
# DELETE SINGLE LOG
def delete(request, log_id):
    Data.objects.filter(pk=log_id).delete()
    return render(request, 'log_deleted.html')

# SEARCH
def search(request):
    data = Data.objects.filter(data_owner_id=request.user).order_by('-timestamp')

    def countData(data):
        counter = data.count()
        return counter

    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''
        
    data = Data.objects.filter(data_owner_id=request.user, name__icontains=search_text).order_by('-timestamp')

    context = {
        'data': data,
        'counter': countData(data)
    }

    return render(request, 'logs_ajax_search.html', context)
