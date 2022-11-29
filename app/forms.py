from django import forms


class CSVFileForm(forms.Form):
    template_name = 'app/index.html'
    csv_file = forms.FileField(
        label='Upload File', allow_empty_file=False, max_length=100)
