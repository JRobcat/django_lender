from django.contrib import admin
from .views import lender_list_view
from django.urls import path, include

urlpatterns = [
    path('', lender_list_view, name='lender_list'),

]