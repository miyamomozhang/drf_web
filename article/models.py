from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# 自己的博客文章 model
class Article(models.Model):
    # 文章作者
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name="articles"
    )
    # 标题
    title = models.CharField(max_length=200)
    # 正文
    body = models.TextField(max_length=400)
    # 博客的创建时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 博客的更新时间
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
