from django.shortcuts import render, redirect, get_object_or_404
from .models import Client


def dashboard(request):
    return render(request, 'clients/dashboard.html')


def clients(request):
    clients = Client.objects.all()
    return render(request, "clients/clients.html", {"clients": clients})


def add_client(request):
    if request.method == "POST":
        Client.objects.create(
            nom=request.POST['nom'],
            email=request.POST['email'],
            telephone=request.POST['telephone'],
            ville=request.POST['ville']
        )
        return redirect('clients')




def delete_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)

    if request.method == "POST":
        client.delete()

    return redirect('clients')