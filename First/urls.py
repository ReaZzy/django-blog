from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as userViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Blog.urls')),
    path('profile/', userViews.profile, name='profile'),
    path('registration/', include('users.urls')),
    path('auth/', auth_views.LoginView.as_view(template_name='users/auth.html'), name='auth' ),
    path('exit/', auth_views.LogoutView.as_view(template_name='users/exit.html'), name='exit' ),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
