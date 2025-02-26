from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import GroupViewSet, PostViewSet, CommentViewSet, FollowViewSet


app_name = "api"

v1_router = DefaultRouter()
v1_router.register(r'groups', GroupViewSet)
v1_router.register(r'posts', PostViewSet)
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet,
                   basename='comment'
                   )
v1_router.register(r'follow', FollowViewSet,
                   basename='follow'
                   )

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
