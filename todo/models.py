from django.db import models

# Create your models here.

PRIORITY = (("danger","高"),("info","中"),("success","低"))
class TodoModel(models.Model):
    title = models.CharField(max_length=100,verbose_name="タイトル")
    memo = models.TextField(verbose_name="メモ")
    priority = models.CharField(
        max_length=10,choices=PRIORITY,verbose_name="優先度")
    duedate = models.DateField(verbose_name="期限")
    creator = models.ForeignKey("auth.User",  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title