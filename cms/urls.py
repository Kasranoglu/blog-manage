from django.urls import path
from cms import views

urlpatterns = [
    path('', views.home, name="home"),
    path('index', views.home, name="home"),
    path('signup',views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('test', views.posts, name='test'),
    path('about', views.about, name="about"),
    path('blog', views.blog, name="blog"),
    path('contact', views.contact, name="contact"),
    path('post-details/<slug:slug>/', views.post_details, name='post_details'),
    path('send_comment', views.send_comment, name="send_comment"),
    path('support', views.support, name="support_message"),
    path('like/<slug:slug>/', views.like_post, name="like"),
    path('add-post', views.add_post, name="add-post"),
    path('profile', views.profile, name="profile")
]
