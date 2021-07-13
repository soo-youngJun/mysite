from django.db import models

# 질문 모델(테이블)
class Question(models.Model):   # 질문 게시판
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

# 답변 모델(테이블)
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 질문 삭제 시 답변도 삭제
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return str(self.question)
