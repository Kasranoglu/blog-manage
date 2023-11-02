from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from api.posts.serializer import PostSerializer
from core.paginations import PostListPagination
from core.models import Post


# Create your views here.
class PostList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetails(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class MyPostsListView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Login olan kullanıcının yazdığı postları çekmek için queryset'i filtreleme
        return Post.objects.filter(author=self.request.user)


class MyLikesListView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PostListPagination

    def get_queryset(self):
        # Login olan kullanıcının yazdığı postları çekmek için queryset'i filtreleme
        return Post.objects.filter(like__user=self.request.user)
