import random
from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'password_generator/home.html', )

def password(request):

    randompassword = ''

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*?'))

    if request.GET.get('number'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length', 12))

    for x in range(length):
        randompassword += random.choice(characters)

    return render(request, 'password_generator/password.html', {'password' : randompassword})

def about(request):
    return render(request, 'password_generator/about.html')