from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProfileCreationView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    # success_url = reverse_lazy("accountapp:hello_world")
    template_name = 'profileapp/create.html'

    def form_valid(self, form): # 성공했을 때 실행되는 함수
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={ 'pk' : self.object.user.pk })
@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    # success_url = reverse_lazy('accountapp:detail')
    # 클래스 변수기 때문에 클래스가 생성될 때 만들어지는 것이다. 클래스를 선언하는 시점에서 pk를 가져올 수 없는 문제가 있다.
    # 동적으로 메소드를 불러 올 수 있도록 만들어야 한다.
    # 바로 메소드 오버라이드를 이용해야 한다.
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk' : self.object.user.pk})
        #여기서 object는 위의 변수 중 context_object_name과 같다.
