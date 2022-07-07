from django.urls import path
from .views import *


urlpatterns = [
        path('', MobileList.as_view(), name = "home"),
        path('mobile/<int:pk>', MobileDetail.as_view(), name = 'detail'),
        path('add', AddMobile.as_view(), name = 'add'),
        path('delete/<int:pk>', DeleteMobile.as_view(), name = 'delete'),
        path('edit/<int:pk>', EditMobile.as_view(), name = 'edit'),
        path('search', search, name="search"),
    ]
