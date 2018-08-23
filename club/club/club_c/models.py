#encoding=utf-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class clubUser(models.Model):
    user = models.OneToOneField(User)
    signature = models.CharField(max_length=125,default='This guy is too lazy to leave anything here~')
    photo = models.ImageField(upload_to='image_head/',default='image_head/timg.jpeg')
    def __str__(self):
        return self.user.username.encode('utf-8')

class palte(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name.encode('utf-8')

class Articals(models.Model):
    # 帖子主题
    title = models.CharField(max_length=125)
    # 帖子内容
    content = models.TextField()
    # 帖子发布时间
    create_time = models.DateTimeField(auto_now_add=True)
    # 作者
    author = models.ForeignKey(clubUser)
    # 点击量
    click_num = models.IntegerField(default=0)
    # 所属板块
    in_palte = models.ForeignKey(palte)

    def __str__(self):
        return self.title.encode('utf-8')
