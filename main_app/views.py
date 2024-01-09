from django.shortcuts import render

# Create your views here.
motorcycles = [
  {'name': 'Kawasaki', 'breed': 'Z650RS', 'description': 'fun middle-weight commuter', 'age': 2023},
  {'name': 'Honda', 'breed': 'CR125R', 'description': 'screaming motox champ', 'age': 1985},
]

def home(request) :
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def motorcycle_index(request):
    return render(request, 'motorcycle/index.html', {
        'motorcycles': motorcycles
    })