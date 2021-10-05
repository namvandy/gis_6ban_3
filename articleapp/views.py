from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin

from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article
from commentapp.forms import CommentCreationForm
import requests
import re
from pysentimiento import EmotionAnalyzer
emotion_analyzer = EmotionAnalyzer(lang="en")

def transrate(data):
    url = 'https://translate.kakao.com/translator/translate.json'
    headers = {
        "Referer": "https://translate.kakao.com/",
        "User-Agent": "Mozilla/5.0"
    }
    query = {
        "queryLanguage": "ko",
        "resultLanguage": "en",
        "q": data
    }
    resp = requests.post(url, headers=headers, data=query)
    query = resp.json()
    output = query['result']['output'][0][0]
    return output

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    # success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/create.html'
    def form_valid(self, form):
        form.instance.writer = self.request.user # Foreign Key 지정하여 삽입하기 위한 코드
        return super().form_valid(form)

    def get_success_url(self):# self.object는 target_object와 동일하다고 보면 됨
        obj = Article.objects.get(pk=self.object.id)
        content = obj.content
        content = re.sub('<.>|</.>', '', content)
        transrated_content = transrate(content)
        emotion = emotion_analyzer.predict(transrated_content)
        obj.others = emotion.probas['others']
        obj.joy = emotion.probas['joy']
        obj.surprise = emotion.probas['surprise']
        obj.disgust = emotion.probas['disgust']
        obj.anger = emotion.probas['anger']
        obj.sadness = emotion.probas['sadness']
        obj.fear = emotion.probas['fear']
        obj.save()
        return reverse('articleapp:detail', kwargs={'pk':self.object.pk})

class ArticleDetailView(DetailView, FormMixin):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'
    form_class = CommentCreationForm


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/update.html'

    def get_success_url(self):# self.object는 target_object와 동일하다고 보면 됨
        return reverse('articleapp:detail', kwargs={'pk':self.object.pk})


class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/delete.html'


class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 20
    