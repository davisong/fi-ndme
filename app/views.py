from django.shortcuts import render
from django.http import HttpResponseRedirect
# import pandas as pd

from .forms import CSVFileForm

# Create your views here.


def index(request):
    template_name = 'app/index.html'
    form = CSVFileForm()
    rendered_form = form.as_div()
    context = {'form': rendered_form}
    return render(request, template_name, context)


def upload_csv(request):
    if request.method == 'POST':
        form = CSVFileForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            handle_uploaded_file(request.FILES['csv_file'])
            return HttpResponseRedirect('')
    else:
        form = CSVFileForm()
    return render(request, 'app/index.html', {'form': form})


def handle_uploaded_file(f):
    with open('name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
