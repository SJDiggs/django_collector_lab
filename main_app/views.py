from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Motorcycle

# motorcycles = [
#   {'name': 'Kawasaki', 'model': 'Z650RS', 'description': 'fun middle-weight commuter', 'year': 2023},
#   {'name': 'Honda', 'model': 'CR125R', 'description': 'screaming motox champ', 'year': 1985},
# ]
# HOME VIEW
def home(request) :
    return render(request, 'home.html')

# ABOUT VIEW
def about(request):
    return render(request, 'about.html')

# MOTORCYCLE INDEX
def motorcycles_index(request):
    motorcycles = Motorcycle.objects.all() # retrieve all motorcycles from the db
    return render(request, 'motorcycles/index.html', {
        'motorcycles': motorcycles
    })

# MOTORCYCLE DETAIL
def motorcycles_detail(request, motorcycle_id):
  motorcycle = Motorcycle.objects.get(id=motorcycle_id)
  return render(request, 'motorcycles/detail.html', { 'motorcycle': motorcycle })

# MOTORCYCLE CREATE
class MotorcycleCreate(CreateView):
    model = Motorcycle
    fields = '__all__'

# MOTORCYCLE UPDATE
class MotorcycleUpdate(UpdateView):
    model = Motorcycle
    fields = ['model', 'description', 'year']

# MOTORCYCLE DELETE
class MotorcycleDelete(DeleteView):
    model = Motorcycle
    success_url = '/motorcycles' #navigate back to the motorcycles index page