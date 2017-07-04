from django.db import models
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
def dp(list):
    list1 = ()
    for i in list:
        list1+=((i,i,),)
        return list1
class genre(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Country(models.Model):
    Name = models.CharField(max_length=5000)
    Continents = (
        ("Asia","Asia"),
        ("North America","North America"),
        ("South America","South America"),
        ("Australia","Australia"),
        ("Europe","Europe"),
        ("Africa","Africa"),
    )
    continent = models.CharField(max_length=1000,choices=Continents)
    def __str__(self):
        return self.Name
class Manager(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    PictureFile = models.ImageField()
    Bio = RichTextField()
    Major = models.CharField(max_length=10000)
    Interest_Fields = TaggableManager()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Company(models.Model):
    Name = models.CharField(max_length=700)
    master = models.ForeignKey(Manager,on_delete=models.CASCADE)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    DateOfCreation = models.DateField()
    def __str__(self):
        return self.Name
class Job(models.Model):
    job = models.CharField(max_length=500)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    def __str__(self):
        return self.job
        
class Person(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    PictureFile = models.ImageField()
    Job = models.ForeignKey(Job,on_delete=models.CASCADE)
    Bio = RichTextField()
    Major = models.CharField(max_length=10000)
    Interest_Fields = TaggableManager()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class post(models.Model):
    Title = models.CharField(max_length=100)
    genre = models.ForeignKey(genre,on_delete=models.CASCADE)
    authur = models.ForeignKey(Person,on_delete=models.CASCADE)
    Company = models.ForeignKey(Company,on_delete=models.CASCADE)
    First_Display = RichTextField()
    Complete_Text = RichTextField()
    Publish_Time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Title+" ^*^ "+self.genre.title+" ^*^ "+self.authur.name