from django.shortcuts import render
from .models import Lender

def lender_list_view(request):
    lender = Lender.objects.all()

    context = {
        'lender': lender
    }

    return render(request, 'lender/lender_list.html', context=context)

def lender_detail_view(request, pk=None):
    pass