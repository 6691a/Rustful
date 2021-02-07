from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

# app_name = 'blog_api'

# router = DefaultRouter()
# router.register('', PostList, basename='post')
# urlpatterns = router.urls

urlpatterns = [

    path('', PostList.as_view(), name='list_api'),
    # path('all/', PostListAll.as_view(), name='list_all'),
    # path('<int:pk>/', PostDetail.as_view(), name='detail_api'),
]
