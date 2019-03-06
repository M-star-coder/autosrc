from .models import VisitNumber, Category, ArticleUser, Book, Article
from apps.users.models import User, Profile
from django.db.models import Count


def add_variable_to_context(request):
    vm = VisitNumber.objects.first()
    cates = Category.objects.all()
    for cate in cates:
        cate.books = Book.objects.filter(category=cate)
    types = Article.type_choice

    hot_articles = ArticleUser.objects.values('article_id').annotate(num_articles=Count('article_id')).order_by('-num_articles')[:5]
    for ha in hot_articles:
        try:
            ha['title'] = Article.objects.get(id=ha['article_id']).title
        except Exception as e:
            print(e)

    # zan_articles = ArticleUser.objects.values('article_id').annotate(num_articles=Count('article_id')).order_by('-num_articles')[:5]
    # for hk in hot_books:
    #     try:
    #         hk['title'] = Book.objects.get(id=hk['book_id']).title
    #     except Exception as e:
    #         print(e)

    hot_users = Profile.objects.order_by('-point')[:10]
    for hu in hot_users:
        try:
            hu.username = User.objects.get(id=hu.user_id).username
            # hu['avatar'] = Profile.objects.get(user_id=hu['user_id']).avatar
        except Exception as e:
            print(e)

    # hot_users = BookUser.objects.values('user_id').annotate(num_comments=Count('user_id')).order_by('-num_comments')[:10]
    # for hu in hot_users:
    #     try:
    #         hu['username'] = User.objects.get(id=hu['user_id']).username
    #         hu['avatar'] = Profile.objects.get(user_id=hu['user_id']).avatar
    #     except Exception as e:
    #         print(e)

    return locals()