from .models import *
from django.forms import ModelForm, TextInput, Textarea

class MobileForm(ModelForm):
    class Meta:
        model = Mobile 
        fields = ['name', 'price', 'cam_des', 'RAM_des', 'image']
        widgets = {
            'name':TextInput(attrs={'class':'input','placeholder':'Enter the mobile name'}),
            'price':TextInput(attrs={'class':'input', 'placeholder':'Enter the mobile price'}),
            'cam_des':Textarea(attrs={'class':'input', 'placeholder':'Enter the camera description'}),
            'RAM_des':Textarea(attrs={'class':'input', 'placeholder':'Enter the RAM description'}),
            }
        labels = {
            'name':"Device Name",
            'price':"Price",
            'cam_des':"Camers Info",
            'RAM_des':"RAM info",
            'image':'Image'
            }
        