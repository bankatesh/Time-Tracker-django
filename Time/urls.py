
from django.contrib import admin
from django.urls import path,include
from accounts.views import home
from accounts import urls
from Tracker.views import add, dash

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('accounts/', include('accounts.urls')),
    path('dash/', dash, name="dash"),
    path('add/', add, name="add")
]
