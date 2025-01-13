from django.urls import path
from apps.base.views import about, index

urlpatterns = [
        path('index/', index, name='index'),
    path('about/', about, name='about'),
]