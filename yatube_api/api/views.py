from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from posts.models import Group, Post, Follow
from .serializers import (
    GroupSerializer,
    PostSerializer,
    CommentSerializer,
    FollowSerializer
)
from .permissions import IsOwnerOrReadOnly


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly, ]

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


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
