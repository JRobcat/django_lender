from django.shortcuts import render, get_object_or_404
from .models import Lender


def lender_list_view(request):
    lender = Lender.objects.all()

    context = {
        'lender': lender
    }

    return render(request, 'lender/lender_list.html', context=context)


def lender_detail_view(request, pk=None):
    lender = get_object_or_404(Lender, id=pk)

    context = {
        'lender': lender
    }
    return render(request, 'lender/lender_detail.html', context=context)
