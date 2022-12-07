from django.shortcuts import render
from django.http import HttpResponseRedirect
from io import TextIOWrapper
from csv import DictReader
# import pandas as pd

from .forms import CSVFileForm

# Create your views here.


def index(request):
    template_name = 'app/index.html'
    form = CSVFileForm()
    rendered_form = form.as_div()
    context = {'form': rendered_form}
    return render(request, template_name, context)


# input validation:
# check if it's a CSV file
# check that the data is formatted properly
# check that the data is encoded properly
# check that the data is in the correct form

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


# may need to consider the maximum file size that a GoogleFi CSV file can be
# may need to optimize reading in from file by not storing to disk?
def handle_uploaded_file(f):
    # converts files in binary mode (django default) to a text stream
    # that CSV module can read. assumes file encoded in utf-8, need
    # newline option to parse linebreaks in quoted fields
    rows = TextIOWrapper(f, encoding="utf-8", newline="")
    for row in DictReader(rows):
        print(row)
