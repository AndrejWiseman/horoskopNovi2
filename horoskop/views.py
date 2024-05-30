from django.shortcuts import render
from .utils import dnevni_horoskop, nedeljni_horoskop, mesecni_horoskop, godisnji_horoskop


# Create your views here.
def index(requests):

    context = {

    }
    return render(requests, 'index.html', context)


def horoskop_view(request, znak):
    if znak == 'ovan':
        dnevni = dnevni_horoskop(znak)
        nedeljni = nedeljni_horoskop(znak)
        mesecni = mesecni_horoskop(znak)
        godisnji = godisnji_horoskop(znak)
    elif znak == 'bik':
        dnevni = dnevni_horoskop(znak)
        nedeljni = nedeljni_horoskop(znak)
        mesecni = mesecni_horoskop(znak)
        godisnji = godisnji_horoskop(znak)
    elif znak == 'blizanci':
        dnevni = dnevni_horoskop(znak)
        nedeljni = nedeljni_horoskop(znak)
        mesecni = mesecni_horoskop(znak)
        godisnji = godisnji_horoskop(znak)
    elif znak == 'rak':
        dnevni = dnevni_horoskop(znak)
        nedeljni = nedeljni_horoskop(znak)
        mesecni = mesecni_horoskop(znak)
        godisnji = godisnji_horoskop(znak)
    elif znak == 'lav':
        dnevni = dnevni_horoskop(znak)
        nedeljni = nedeljni_horoskop(znak)
        mesecni = mesecni_horoskop(znak)
        godisnji = godisnji_horoskop(znak)
    elif znak == 'devica':
        dnevni = dnevni_horoskop(znak)
        nedeljni = nedeljni_horoskop(znak)
        mesecni = mesecni_horoskop(znak)
        godisnji = godisnji_horoskop(znak)
    elif znak == 'vaga':
        dnevni = dnevni_horoskop(znak)
        nedeljni = nedeljni_horoskop(znak)
        mesecni = mesecni_horoskop(znak)
        godisnji = godisnji_horoskop(znak)
    elif znak == 'skorpija':
        dnevni = dnevni_horoskop(znak)
        nedeljni = nedeljni_horoskop(znak)
        mesecni = mesecni_horoskop(znak)
        godisnji = godisnji_horoskop(znak)
    elif znak == 'strelac':
        dnevni = dnevni_horoskop(znak)
        nedeljni = nedeljni_horoskop(znak)
        mesecni = mesecni_horoskop(znak)
        godisnji = godisnji_horoskop(znak)
    elif znak == 'jarac':
        dnevni = dnevni_horoskop(znak)
        nedeljni = nedeljni_horoskop(znak)
        mesecni = mesecni_horoskop(znak)
        godisnji = godisnji_horoskop(znak)
    elif znak == 'vodolija':
        dnevni = dnevni_horoskop(znak)
        nedeljni = nedeljni_horoskop(znak)
        mesecni = mesecni_horoskop(znak)
        godisnji = godisnji_horoskop(znak)
    elif znak == 'ribe':
        dnevni = dnevni_horoskop(znak)
        nedeljni = nedeljni_horoskop(znak)
        mesecni = mesecni_horoskop(znak)
        godisnji = godisnji_horoskop(znak)

    return render(request, 'ovan.html', {
        'dnevni': dnevni,
        'nedeljni': nedeljni,
        'mesecni': mesecni,
        'godisnji': godisnji,
    })
