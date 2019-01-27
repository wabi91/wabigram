from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True) # 처음 생성되었을 때만 타임 Add
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # Meta 클래스는 무엇이든 이것은 필드가 아니다 라고 지정. (URL과 무관한 클래스라고 지정) : DataBase와 연결 안함

class Image(TimeStampedModel):

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()


class Comment(TimeStampedModel):

    message = models.TextField()