from rest_framework import generics, mixins, viewsets, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment


class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    
    def get_queryset(self):
        return Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def update(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        if post.owner != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super().update(request, pk=pk)

    def destroy(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        if post.owner != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, pk=pk)


class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        if post_id:
            return Comment.objects.filter(post=post_id)
        return Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def update(self, request, pk=None):
        comment = get_object_or_404(Comment, pk=pk)
        if comment.owner != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super().update(request, pk=pk)

    def destroy(self, request, pk=None):
        comment = get_object_or_404(Comment, pk=pk)
        if comment.owner != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, pk=pk)