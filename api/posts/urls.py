from django.urls import path

from api.posts.views import PostList, PostDetails, MyPostsListView, MyLikesListView

urlpatterns = [
    path('list', PostList.as_view(), name='api-post lists'),
    path('details/<slug:slug>/', PostDetails.as_view(), name='api-details'),
    path('myposts', MyPostsListView.as_view(), name='api-myposts'),
    path('mylikes', MyLikesListView.as_view(), name='api-mylikes')

]
