from django.urls import path
from .views import PostView, CommentView

urlpatterns = [
    path("", PostView.as_view(), name="post"),
    path("<int:post_id>/", PostView.as_view(), name="postDetail"),
    path("comment/", CommentView.as_view(), name="comment"),
    path("<int:post_id>/comment/", CommentView.as_view(), name="postComment")
]


