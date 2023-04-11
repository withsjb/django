from django.db import models

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=200)
    # 제목
    content = models.TextField() #내용
    create_date = models.DateTimeField() #작성일지

    def __str__(self) -> str:
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #foreignkey는 질문에 대한 답으로 question하고 연결하는데 사용됨 on_delete=models.CASCADE는 질문이 삭제될경우 답변도 삭제 cascade는 질문에 대한 모든 답변을 삭제한다는 의미도 있음
    content = models.TextField()
    create_date = models.DateTimeField()



class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)