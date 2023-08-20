from django.http import HttpResponseRedirect
from django.shortcuts import render

from app.propiedad.forms import PropiedadForm
from app.propiedad.models import Propiedad


def propiedad_list_view(request):
    propiedades = Propiedad.objects.all()
    return render(request, 'propiedad_list.html', {
        'propiedades': propiedades,
    })


def propiedad_create_view(request):
    if request.method == 'POST':
        form = PropiedadForm(data=request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect(reverse('propiedad-list'))

    return render(request, 'propiedad_create.html', {
        'form': PropiedadForm(),
    })


def propiedad_detail_view(request):
    return render(request, 'propiedad_detail.html')


def propiedad_update_view(request, pk):
    return render(request, 'propiedad_update.html')


def propiedad_delete_view(request, pk):
    return render(request, 'propiedad_delete.html')