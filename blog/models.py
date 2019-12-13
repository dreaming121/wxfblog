from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class BlogType(models.Model):
    type_name = models.CharField(verbose_name="博客标签", max_length=30)

    def __str__(self):
        return self.type_name

class Blog(models.Model):
    tittle = models.CharField(verbose_name="标题", max_length=50)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING, verbose_name="博客标签")
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="作者")
    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    last_updated_time = models.DateTimeField(verbose_name="最后更新时间", auto_now=True)

    def __str__(self):
        return "<blog:%s>" % self.tittle
