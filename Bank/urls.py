from django.contrib import admin
from django.urls import path, include
from bank_details import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('bank_details.api.urls')),
    path('home/', views.bankdetails, name="details"),
]
