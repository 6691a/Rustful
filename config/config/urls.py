
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
      # JWT Token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('', include('blog.urls'), name='blog'),
    path('api/user/', include('users.urls')),
    path('api/', include('blog_api.urls'), name='blog_api'),
    path('api-auth', include('rest_framework.urls')),

   

  
]
