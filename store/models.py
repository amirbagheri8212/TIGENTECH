from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User

class money(models.Model):
    moneynow = models.IntegerField()
    Person = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.Person.first_name+" _ "+self.Person.last_name+" |$$$| "+str(self.moneynow)
class ItemGroup(models.Model):
    Group_name = models.CharField(max_length=30)
    Type = models.CharField(max_length=30)
    Company = models.CharField(max_length=30)
    About = RichTextField()
    def __str__(self):
        return self.Group_name+" |###| "+self.Type+" |^^^| "+self.Company
class Item(models.Model):
    Name = models.CharField(max_length=30)
    Company = models.CharField(max_length=35)
    Price = models.IntegerField()
    Year = models.CharField(max_length=4)
    Aboutit = RichTextField()
    group = models.ForeignKey(ItemGroup, on_delete=models.CASCADE)
    is_VIP = models.BooleanField()
    log = models.ImageField()
    Publish_Time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Name+" | *** | "+self.Company+" | ### | "+self.group.Group_name+" | $$$ | "+str(self.Price)+" | &&& | "+self.Year
