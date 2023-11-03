from django.urls import path
from .views import CreatePostView,DeletePostView,ListPostView,LikePostView,CreateCommentView
urlpatterns = [
    # path("myfeed/",FollowingListPostView.as_view(),name ="list_post"),
    path("allfeed/",ListPostView.as_view(),name ="list_post"),
    path("create/",CreatePostView.as_view(),name ="create_post"),
    path("delete/<str:pk>/",DeletePostView.as_view(),name ="delete_post"),
    path("like/<str:pk>/",LikePostView,name="like_post"),
    path("comment/<str:pk>/",CreateCommentView.as_view(),name="create_comment")
]