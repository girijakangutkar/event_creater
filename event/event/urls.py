from django.contrib import admin
from django.urls import path, include
from django.conf import settings #add this
from django.conf.urls.static import static
from eveapp.views import eventpage, EventInfo, SignUp, user_login, user_logout, about
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', EventInfo, name='EventInfo'),
    path('eventpage/', eventpage, name='eventpage'),
    path('signup/',SignUp,name='signup'),
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('about/', about.as_view(),name='about'),
]

if settings.DEBUG: #add this
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
