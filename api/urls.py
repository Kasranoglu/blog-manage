from django.urls import path, include

urlpatterns = [
    path('post/', include('api.posts.urls')),
    path('auth/', include('api.auth.urls'))
]
