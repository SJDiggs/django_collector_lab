from django.shortcuts import render

# Create your views here.
motorcycles = [
  {'name': 'Kawasaki', 'model': 'Z650RS', 'description': 'fun middle-weight commuter', 'year': 2023},
  {'name': 'Honda', 'model': 'CR125R', 'description': 'screaming motox champ', 'year': 1985},
]

def home(request) :
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def motorcycles_index(request):
    return render(request, 'motorcycles/index.html', {
        'motorcycles': motorcycles
    })