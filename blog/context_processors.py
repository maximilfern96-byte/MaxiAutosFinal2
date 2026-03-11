from .models import Favorito

def favoritos_count(request):

    if request.user.is_authenticated:
        cantidad = Favorito.objects.filter(usuario=request.user).count()
    else:
        cantidad = 0

    return {
        'favoritos_count': cantidad
    }