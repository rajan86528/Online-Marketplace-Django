from django.urls import path
from . import views

# for images display on website
from django.conf import settings
from django.conf.urls.static import static

# for login
from django.contrib.auth import views as auth_views
from . forms import LoginForm


urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('singnup/', views.singnup, name="singnup"),
    path('login/', auth_views.LoginView.as_view(template_name = 'core/login.html', authentication_form = LoginForm), name="login"),
    path('logout/', views.Logout_view, name='logout'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
