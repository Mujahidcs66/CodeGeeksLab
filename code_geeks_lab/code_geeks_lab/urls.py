from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth
from user import views as user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('geeks/', include('geeks.urls')),
    path('weather/', include('weather.urls')),
    path('', include('user.urls')),
    path('todo/', include('todo.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('polls/', include('polls.urls')),
    path('login/', user_view.Login, name="login"),
    path('logout/', auth.LogoutView.as_view(template_name='user/index.html'), name='logout'),
    path('register/', user_view.register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
