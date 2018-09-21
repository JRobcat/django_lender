from django.contrib import admin
from django.urls import path, include
from .views import lender_list_view, lender_detail_view

urlpatterns = [
    path('', lender_list_view, name='lender_list'),
    path('<int:pk>', lender_detail_view, name='lender_detail')

]
