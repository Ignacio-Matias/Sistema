from django.http import JsonResponse

from apps.catalogos.models import cat_tipo


def eliminar_identificador(request):
    pk = request.POST.get('identificador_id')
    identificador = cat_tipo.objects.get(pk=pk)
    identificador.delete()
    response = {}
    return JsonResponse(response)