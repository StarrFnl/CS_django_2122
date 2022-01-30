from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Post(models.Model):
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True, default=None)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    viewCount = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    # click_count

    class Meta:
        abstract = True

class Reply(models.Model):
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField()

    class Meta:
        abstract = True
        #model에서 reply_sell은 새로 만들고 image도 추가할 수 있게 옵션주기? 후기 같은 느낌

# # image 여러 개 하려면 외부키로 줘야 하는데 post가 abstract라 외부키가 안먹음. 그러면 post별로 각자 연결시켜야하나?
# class Photo(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
#     image = models.ImageField(upload_to='images/', blank=True, null=True)


class Post_Normal(Post):
    #author = models.ForeignKey(User, related_name = "post_normal_author", on_delete=models.CASCADE)
    #개체관계에 사용할 이름 추가 필요
    def __str__(self):
        return self.subject



class Reply_Normal(Reply):
    author = models.ForeignKey(User, related_name = "reply_normal_author", on_delete=models.CASCADE)
    post = models.ForeignKey(Post_Normal, related_name = "replied_post_normal",on_delete=models.CASCADE)


class Post_Evaluate(Post):
    author = models.ForeignKey(User, related_name = "post_evaluate_author", on_delete=models.CASCADE)
    rate = models.FloatField(default=0.0)


class Reply_Evaluate(Reply):
    author = models.ForeignKey(User, related_name = "reply_evaluate_author", on_delete=models.CASCADE)
    post = models.ForeignKey(Post_Evaluate, related_name = "replied_post_evaluate", on_delete=models.CASCADE)
    reeScore = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])



