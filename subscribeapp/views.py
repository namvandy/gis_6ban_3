from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

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


