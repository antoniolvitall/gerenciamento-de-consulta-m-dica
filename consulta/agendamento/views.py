from django.http import JsonResponse


def profissionais(request):
    if request.method == 'GET':
        profissionais = {}
