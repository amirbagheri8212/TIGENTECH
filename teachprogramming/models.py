from django.db import models
from ckeditor.fields import RichTextField
class programlanguages(models.Model):
    Language_Name = models.CharField(max_length=20)
    Logo = models.FileField()#(max_length=100000)
    Country = models.CharField(max_length=30)
    text = RichTextField()#(max_length=10**6)
    def __str__(self):
        return self.Language_Name
class program(models.Model):
    Program = models.ForeignKey(programlanguages, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    teacher = models.CharField(max_length=20)
    Company = models.CharField(max_length=30)
    price = models.FloatField(max_length=100)
    text = RichTextField()
    type = models.CharField(max_length=26)
    log = models.FileField()#(max_length=10**7)
    def __str__(self):
        return self.name
