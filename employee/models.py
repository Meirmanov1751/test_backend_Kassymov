from django.db import models
from mptt.models import MPTTModel, TreeForeignKey



class Employee(MPTTModel):
    class MPTTMeta:
        order_insertion_by = ['name']

    name = models.CharField(max_length=200,help_text="Имя")
    surname = models.CharField(max_length=200,help_text="Фамилия")
    patronymic = models.CharField(max_length=200,help_text="Отчество")
    position = models.CharField(max_length=150)
    employment_date = models.DateTimeField()
    salary = models.IntegerField(default=100000)
    photo = models.ImageField(blank=True)
    parent = TreeForeignKey('Employee',on_delete=models.CASCADE,null=True,blank=True,related_name='less_weighty')

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    def save(self, *args, **kwargs):
        super(Employee, self).save(*args, **kwargs)

