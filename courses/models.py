from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name

class Faculty(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=True,max_length=100)
    email = models.EmailField()
    department = models.ManyToManyField(to=Department)
    date_hired = models.DateField()
    date_end = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.name


class Stage(MPTTModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default='untitled')
    parent = TreeForeignKey(to='self',on_delete=models.CASCADE,null=True,blank=True,related_name='children')

    def __str__(self):
        return self.name


class Proposal(models.Model):
    id = models.AutoField(primary_key=True)
    stage = models.OneToOneField(to=Stage,on_delete=models.CASCADE,null=True)
    owner = models.ManyToManyField(to=Faculty)
    name = models.CharField(null=True,max_length=100)
    department = models.OneToOneField(to=Department,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=True,max_length=100)
    department = models.OneToOneField(to=Department,on_delete=models.CASCADE,null=True)
    teacher = models.ManyToManyField(to=Faculty)
    description = models.TextField(null=True,blank=True)
    proposal = models.OneToOneField(to=Proposal,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name
