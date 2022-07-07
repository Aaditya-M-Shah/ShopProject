from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import *
from .forms import MobileForm
from django.urls import reverse_lazy

class MobileList(ListView):    
    template_name = 'mobile/home.html'
    model = Mobile
    context_object_name = 'mobiles'
    
class MobileDetail(DetailView):
    model = Mobile
    
class AddMobile(CreateView):
    model = Mobile 
    template_name = 'mobile/add_mobile.html'
    #fields = ['name', 'price', 'cam_des', 'RAM_des']
    form_class= MobileForm
    
class DeleteMobile(DeleteView):
    model = Mobile
    template_name = 'mobile/mobile_delete.html'
    success_url = reverse_lazy('home')
    
class EditMobile(UpdateView):
    model = Mobile
    form_class = MobileForm
    template_name = 'mobile/mobile_edit.html'
    
def search(request):
    query=request.POST['query']
    device_list=Mobile.objects.all()
    relevent_devices=[]
    for device in device_list:
        if query in device.name:
            relevent_devices.append(device)
    
    mobiles={'mobiles':relevent_devices}
            
    return render(request, 'mobile/home.html', mobiles)
    
    