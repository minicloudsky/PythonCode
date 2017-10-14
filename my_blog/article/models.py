from django.db import models

# Create your models here.
class Article(models.Model):
    #博客标题
    title = models.CharField(max_length=100)
    #博客标签
    category = models.CharField(max_length=50,blank=True)
    # blog date
    date_time = models.DateTimeField(auto_now_add=True)
    # blog content
    content = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title
    class Meta:
        #按照时间降序排列
        ordering = ['-date_time']
