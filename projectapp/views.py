from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    # success_url = reverse_lazy('articleapp:list') login_required를 적용하였으므로 아래의와 같이 get_success_url 메소드를 재정의한다.
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse("projectapp:detail" , kwargs={"pk":self.object.pk})


class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

    paginate_by = 20

    def get_context_data(self, **kwargs):
        user = self.request.user
        project = self.object # target_object를 지칭한다.

        if user.is_authenticated:
            # 현재 아래의 subscription은 구독정보를 뜻함
            subscription = Subscription.objects.filter(user=user, project=project)
        else:
            subscription = None
        article_list = Article.objects.filter(project=self.object)
        return super().get_context_data(object_list=article_list, subscription=subscription, **kwargs)

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 20