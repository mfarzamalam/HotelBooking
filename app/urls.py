from django.urls import path
from .views import Index, UserRegister, HotelDetail, add_to_cart, success, failed
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('registration/', UserRegister.as_view(), name='customerregistration'),
    
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=UserLoginForm, redirect_authenticated_user = True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),

    path('Hotel-detail/<int:pk>/', HotelDetail.as_view(), name='hotel-detail'),
    path('add-to-cart/', add_to_cart, name='add-to-cart'),
    path('success/', success, name='success'),
    path('failed/', failed, name='failed'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
