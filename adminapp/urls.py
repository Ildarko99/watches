from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    # path('', adminapp.index, name='index'),
    path('', adminapp.UsersList.as_view(), name='index'),
    path('user/create/', adminapp.user_create, name='user_create'),
    path('user/<int:pk>/update/', adminapp.user_update, name='user_update'),
    path('user/<int:pk>/delete/', adminapp.user_delete, name='user_delete'),

    path('categories/read/', adminapp.CategoriesRead.as_view(), name='categories_read'),
]
