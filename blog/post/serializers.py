from rest_framework import serializers
from .models import Comment, Post

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'owner', 'content']


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(source='comment_set', many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'owner', 'comments']