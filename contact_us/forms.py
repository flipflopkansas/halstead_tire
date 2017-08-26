from django import forms

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    vehicle_type = forms.CharField()
    tire_size = forms.CharField()
    phone_number = forms.IntegerField()
    text = forms.CharField(widget=forms.Textarea)
