from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord


@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):
    # RedirectView를 상속받았으므로, 어디로 갈지 지정해 주어야 한다.
    # get_redirect_url로 지정해 줄 수 있다.

    def get(self, request, *args, **kwargs):
        # 좋아요를 하기 위해서 해야 하는 작업
        user = request.user # 유저를 받아 왔고 해당 유저로 로직을 처리하므로, login required는 필수이다.
        article = Article.objects.get(pk=kwargs['article_pk']) # kwargs에 article_pk로 받아와야 한다. 즉, url로부터 받아와야 함.

        like_record : list = LikeRecord.objects.filter(user=user, article=article)
        if like_record.exists():
            # 좋아요가 반영되지 않는 경우/ 좋아요 X -> error message 전달
            # messages module
            messages.add_message(request, messages.ERROR, '좋아요는 한 번만 가능합니다.')
            ####

            return HttpResponseRedirect(reverse('articleapp:detail', kwargs={'pk':kwargs['article_pk']}))
        else:
            LikeRecord(user=user, article=article).save()

        article.like += 1
        article.save() # 실제 db에 저장까지 해주어야 반영된다.

        # 좋아요가 반영되는 경우 / 좋아요 O -> success message
        messages.add_message(request, messages.SUCCESS, '좋아요가 반영되었습니다.')
        ####

        return super().get(self, request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk':kwargs['article_pk']})