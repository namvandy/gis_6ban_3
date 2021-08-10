from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    #User가 탈퇴했을 경우, 작성자 미상(게시글에서) 처럼 되게 한다.
    #OneToOne과 다른 점은 다대다도 가능하다.
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/')
    content = models.TextField(null=True)
    created_at = models.DateField(auto_now_add = True, null=True)


