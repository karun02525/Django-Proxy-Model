from django.db import models
from datetime import datetime    
import uuid

# Create your models here.
class BaseModel(models.Model):
    base_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class ExamCenter(BaseModel):
    base_id= None
    cname = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    
class Student(ExamCenter):
    base_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    roll = models.IntegerField()    
    
class ProxyStudent(Student):
    class Meta:
        proxy=True
        ordering = ['roll']   


class Teacher(BaseModel):
    base_id= None
    teacher_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False),
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    city = models.CharField(max_length=20)
    