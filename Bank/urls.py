from django.contrib import admin
from django.urls import path, include
from bank_details import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('bank_details.api.urls')),
    path('get_data/<int:page>', views.get_data, name="get_data"),
    path('get_data/',views.get_data,name='get_data1',kwargs={'page': 1}),
    path('city/', views.filter, name="city"),
    path('feed_data/',views.feed_data,name="feed_data")
]
