from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription



@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    def get(self, request, *args, **kwargs):
        user = request.user
        project = Project.objects.get(pk=kwargs['project_pk']) # 주소창에 pk를 입력하여 project object를 불러온다.

        subscription = Subscription.objects.filter(user=user, project=project)
        # 해당 user와 project의 subscription을 불러온다.

        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()
            # subscription 객체가 기존에 없다면 새로 생성하여 DB에 저장

        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk' : kwargs['project_pk']})

# 구독 정보가 필요하므로 login은 필수임.
@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 20

    def get_queryset(self): # def get_context_data는 모든 문맥데이터를 확인하는 것임.
        # article만 지정하고자 하므로 get_queryset을 이용한다.

        project_list = Subscription.objects.filter(user=self.request.user).values_list('project')
        # .values_list('project') # project 칼럼만 리스트로 반환
        # Subscription은 User와 Project의 두 정보 모두 가지고 있다.

        # field lookup : __in과 같은 문법
        print(project_list)
        for pro in project_list:
            print(pro)
        article_list = Article.objects.filter(project__in = project_list)
        print(article_list)
        # 구독 중인 article 리스트를 반환
        return article_list





