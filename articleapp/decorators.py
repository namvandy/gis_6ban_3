from django.http import HttpResponseForbidden

from articleapp.models import Article
from django.contrib.auth.models import User

def article_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_article = Article.objects.get(pk=kwargs['pk'])
        if target_article.writer == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    return decorated

def article_is_private(func):
    def decorated(request, *args, **kwargs):
        target_article = Article.objects.get(pk=kwargs['pk'])
        if target_article.is_private == False:

            if (target_article.writer == request.user) or User.is_staff:
                return func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden()
        elif target_article.is_private == True:
            return func(request, *args, **kwargs)