from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    path('sign_up/', views.sign_up, name= 'sign_up'),
    path('post/<int:pk>/', views.post_detail, name = 'post_detail'),
    path('post/new/', views.post_new, name = 'post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    #La siguiente línea es parte del tutorial de MDN para logins
    path('accounts/', include('django.contrib.auth.urls')),
]
