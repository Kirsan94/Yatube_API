from rest_framework import viewsets, permissions, mixins, filters
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404
from posts.models import Group, Post
from .serializers import (
    GroupSerializer,
    PostSerializer,
    CommentSerializer,
    FollowSerializer
)
from .permissions import IsOwnerOrReadOnly


class CreateRetrieveViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    pass


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny, ]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly, ]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly, ]

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        new_queryset = post.comments.all()
        return new_queryset


class FollowViewSet(CreateRetrieveViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        new_queryset = user.followers.all()
        return new_queryset
