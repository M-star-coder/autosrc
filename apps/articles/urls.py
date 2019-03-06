from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'articles'

urlpatterns = [
    path(r'', views.IndexView.as_view(), name="index"),
    path(r'article/<int:article_id>.html', views.ArticleDetailView.as_view(), name="article_detail"),

    path(r'^author/<int:author_id>.html', views.author_detail, name="author_detail"),

    url(r'^comment$', views.article_comment, name="article_comment"),
    url(r'^type/(?P<type>.*)$', views.article_type, name="article_type"),
    url(r'^category/(?P<category_id>[0-9]+)$', views.article_category, name="article_category"),  # 书分类
    url(r'^add/$', views.article_add, name="article_add"),
    url(r'^support$', views.article_support, name="article_support"),
    url(r'^collect$', views.article_collect, name="article_collect"),

    path(r'edit/<int:article_id>.html', views.article_edit, name="article_edit"),
    url(r'^search$', views.article_search, name="article_search"),
    url(r'^about$', views.about, name="about"),
    url(r'^google7c5c39bd4748d567.html$', views.google_search, name="google_search"),
    url(r'^baidu_verify_Z85YzIi6cp.html$', views.baidu_search, name="baidu_search"),

]