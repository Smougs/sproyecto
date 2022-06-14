from django.shortcuts import render, redirect
from .models import Prestamo

def inicio(request):
    prestamos = Prestamo.objects.all()
    print(Prestamo)
    return render(request, "index.html", {"prestamos": prestamos})

def create_task(request):
    prestamo = Prestamo(
        nombre=request.POST["nombre"],
        apellido=request.POST["apellido"],
        telefono=request.POST["telefono"],
        direccion=request.POST["direccion"],
        libro=request.POST["libro"],
    )
    prestamo.save()
    return redirect("/app_prestamo/")




