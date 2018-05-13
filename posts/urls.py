from django.conf.urls import url
from .import views
# from posts.views import HomeView
from django.urls import path

app_name = 'posts'
urlpatterns = [
    path('', views.AllPosts.as_view(), name="all"),
    path('<int:pk>/', views.PostDetailView.as_view(), name="detail"),
    

]