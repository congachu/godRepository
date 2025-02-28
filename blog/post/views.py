from rest_framework import generics, mixins
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment


class PostView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = PostSerializer
    
    def get_queryset(self):
        return Post.objects.all()

    def post(self, request, *arg, **kwargs):
        return self.create(request, *arg, **kwargs)

    def get(self, request, *arg, **kwargs):
        if "post_id" in kwargs:
            return self.retrieve(self, request, *arg, **kwargs)
        return self.list(self, request, *arg, **kwargs)

class CommentView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        if "post_id" in self.kwargs:
            post_id = self.kwargs["post_id"]
            return Comment.objects.filter(post=post_id)
        return Comment.objects.all()