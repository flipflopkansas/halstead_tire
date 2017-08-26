from django.shortcuts import render
from . import forms

# Create your views here.

def index(request):
    return render(request, 'contact_us/index.html')


def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = form.FormName(request.POST)

        if form.is_valid():

            print("VALIDATION SUCCESS!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("VEHICLE_TYPE: "+form.cleaned_data['vehicle_type'])
            print("TIRE_SIZE: "+form.cleaned_data['tire_size'])
            print("TEXT: "+form.cleaned_data['text'])

    return render(request, 'contact_us/form_page.html', {'form' :form})
