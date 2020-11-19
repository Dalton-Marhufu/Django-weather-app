from django.forms import ModelForm, TextInput
from .models import CityCharts

#Creating form from model
class CityCharts(ModelForm):
    class Meta:
        model = CityCharts
        fields = ['name']
        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'})}
