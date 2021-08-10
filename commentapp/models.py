from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article

# target_article.comment.all() -> related_name

class Comment(models.Model):
    # 서버에서 해당 데이터를 가져오는 로직을 구성해야 한다.
    article = models.ForeignKey(Article, on_delete=models.SET_NULL,
                                related_name='comment', null=True) # related_name을 지정하여 해당 명칭으로 접근 가능하게 한다.

    # 서버에서 해당 데이터를 가져오는 로직을 구성해야 한다.
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='comment', null=True)

    content = models.TextField(null=False) # Null 불허

    # 서버에서 해당 데이터를 가져오는 로직을 구성해야 한다.
    created_at = models.DateTimeField(auto_now_add=True) # 시간이 자동으로 찍히게 됨

    