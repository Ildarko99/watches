from django.shortcuts import render

from authapp.forms import myAuthenticationForm


def login(request):
    form = myAuthenticationForm()
    context = {
        'page_title': 'аутентификация',
        'form': form
    }
    return render(request, 'authapp/login.html', context)

def logout(request):
    pass

def register(request):
    pass