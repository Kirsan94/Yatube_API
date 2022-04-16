from rest_framework import serializers

from posts.models import Comment, Post, Group, Follow, User


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    group = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Group.objects.all(),
        required=False
    )

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.PrimaryKeyRelatedField(
        read_only=True,
        many=False
    )

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        many=False
    )

    class Meta:
        fields = ('user', 'following')
        read_only_fields = ('user',)
        model = Follow
