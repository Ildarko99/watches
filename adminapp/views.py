from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from adminapp.forms import AdminShopUserCreateForm, AdminShopUserUpdateForm, AdminProductCategoryCreateForm
from mainapp.models import ProductCategory


@user_passes_test(lambda x: x.is_superuser)
def index(request):
    users_list = get_user_model().objects.all().order_by(
        '-is_active', '-is_superuser', '-is_staff', 'username'
    )

    context = {
        'page_title': 'админка/пользователи',
        'users_list': users_list
    }

    return render(request, 'adminapp/templates/authapp/shopuser_list.html', context)


class OnlySuperUserMixin:  # добавляя этот миксин в класс можем давать доступ только супер-юзеру
    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PageTitleMixin:  # добавляя этот миксин в класс можем получать к контекст page title
    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs, object_list=None)
        data['page_title'] = self.page_title
        return data


class UsersList(OnlySuperUserMixin, PageTitleMixin, ListView):
    page_title = 'админка/пользователи'
    model = get_user_model()


@user_passes_test(lambda x: x.is_superuser)
def user_create(request):
    if request.method == 'POST':
        user_form = AdminShopUserCreateForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('my_admin:index'))
    else:
        user_form = AdminShopUserCreateForm()

    context = {
        'page_title': 'пользователи/создание',
        'user_form': user_form
    }

    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda x: x.is_superuser)
def user_update(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    if request.method == 'POST':
        user_form = AdminShopUserCreateForm(request.POST, request.FILES, instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('my_admin:index'))
    else:
        user_form = AdminShopUserUpdateForm(instance=user)

    context = {
        'page_title': 'пользователи/редактирование',
        'user_form': user_form
    }

    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda x: x.is_superuser)
def user_delete(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    # user.delete() Будет работать. Но данные удалять не принято. Их потом не восстановить.
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('my_admin:index'))

    context = {
        'page_title': 'пользователи/удаление',
        'user_to_delete': user,
    }

    return render(request, 'adminapp/user_delete.html', context)


# @user_passes_test(lambda x: x.is_superuser)
# def categories_read(request):
#
#     context = {
#         'page_title': 'админка/категории',
#         'categories_list': ProductCategory.objects.all(),
#     }
#     return render(request, 'adminapp/productcategory_list.html', context)

# FBV vs CBV

class ProductCategoriesRead(OnlySuperUserMixin, PageTitleMixin, ListView):  # выводит список категорий в админке
    model = ProductCategory
    page_title = 'Админка/Категории'


class ProductCategoryCreate(OnlySuperUserMixin, PageTitleMixin, CreateView):  # выводит список категорий в админке
    model = ProductCategory
    page_title = 'Админка/Категории/создание'
    success_url = reverse_lazy('my_admin:categories_read')

    # fields = '__all__' можно так, можно как ниже
    form_class = AdminProductCategoryCreateForm
    # template_name = 'adminapp/productcategory_list.html'
    # """Mixin for responding with a template and list of objects."""
    # template_name_suffix = '_list' Поэтому можно не писать имя шаблона, если оно называется по имени модели с суффиксом '_list'

    # context_object_name = 'categories_list'  дефолтом Джанго забрасывает под именем object_list
    #                                          поэтому в шаблоне будем исп-ть object_list


class ProductCategoryUpdate(OnlySuperUserMixin, PageTitleMixin, UpdateView):  # выводит список категорий в админке
    model = ProductCategory
    page_title = 'Админка/Категории/Редактирование'
    success_url = reverse_lazy('my_admin:categories_read')
    form_class = AdminProductCategoryCreateForm
    pk_url_kwarg = 'category_pk'


class ProductCategoryDelete(OnlySuperUserMixin, PageTitleMixin, DeleteView):  # выводит список категорий в админке
    model = ProductCategory
    page_title = 'Админка/Категории/Удаление'
    success_url = reverse_lazy('my_admin:categories_read')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
