from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
# Create your models here.
class qasession(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1)])
    detail = models.CharField(max_length=1000)
    create_at = models.DateTimeField(auto_now_add=True)
    close_at = models.DateField(blank=True, null=True)

class question(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    qa = models.ForeignKey(qasession, on_delete=models.CASCADE, null=True)
    content = models.TextField(max_length=2000)
    create_at = models.DateTimeField(auto_now_add=True)

class answer(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ques = models.ForeignKey(question, on_delete=models.CASCADE, null=True)
    content = models.TextField(max_length=2000)
    create_at = models.DateTimeField(auto_now_add=True)

class comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ans = models.ForeignKey(answer, on_delete=models.CASCADE, null=True)
    content = models.TextField(max_length=2000)
    create_at = models.DateTimeField(auto_now_add=True)
