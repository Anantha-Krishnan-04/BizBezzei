from django.urls import path
# from . import views
from . views import HomeView, ArticleDetailView, AddPostView, AddCategoryView, UpdatePostView, DeletePostView, CategoryView, LikeView, AddCommentView, CategoryListView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete'),
    path('category/<str:cate>/', CategoryView, name='category'),
    path('likes/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('category-list/', CategoryListView, name='category-list'),
]


