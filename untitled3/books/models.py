from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime
# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=32,verbose_name='书籍名称')
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    image = models.ImageField(upload_to="", verbose_name="封面图片", null=True, blank=True)
    autor = models.CharField(max_length=12,verbose_name='作者')
    book_desc = models.CharField(max_length=256,verbose_name='书籍介绍')

    class Meta:
        verbose_name = '书籍列表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

