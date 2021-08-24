from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class LikeRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, # 연결되어 있는 유저 객체가 사라졌을 때, 발생되는 정책
                             related_name='like_record', null = False) # User 쪽에서 불러오고자 하는 이름, Not NUll
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='like_record') # Article 쪽에서 불러오고자 하는 이름 -> like_record



    class Meta:
        unique_together = ['user', 'article']
        # Unique Key 지정, 해당 쌍이 유니크 하도록 지정함
    

    

