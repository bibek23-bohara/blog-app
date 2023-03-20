
from django.urls import path
from blog_app import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="post-list"),
    path("post-detail/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("post-delete/<int:pk>/",
         views.PostDeleteView.as_view(),
         name="post-delete"),
    path(
    "post-update/<int:pk>/",
        views.PostUpdateView.as_view(),
        name="post-update"),
    path(
        "post-create/",
        views.post_create,
        name="post-create"
    ),
    path(
        "draft-list/",
        views.DraftListView.as_view(),
        name="draft-list",
    ),
    path("post-publish/<int:pk>/",
         views.PostPublishView.as_view(),
         name="post-publish"),
         
]
