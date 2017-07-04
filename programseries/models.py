from ckeditor.fields import RichTextField
from django.db import models
class Program_Serie(models.Model):
    Title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    logo = models.FileField()
    Company = models.CharField(max_length=200)
    def __str__(self):
        return self.Title+"-"+self.Company

class Program(models.Model):
    serie = models.ForeignKey(Program_Serie, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    program_title = models.CharField(max_length=250)
    Logo = models.FileField()
    price = models.FloatField(max_length=100)
    codeprice = models.FloatField(max_length=200)
    text = RichTextField(max_length=1000000)
    def __str__(self):
        return self.program_title