from django.urls import path
from .views import ProfileListView,ProfileDetailView,ProfileUpdateView,ProfileFollowView

urlpatterns = [
    path("profilelist/",ProfileListView.as_view(),name="profile_list"),
    path("profile/update/<str:pk>",ProfileUpdateView.as_view(),name="profile_update"),
    path("profile/<str:pk>",ProfileDetailView.as_view(),name="profile_detail"),
    path("profile/followship/<str:pk>",ProfileFollowView,name="profile_follow")
]
