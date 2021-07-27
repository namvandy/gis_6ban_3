from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreationView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    success_url = reverse_lazy("accountapp:hello_world")
    template_name = 'profileapp/create.html'

    def form_valid(self, form): # 성공했을 때 실행되는 함수
        form.instance.user = self.request.user
        return super().form_valid(form)
