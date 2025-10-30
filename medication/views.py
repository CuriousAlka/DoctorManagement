from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "medication/index.html")
def create(request):
    return render(request, "medication/create.html")
def edit(request):
    return render(request, "medication/edit.html")
def delete(request):
    return render(request, "medication/delete.html")
def view(request):
    return render(request, "medication/view.html")
def search(request):
    return render(request, "medication/search.html")
def add(request):
    return render(request, "medication/create.html")
