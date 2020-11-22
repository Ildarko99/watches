from django.conf import settings
from django.core.mail import send_mail
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse

from authapp.forms import ShopUserAuthenticationForm, ShopUserRegisterForm, ShopUserEditForm, ShopUserProfileEditForm
from authapp.models import ShopUser

def send_verification_email(user):
    verify_link = reverse('auth:verify', args=[user.email, user.activation_key])

    subject = f'Активация пользователя {user.username}'

    message = f'Для подтверждения перейдите по ссылке:\n {settings.DOMAIN_NAME}{verify_link}'

    return send_mail(subject, message, settings.DOMAIN_NAME, [user.email], fail_silently=False) #send_mail метод из стандартного набора


def verify(request, email, activation_key):
    try:
        user = ShopUser.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return render(request, 'authapp/verification.html')
        else:
            print(f'error: activation user: {email}') #логирование
            return render(request, 'authapp/verification.html')
    except Exception as e:
        print(e.args)
        return HttpResponseRedirect(reverse('main:index'))


def login(request):
    redirect_url = request.GET.get('next', None)

    if request.method == 'POST':
        form = ShopUserAuthenticationForm(data=request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                redirect_url = request.POST.get('redirect_url', None)

                auth.login(request, user)
                if redirect_url:

                    return HttpResponseRedirect(redirect_url)
                return HttpResponseRedirect(reverse('main:index'))
    else:

        form = ShopUserAuthenticationForm()
    from_register = request.session.get('register', None)
    if from_register:
        del request.session['register']
    context = {
        'page_title': 'аутентификация',
        'form': form,
        'redirect_url': redirect_url,
        'from_register': from_register,
    }
    return render(request, 'authapp/login.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))

def user_register(request):
    title = 'регистрация'
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            user = register_form.save()
            if send_verification_email(user):
                request.session['register'] = True
                print('succes')
                return HttpResponseRedirect(reverse('authapp:login'))
    else:
        print('error')
        register_form = ShopUserRegisterForm()
    context = {
        'page_title': 'регистрация',
        'form': register_form,
    }
    return render(request, 'authapp/register.html', context)

@transaction.atomic() #в случае, если операция не завершилась успешно, делает откат в БД
def user_profile(request):

    if request.method == 'POST':
        user = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        profile_form = ShopUserProfileEditForm(request.POST, instance=request.user.shopuserprofile)
        if user.is_valid() and profile_form.is_valid():
            # with transaction.atomic(): пример исп-я декоратора внутри ф-ции
                        # smth_to.save() для примера исп-я декоратора внутри ф-ции
                        # user.save()
                        #etc
            user.save()
            return HttpResponseRedirect(reverse('main:index'))
    else:
        user = ShopUserEditForm(instance=request.user) #если в Джанго не передавать instance, то он будет пытаться создавать новый объект
        profile_form = ShopUserProfileEditForm(instance=request.user.shopuserprofile)

    context = {
        'page_title': 'профиль',
        'form': user,
        'profile_form': profile_form
    }
    return render(request, 'authapp/profile.html', context)