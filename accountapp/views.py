from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld

has_ownership = [login_required, account_ownership_required]


@login_required(login_url=reverse_lazy("accountapp:login"))
def hello_world(request):
    if request.method == 'POST':
        temp = request.POST.get('input_text')
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse("appaccount:hello_world"))
    elif request.method == 'GET':

        new_hello_list = HelloWorld.objects.all()

        return render(request, 'accountapp/hello_world.html',
                      context={'new_hello_list': new_hello_list, 'method':'get'})



class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'


@method_decorator(has_ownership, 'get')
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    form_class = UserCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'

