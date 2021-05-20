from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Checkbook.urls')),
    path('', views.home, name='index'),
    path('create/', views.create_account, name='create'),
    path('/balance/', views.balance, name='balance'),
    path('transaction/', views.transaction, name='transaction')
]