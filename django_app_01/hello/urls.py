from django.urls import path
from . import views
from django.conf.urls import url
from .views import HelloView

urlpatterns = [
    url('',HelloView.as_view(),name='index'),
]