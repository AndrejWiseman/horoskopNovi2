from django.shortcuts import render

from .utils import ovan


# Create your views here.
def index(requests):

    context = {

    }
    return render(requests, 'index.html', context)


def ovanH(requests):

    dnevni = ovan()

    context = {
        'dnevni': dnevni
    }
    return render(requests, 'ovan.html', context)
