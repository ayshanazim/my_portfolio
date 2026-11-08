from django.shortcuts import render

def home(request):
    data = {
        'name': 'Aysha',
        'profession': 'Python Full Stack Developer'
    }

    return render(request, 'index.html', data)