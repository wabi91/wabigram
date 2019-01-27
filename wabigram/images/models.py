from django.db import models
from wabigram.users import models as user_models

# Create your models here.
class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True) # 처음 생성되었을 때만 타임 Add
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # Meta 클래스는 무엇이든 이것은 필드가 아니다 라고 지정. (URL과 무관한 클래스라고 지정) : DataBase와 연결 안함

class Image(TimeStampedModel):

    """ Image Model """

    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User,on_delete=models.PROTECT,null=True)

    def __str__(self):
        return '{} ,글쓴이: {}(장소 {})'.format(self.caption, self.creator, self.location)

class Comment(TimeStampedModel):
    """ Comment Model """

    message = models.TextField()
    creator = models.ForeignKey(user_models.User,on_delete=models.PROTECT,null=True)
    image = models.ForeignKey(Image,on_delete=models.PROTECT,null=True)

    def __str__(self):
        return '댓글: {}, 글쓴이: {}'.format(self.message,self.creator)

class Like(TimeStampedModel):

    """ Like Model """
    
    creator = models.ForeignKey(user_models.User,on_delete=models.PROTECT,null=True)
    image = models.ForeignKey(Image,on_delete=models.PROTECT,null=True)

    def __str__(self):
        return 'Image caption: {}, 글쓴이: {}'.format(self.image.caption, self.creator.username)