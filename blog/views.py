from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Vehiculo, Categoria, Favorito


def inicio(request):
    return render(request, "inicio.html")


def lista_vehiculos(request):

    busqueda = request.GET.get("q")

    vehiculos = Vehiculo.objects.all()

    if busqueda:
        vehiculos = vehiculos.filter(
            titulo__icontains=busqueda
        ) | vehiculos.filter(
            marca__icontains=busqueda
        ) | vehiculos.filter(
            tipo__icontains=busqueda
        )

    return render(request, "vehiculos/lista_vehiculos.html", {
        "vehiculos": vehiculos,
        "busqueda": busqueda
    })

def vehiculos_por_categoria(request, slug):

    categoria = Categoria.objects.get(slug=slug)

    busqueda = request.GET.get("q")

    vehiculos = Vehiculo.objects.filter(categoria=categoria)

    if busqueda:
        vehiculos = vehiculos.filter(
            titulo__icontains=busqueda
        ) | vehiculos.filter(
            marca__icontains=busqueda
        ) | vehiculos.filter(
            tipo__icontains=busqueda
        )

    return render(request, "vehiculos/lista_vehiculos.html", {
        "vehiculos": vehiculos,
        "busqueda": busqueda,
        "categoria_actual": categoria
    })


def detalle_vehiculo(request, vehiculo_id):

    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    fotos = list(vehiculo.fotos.all())

    if fotos:
        imagen_principal = fotos[0].imagen.url
    elif vehiculo.imagen:
        imagen_principal = vehiculo.imagen.url
    else:
        imagen_principal = ""

    es_favorito = False

    if request.user.is_authenticated:
        es_favorito = Favorito.objects.filter(
            usuario=request.user,
            vehiculo=vehiculo
        ).exists()

    return render(request, "vehiculos/detalle_vehiculo.html", {
        "vehiculo": vehiculo,
        "fotos": fotos,
        "imagen_principal": imagen_principal,
        "cantidad_fotos": len(fotos),
        "es_favorito": es_favorito
    })

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Favorito


@login_required
def agregar_favorito(request, vehiculo_id):

    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)

    Favorito.objects.get_or_create(
        usuario=request.user,
        vehiculo=vehiculo
    )

    return redirect('detalle_vehiculo', vehiculo_id=vehiculo.id)

@login_required
def quitar_favorito(request, vehiculo_id):

    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)

    Favorito.objects.filter(
        usuario=request.user,
        vehiculo=vehiculo
    ).delete()

    return redirect('detalle_vehiculo', vehiculo_id=vehiculo.id)

@login_required
def mis_favoritos(request):

    favoritos = Favorito.objects.filter(usuario=request.user)

    return render(request, "vehiculos/favoritos.html", {
        "favoritos": favoritos
    })