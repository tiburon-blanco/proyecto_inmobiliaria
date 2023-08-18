from django.http import HttpResponse

def saludo (request):
    
    return HttpResponse("Hola")


def despedida (request):
    
    return HttpResponse("adios")