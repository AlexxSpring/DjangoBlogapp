from django.contrib import admin
from django.urls import path, include
from app.views import home_page, login_page, signup_page, create_post_page, detail_page, logout_page, edit_post_page, delete_post_page
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('login/', login_page, name='login'),
    path('signup/', signup_page, name='signup'),
    path('create/', create_post_page, name='create_post'),
    path('post/<int:id>/', detail_page, name='detail'),
    path('logout/', logout_page, name='logout'),
    path('edit/<int:id>/', edit_post_page, name='edit'),
    path('delete/<int:id>/', delete_post_page, name='delete'),

    # Blog API
    path('api/', include('app.urls')),

    # JWT Login
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


